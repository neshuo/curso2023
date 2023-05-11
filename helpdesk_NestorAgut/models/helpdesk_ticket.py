from odoo import api,fields,models
from odoo.exceptions import UserError

from datetime import timedelta

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

    @api.model
    def get_default_date(self):
        return fields.Date.today()
    

    #Fecha
    date= fields.Date(
        #string='descripcion',
        #help='añade una descripción para poder solucionar la incidencia'
        default=get_default_date,
    )

    #Fecha y hora limite
    date_limit= fields.Datetime(
        string='Limit Date & Time'
    )

    @api.onchange('date')
    def _onchange_date(sef):    
        if self.date:
            self.date_limit = self.date + timedelta(days=1)
        else:
            pass


    #Asignado
    assigned= fields.Boolean(
        readonly=True
    )

    tag_ids = fields.Many2many(
        relation='helpdesk_ticket_tag_rel',
        column1='ticket_id',
        column2='tag_id',
        string='Tags'
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

    #Clase 3.1
    #amount time debe ser mayor que 0
    @api.constrains('amount_time')
    def check_amount_time(self):
        for record in self:
            if record.amount_time < 0:
                raise UserError(_("Time cant be nagativve"))

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
        for record in self:
            record.write({
                    'tag_ids' : Command.create({'name': self.tag_name})
                }
            )

    def clear_tags(self):
        self.ensure_one()
        self.tag_ids=Command.Clear()

    def get_assigned(self):
        self.ensure_one()
        self.state = 'assigned'
        self.user_id = self.env.user
