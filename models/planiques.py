# -*-coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta

class AtmPlaniques(models.Model):
    _name = "atm.planiques"
    _description = "Planique"
    _rename = "name"



    def write(self, vals):
        user = self.env.user
        group_users= user.has_group('gestion_releve_rq.tableau_planique')

        if group_users !=True:
            raise models.UserError("Désolé, vous ne pouvez pas modifier ce planning. Veuillez voir l'administrateur !")
        res= super(AtmPlaniques, self).write(vals)

        return res


    user_id = fields.Many2one("res.users", string="Agent :")
    refer_id=fields.Many2one("atm.reference" , string="Réference :")
    type_round=fields.Selection([("C","C "),("R","R "),("M"," M"),("N"," N"),("J","J "),("AM","AM ")])
    date_plani=fields.Date("Date :")




