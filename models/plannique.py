# -*-coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta




class AtmPlannique(models.Model):
    _name = "atm.plannique"
    _description = "planniques"
    _rename = "name"

    def test(self):
        return 'conde'

    def write(self, vals):
        user = self.env.user
        group_users = user.has_group('gestion_releve_rq.tableau_planique')

        if group_users != True:
            raise models.UserError("Désolé, vous ne pouvez pas modifier ce planning. Veuillez voir l'administrateur !")
        res = super(AtmPlannique, self).write(vals)

        return res


    name=fields.Char(string="Mois :")
    user_id = fields.Many2one("res.users", string="Agents:")
    period1=fields.Char("P1")
    period2 = fields.Char("P2")
    period3 = fields.Char("P3")
    period4 = fields.Char("P4 ")
    period5 = fields.Char("P5")
    period6 = fields.Char("P6")
    period7 = fields.Char("P7")
    period8 = fields.Char("P8")
    period9 = fields.Char("P9")
    period10 = fields.Char("P10")
    period11= fields.Char("P11")
    period12= fields.Char("P12")
    period13= fields.Char("P13")
    period14= fields.Char("P14")
    period15 = fields.Char("P15")
    period16 = fields.Char("P16")
    period17 = fields.Char("P17")
    period18 = fields.Char("P18")
    period19 = fields.Char("P19")
    period20 = fields.Char("P20")
    period21 = fields.Char("P21")
    period22 = fields.Char("P22")
    period23 = fields.Char("P23")
    period24 = fields.Char("P24")
    period25 = fields.Char("P25")
    period26 = fields.Char("P26")
    period27 = fields.Char("P27")
    period28 = fields.Char("P28")
    period29 = fields.Char("P29")
    period30 = fields.Char("P30")
    period31 = fields.Char("P31")


