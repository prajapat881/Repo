from flectra import api, fields, models


class StaffInfo(models.Model):
    _name = "staff.info"
    _order='hand'
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

    @api.onchange("bank_staff_id")
    def _compute_customer(self):
        self.ifsc_code = self.bank_staff_id.bank_ifsc_code
        print("Customer count")

    total_staff = fields.Integer("")
    name = fields.Char("Name")
    staff_post = fields.Char("Post")
    staff_pan = fields.Char("Pan no")
    staff_mobile = fields.Integer("Mobile No",size=12)
    staff_image = fields.Binary("Image")
    ifsc_code = fields.Char('IFSC Code')
    bank_staff_id = fields.Many2one("bank.info", string="Bank")
    state = fields.Selection([('draft', 'Draft'), ('done', 'Accept'),
                              ('cancel', 'Reject')], default='draft')
    hand=fields.Integer("Sequence")

    _sql_constraints = [
        ('staff_info_staff_pan', 'UNIQUE (staff_pan)', 'Pan No. must be unique!'),
    ]

