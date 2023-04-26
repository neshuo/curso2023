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
        String='nombre',
        requiered=True,
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
        String='Limit Date & Time'
    )

    #Asignado
    assigned= fields.Boolean(
        readonly=True
    )
    user_id = fields.Many2one(
        comodel_name='res.users',
        String='assigned'
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
