from odoo import api,fields,models

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

    color = fields.Integer('Color Index', default=0)

    amount_time = fields.Float(
        string='Amount of time'
    )


    #CLASE 2.2

    assigned = fields.Boolean(
        compute= '_compute_assigned',
        search= '_search_assigned',
        inverse='_inverse_assigned',
    )

    @api.depends('user_id')
    def _compute_asigned(self):
        for record in self:
            record.assigned = bool(record.user_id)

    def _search_assigned(self, operator, value):
        if operator == '=' and value == True:
            operator = '!='
        else:
            operator = '='
        return[('user_id',operator,False)]
    
    def _inverse_assigned(self):
        for record in self:
            if not record.assigned:
                record.user_id = False
            else:
                record.user_id = self.env.user

    
    tag_name = fields.Char()

    def create_tag(self):

        #self.ensure_one()
        #self.write({'tag_ids': Command.create({'name' : self.tag_name})})
        for record in self:
            record.write({
                    'tag_ids' : Command.create({'name': self.tag_name})
                }
            )

    def clear_tags(self):
        self.ensure_one()
        self.tag_ids=Command.Clear()
