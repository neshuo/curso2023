from odoo import fields,models

class Helpdesktickets(models.Model):
    _name= 'helpdesk.ticket'
    _description= 'Helpdesk Ticket' 


    #Nombre
    name= fields.Char()

    #Descripción
    description= fields.Text()

    #Fecha
    date= fields.Date()

    #Fecha y hora limite
    date_limit= fields.Datetime(
        String='Limit Date & Time'
    )

    #Asignado
    assigned= fields.Boolean()

    #Acciones a realizar
    actions_todo= fields.Html()