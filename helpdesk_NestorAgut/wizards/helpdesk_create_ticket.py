from odoo import models,api,fields

#Clase 3.2, comentar hasta terminar 3.1#
class HelpdeskCreateTicket(models.TransientModel):
    _name='helpdesk.create.ticket'
    _description='Helpdesk ticket'

    tag_id = fields.Many2one(
        'helpdesk.ticket.tag',
        string='Tag',
        required=True,
    )
    name = fields.Char(string='Subject', required=True)
    description = fields.Text(string='Description', required=True)

    def create_ticket(self):
        ticket = self.env['helpdesk.ticket'].create({
            'name': self.name,
            'description': self.description,
            'tag_ids': [(4, self.tag_id.id)],
        })
        return {
            'name': _('Ticket'),
            'view_mode': 'form',
            'res_model': 'helpdesk.ticket',
            'res_id': ticket.id,
            'type': 'ir.actions.act_window',
        }