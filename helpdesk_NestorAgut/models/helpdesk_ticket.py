from odoo import fields,models

class Helpdesktickets(models.Model):
    _name= 'helpdesk.ticket'
    _description= 'Helpdesk ticket' 


    #secuencia
    sequence=fields.Integer(
        default=10,
        help="Secuencia de orden"
    )

    #Nombre
    name= fields.Char(
        string='nombre',
        required=True,
        help='nombre de la tarea'
    )

    #Descripción
    description= fields.Text()

    #Fecha
    date= fields.Date(
        string='descripcion',
        help='añade una descripción para poder solucionar la incidencia'
    )

    #Fecha y hora limite
    date_limit= fields.Datetime(
        string='Limit Date & Time'
    )

    #Asignado
    assigned= fields.Boolean(
        readonly=True
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        string='assigned'
    )

    #Acciones a realizar
    actions_todo= fields.Html()

    #Campo etiqueta nuevo
    state = fields.Selection(
        selection=[
            ('new','New'),
            ('assigned','Assigned'),
            ('in progres','In Progress'),
            ('completed','Completed'),
            ('canceled','Canceled')
        ],
        default = 'new'
    )

    tag_ids = fields.Many2many(
        comodel_name='helpdesk.ticket.tag',
        string='Tags'
    )
    
    action_ids = fields.One2many(
        comodel_name='helpdesk.ticket.action',
        inverse_name='ticket_id',
        string='Actions'
    )

    def set_actions_as_done(self):
        self.ensure_one()
        self.action_ids.set_done()