from flectra import api, fields, models


class BankInfo(models.Model):
    _name = 'bank.info'

    @api.multi
    def button_done(self):
        for rec in self:
            rec.state = 'done'

    @api.multi
    def button_cancel(self):
        for rec in self:
            rec.write({'state': 'cancel'})

    @api.multi
    def button_draft(self):
        for rec in self:
            rec.write({'state': 'draft'})

    name = fields.Char("Bank Name")
    bank_registration_no = fields.Integer("Reg.No.")
    bank_ifsc_code = fields.Char("IFSC Code")
    bank_mobile = fields.Integer("Phone No.", size=12)
    bank_address = fields.Char('Address')
    staff_number = fields.Char("Total Staff")
    staff_bank_line = fields.One2many('staff.info', 'bank_staff_id' )
    customer_bank_line = fields.One2many('customer.info', 'bank_customer_id')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Accept'),
                              ('cancel', 'Reject'), ], default='draft')

    def compute_customer(self):

        for number in self:
            number.staff_number = len(number.staff_bank_line)

    _sql_constraints = [
        ('bank_info_name', 'UNIQUE (name)', 'Bank Name must be unique!'),
        ('bank_info_bank_registration_no', 'UNIQUE (bank_registration_no)', 'Registration Number must be unique!'),
        ('bank_info_bank_ifsc_code', 'UNIQUE (bank_ifsc_code)', 'IFSC Code must be unique!')
    ]

    # @api.constrains(name)
    # def bankname(self):
    #     for bname in self:
    #         if self.name == bname:
    #             raise ValidationError('bank not same')
