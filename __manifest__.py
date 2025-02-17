# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>

{
    'name': 'gestion releve',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
     ce module permettant de gerer les demande changement
    """,
    'depends': ['base','web','mail'],
    'data': [
            'security/ir.model.access.csv',
            'security/refuse_login.xml',
            'views/plannique.xml',
           # "automatisation/ligne_vide_releve.xml",
            'wizard/wizard_rapport_releve.xml',
             "wizard/mise_a_jour.xml",
            'rapports/template_releve_equipement.xml',
            'rapports/template_vacation2.xml',
            'rapports/template_vacation3.xml',
            'views/menu_generale.xml',
            #'rapports/report_demande_pdf.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
