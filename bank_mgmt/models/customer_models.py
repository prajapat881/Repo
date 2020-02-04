from flectra import api, fields, models


class CustomerInfo(models.Model):
    _name = 'customer.info'

    @api.multi
    def button_done(self):
        for rec in self:
            rec.write({'state': 'done'})

    @api.multi
    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    @api.multi
    def button_draft(self):
        for rec in self:
            rec.write({'state': 'draft'})

    _sql_constraints = [
        ('customer_info_customer_pan', 'UNIQUE (customer_pan)', 'Pan No. must be unique!'),
        ('customer_info_customer_aadhar', 'UNIQUE (customer_aadhar)', 'Aadhar No. must be unique!'),
    ]

    total_bank = fields.Char("No. Bank")
    name = fields.Char("Name")
    date = fields.Date("Date")
    customer_pan = fields.Char("Pan No")
    customer_aadhar = fields.Char("Aadhar Card No")
    customer_mobile = fields.Integer("Mobile No", size=12)
    customer_email = fields.Char("Email ID")
    customer_image = fields.Binary("Image")
    customer_bank_ids = fields.Many2many('bank.info', string="Bank Name")
    state = fields.Selection([('draft', 'Draft'), ('done', 'Accept'),
                              ('cancel', 'Reject'), ], default='draft')
    bank_customer_id=fields.Many2one('bank.info',string="Bank")
    def compute_customer(self):
        for number in self:
            number.total_bank = len(number.customer_bank_ids)

    @api.multi
    def create_bank(self, ):
        return {
            'name': 'Bank Info',
            'view_type': 'form',
            'view_mode': 'tree',
            'type': 'ir.actions.act_window',
            'res_model': 'bank.info',
            'domain': [('name', '=','name')],
        }
