from odoo import api,fields,models

class helpdeskTicketTag (models.Model):
    _name= 'helpdesk.ticket.tag'
    _description= 'Helpdesk Ticket Tag'

    #Nombre

    name = fields.Char(
        required=True
    )

    
    @api.model
    def _clean_tags_cron(self):
        tags = self.search([('ticket_ids', '=', False)])
        tags._clean_tags()

    #@api.model()
    #def _clean_tags(self):
    #    self.search([('ticket_ids','=',False)]).unlink()