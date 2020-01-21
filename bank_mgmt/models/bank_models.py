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
    bank_registration_no = fields.Integer("Registration No.")
    bank_ifsc_code = fields.Char("IFSC Code")
    bank_mobile = fields.Integer("Phone No.")
    bank_address = fields.Char('Address')
    staff_number = fields.Char("Total Staff")
    staff_bank_line = fields.One2many('staff.info', 'bank_staff_id', string="Employes")
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

#
# class CustomerInfo(models.Model):
#     _name = 'customer.info'
#
#     _sql_constraints = [
#         ('customer_info_customer_pan',
#          'UNIQUE (customer_pan)',
#          'Pan No. must be unique!')
#     ]
#
#     total_bank = fields.Char("No. Bank")
#     name = fields.Char("Customer Name")
#     customer_pan = fields.Char("Pan No")
#     customer_aadhar = fields.Char("Aadhar Card No")
#     customer_mobile = fields.Integer("Mobile No")
#     customer_email = fields.Char("Email ID")
#     customer_image = fields.Binary("Customer Image")
#     customer_bank_ids = fields.Many2many('bank.info', string="Bank Name")
#
#     def compute_customer(self):
#         for number in self:
#             number.total_bank = len(number.customer_bank_ids)
#         print("Customer count")
#
#
# class BankStaff(models.Model):
#     _name = "staff.info"
#
#     @api.onchange("bank_staff_id")
#     def _compute_customer(self):
#         self.ifsc_code = self.bank_staff_id.bank_ifsc_code
#         print("Customer count")
#
#     total_staff = fields.Integer("")
#     name = fields.Char("Staff Name")
#     staff_post = fields.Char("Staff Post")
#     staff_pan = fields.Char("Staff Pan no")
#     staff_mobile = fields.Integer("Mobile No")
#     staff_image = fields.Binary("Staff Image")
#     ifsc_code = fields.Char('IFSC Code')
#     bank_staff_id = fields.Many2one("bank.info", string="Bank")
