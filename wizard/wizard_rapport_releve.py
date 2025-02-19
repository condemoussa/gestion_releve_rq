# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import AccessError

class RapportReleve(models.TransientModel):
    _name = "rapport.releve"
    _description = "Rapport relevés"

    dat_releve = fields.Datetime("Date du relevé :", default=lambda self: fields.Datetime.now())
    vacation = fields.Selection(
        [("vacat1", "VACATION 1: 08h à 14h"),
         ("vacat2", "VACATION 2: 14h à 20h"),
         ("vacat3", "VACATION 3: 20h à 08h")],
        string="Vacation"
    )
    dat_debut = fields.Date("Date de début", default=lambda self: fields.Date.today(),required=True)
    dat_fin = fields.Date("Date de fin", default=lambda self: fields.Date.today(),required=True)
    val_anne = fields.Char("Année", compute="extract_date_info")
    val_mois = fields.Char("Mois", compute="extract_date_info")
    val_jour = fields.Char("Jour", compute="extract_date_info")
    date_recherche = fields.Date("Date recherche", compute="extract_date_info")

    @api.onchange("dat_releve")
    def extract_date_info(self):
        for record in self:
            date_time = record.dat_releve
            if date_time:
                # Extraction de l'année, du mois et du jour à partir du champ datetime
                record.val_anne = str(date_time.year)
                record.val_mois = str(date_time.month)
                record.val_jour = str(date_time.day)
                record.date_recherche = date_time.date()

    def releve(self):
        if self.date_recherche:
            requete_sql = """
                SELECT equipement.name, relev.statut, relev.observat, relev.value, relev.ronde, relev.ronde3, relev.ronde2
                FROM atm_releve AS relev
                JOIN res_users AS val_user ON relev.user_id = val_user.id
                JOIN atm_equipement AS equipement ON relev.equi_id = equipement.id
                WHERE relev.vacation = %s
                AND relev.date_cache BETWEEN %s AND %s
                ORDER BY relev.id DESC
            """

            # Exécution de la requête SQL
            self.env.cr.execute(requete_sql, (self.vacation, self.dat_debut, self.dat_fin))
            reponse_releve = self.env.cr.fetchall()


            # Préparer les données pour le rapport
            data = {
                'form_data': self.read()[0],
                'resultat': reponse_releve,
                'date_debut': self.dat_debut,
                'date_fin': self.dat_fin,
            }

            # Génération du rapport PDF
            return self.env.ref('gestion_releve_rq.action_rapport_releve_equipement_pdf').with_context(
                landscape=True).report_action(self, data=data)

    def releve_vacation2(self):
        if self.date_recherche:
            requete_sql = """
                   SELECT equipement.name, relev.statut, relev.observat, relev.value, relev.ronde, relev.ronde3, relev.ronde2
                   FROM atm_releve AS relev
                   JOIN res_users AS val_user ON relev.user_id = val_user.id
                   JOIN atm_equipement AS equipement ON relev.equi_id = equipement.id
                   WHERE relev.vacation = %s
                   AND relev.date_cache BETWEEN %s AND %s
                   ORDER BY relev.id DESC
               """

            # Exécution de la requête SQL
            self.env.cr.execute(requete_sql, (self.vacation, self.dat_debut, self.dat_fin))
            reponse_releve = self.env.cr.fetchall()


            # Préparer les données pour le rapport
            data = {
                'form_data': self.read()[0],
                'resultat': reponse_releve,
                'date_debut': self.dat_debut,
                'date_fin': self.dat_fin,
            }

            # Génération du rapport PDF
            return self.env.ref('gestion_releve_rq.action_rapport_releve_equipement_pdf_vacation2').with_context(
                landscape=True).report_action(self, data=data)

    def releve_vacation3(self):
        if self.date_recherche:
            requete_sql = """
                   SELECT equipement.name, relev.statut, relev.observat, relev.value, relev.ronde, relev.ronde3, relev.ronde2
                   FROM atm_releve AS relev
                   JOIN res_users AS val_user ON relev.user_id = val_user.id
                   JOIN atm_equipement AS equipement ON relev.equi_id = equipement.id
                   WHERE relev.vacation = %s
                   AND relev.date_cache BETWEEN %s AND %s
                   ORDER BY relev.id DESC
               """

            # Exécution de la requête SQL
            self.env.cr.execute(requete_sql, (self.vacation, self.dat_debut, self.dat_fin))
            reponse_releve = self.env.cr.fetchall()


            # Préparer les données pour le rapport
            data = {
                'form_data': self.read()[0],
                'resultat': reponse_releve,
                'date_debut': self.dat_debut,
                'date_fin': self.dat_fin,
            }

            # Génération du rapport PDF
            return self.env.ref('gestion_releve_rq.action_rapport_releve_equipement_pdf_vacation3').with_context(
                landscape=True).report_action(self, data=data)
