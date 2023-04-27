# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "helpdesk Nestor Agut",
    "summary": "Gestion incidencias de nestor",
    "version": "16.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/neshuo",
    "author": "Datanalisis, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "views/helpdesk_Nestor.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_tag.xml"
    ],
}