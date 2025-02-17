# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import AccessError

class RapportJour(models.TransientModel):
    _name = "rapport.jour"
    _description = "Mise à jour equipement"

    jour = fields.Char("Jour")



    def actualise_equipement(self):
        equipement = self.env["atm.equipement"].search([])
        for line in equipement:
            line.update({
                "etat_equi": "on"
            })

