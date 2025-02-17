# -*-coding: utf-8 -*-
from email.policy import default

from odoo import _, models, fields, api
from odoo.addons.test_impex.models import field
from odoo.exceptions import ValidationError ,UserError
from datetime import datetime, timedelta



class AtmEquipement(models.Model):
    _name = "atm.equipement"
    _description = "Equiment "
    _rename = "name"

    name=fields.Char("Libellé :")
    etat_equi=fields.Selection([  ("on","ON"),("off","OFF") ],string="Etat",default="on")
    val_pos=fields.Char("Valeur possible :" , size=80)



class AtmReleve(models.Model):
    _name="atm.releve"
    _description = "Relevé "
    _rename = "name"




    @api.model
    def create(self, vals):
        res = self._check_vacation_ronde(vals, super(AtmReleve, self).create)
        res["name"] = "Rélevé N°00"+str(res["id"])

        return res

    def supprime_ligne_vide(self):
        dernier_enregistrement = self.search([('observat', '=',''),('value','=','')])
        print(dernier_enregistrement)
        dernier_enregistrement.unlink()




    def _check_vacation_ronde(self, vals, operation):
        vacat = vals.get('vacation', self.vacation)
        ronde1 = vals.get('ronde', self.ronde)
        ronde2 = vals.get('ronde2', self.ronde2)
        ronde3 = vals.get('ronde3', self.ronde3)

        dat = vals.get('dat_releve', self.dat_releve)

        if isinstance(dat, str):
            dat_releve = fields.Datetime.from_string(dat)
        else:
            dat_releve = dat

        # determination de l'heure et de la minutes  dat_releve.hour  dat_releve.minute
        heure = 14
        minute = 11

        if vacat == "vacat1":  # "VACATION 1: 08h à 14h"
            if ronde1 == "rond1" and heure == 10 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde1 == "rond2" and heure == 12 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde1 == "rond3" and heure == 14 and 0 <= minute <= 59:
                return operation(vals)
            else:
                raise UserError("Ronde non valide pour cette vacation. Veuillez vérifier l'heure svp.")

        elif vacat == "vacat2":  # "VACATION 2: 14h à 20h"
            if ronde2 == "rond_1" and heure == 16 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde2 == "rond_2" and heure == 18 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde2 == "rond_3" and heure == 20 and 0 <= minute <= 59:
                return operation(vals)
            else:
                raise UserError("Ronde non valide pour cette vacation. Veuillez vérifier l'heure svp.")

        elif vacat == "vacat3":  # "VACATION 2: 14h à 20h"
            if ronde3 == "ronde1" and heure == 22 and 00 <= minute <= 59:
                return operation(vals)
            elif ronde3 == "ronde2" and heure == 0 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde3 == "ronde3" and heure == 2 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde3 == "ronde4" and  heure == 4 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde3 == "ronde5" and heure == 6 and 0 <= minute <= 59:
                return operation(vals)
            elif ronde3 == "ronde6" and heure == 8 and 0 <= minute <= 59:
                return operation(vals)
            else:
                raise UserError("Ronde non valide pour cette vacation. Veuillez vérifier l'heure svp.")

        else:
            raise UserError("Vacation non valide.")

    def actualise_equipement(self):
        equipement = self.env["atm.equipement"].search([])
        for line in equipement :
            line.update({
                "etat_equi" :"on"
            })

    def vider_champs(self):
        self.value = ""
        self.observat = ""
        self.statut = ""


    def save_and_next(self):
        # Assure que l'enregistrement actuel est sauvegardé (vous pouvez éventuellement omettre cela)
        self.ensure_one()
        # Crée un nouvel enregistrement avec des valeurs par défaut ou récupérées depuis l'enregistrement actuel
        new_vals = {
            'name': self.name,  # Utilisez les valeurs actuelles ou générez-en de nouvelles
            'dat_releve': fields.Datetime.now(),  # Exemple de valeur par défaut pour la date
            # Ajoutez d'autres champs selon vos besoins
            'vacation': self.vacation,
            'ronde': self.ronde,
            'ronde2': self.ronde2,
            'ronde3': self.ronde3,
            'observat': self.observat,
            'statut': self.statut,
            'value': self.value,
            'equi_id': self.equi_id.id,
            'user_id': self.env.user.id,  # Associe le nouvel enregistrement à l'utilisateur actuel
        }

        # Crée un nouvel enregistrement dans le modèle atm.releve
        new_releve = self.create(new_vals)
        if new_releve :
            id_equipement = new_releve.equi_id.id
            equipement = self.env["atm.equipement"].browse(id_equipement)
            equipement.update({"etat_equi": "off" })
            new_releve.vider_champs()



        # Si un nouvel enregistrement est créé, redirige vers celui-ci
        if new_releve:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'atm.releve',
                'view_mode': 'form',
                'res_id': new_releve.id,
                'target': 'current',
            }
        else:
            raise UserError("Impossible de créer le nouvel enregistrement.")




    name=fields.Char("Libellé :")
    vacation = fields.Selection(
        [("vacat1", "VACATION 1: 08h à 14h"),
                 ("vacat2", "VACATION 2: 14h à 20h"),
                 ("vacat3", "VACATION 3: 20h à 08h"),
        ],string="Vacation"
    )
    ronde = fields.Selection(
        [("rond1", "RONDE 1 (10h)"),
                 ("rond2", "RONDE 2 (12h)"),
                 ("rond3", "RONDE 3 (14h)"),
         ], string="Ronde"
    )
    ronde2 = fields.Selection(
        [("rond_1", "RONDE 1 (16h)"),
            ("rond_2", "RONDE 2 (18h)"),
            ("rond_3", "RONDE 3 (20h)"),
         ], string="Ronde"
    )
    ronde3 = fields.Selection(
        [("ronde1", "RONDE 1 (22h)"),
                 ("ronde2", "RONDE 2 (00h)"),
                 ("ronde3", "RONDE 3 (02h)"),
                 ("ronde4", "RONDE 4 (4h)"),
                 ("ronde5", "RONDE 5 (06h)"),
                 ("ronde6", "RONDE 6(08h)"),

         ], string="Ronde"
    )
    observat = fields.Text("Observation ")
    statut = fields.Selection(
        [("ok", "OK"),
                 ("on", "ON"),
                ("off", "OFF"),
        ],string="Statut"
    )
    value  = fields.Char("Valeur")
    equi_id = fields.Many2one("atm.equipement", string="Equipement :", domain=[('etat_equi', '=','on')])
    # libelle_equipe=fields.Char(related="equi_id.libelle" ,string="Libellé :")
    # val_sais=fields.Char("Valeur saisie :")
    dat_releve=fields.Datetime("Date du relevé :" ,default=lambda self:fields.Datetime.now())
    user_id = fields.Many2one(
        "res.users",
        string="Agent",
        default=lambda self: self.env.user.id , readonly=True
    )
    date_cache = fields.Date("Date", default=lambda self: fields.Date.today())









