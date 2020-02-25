from flectra import http
from werkzeug.exceptions import NotFound
from flectra.http import request


class CustomerForm(http.Controller):
    @http.route(['/customer/form'], type='http', auth="public", website=True)
    def customer_form(self, **kwargs):
        bank_ids = request.env['bank.info'].search([])
        return request.render('bank_mgmt.newcustomer', {'bank_ids':bank_ids})

    @http.route(['/customer/form/submit'], type='http', auth="public", website=True)
    def customer_form_submit(self, **post):
        bank = request.httprequest.args.getlist('customer_bank')
        ids = [int(i) for i in bank]

        customer = request.env['customer.info'].create({
            'name': post.get('name'),
            'customer_pan': post.get('customer_pan'),
            'customer_aadhar': post.get('customer_aadhar'),
            'customer_mobile': post.get('customer_mobile'),
            'customer_email': post.get('customer_email'),
            'customer_bank_ids': [[6, 0, ids]],
        })

        return request.render('bank_mgmt.newcustomer_form', {'customer': customer, })




        """

                Staff Creating form

        """


class StaffForm(http.Controller):
    @http.route(['/staff/form'], type='http', auth="public", website=True)
    def staff_form(self, **kwargs):
        bank_id = request.env['bank.info'].search([])
        return request.render('bank_mgmt.newstaff', {'bank_id':bank_id})

    @http.route(['/staff/form/submit'], type='http', auth="public", website=True)
    def staff_form_submit(self, **post):
        bank = request.httprequest.args.getlist('bank_staff')
        ids = [int(i) for i in bank]

        staff = request.env['staff.info'].create({
            'name': post.get('name'),
            'staff_post': post.get('staff_post'),
            'staff_pan': post.get('staff_pan'),
            'staff_mobile': post.get('staff_mobile'),
            'ifsc_code': post.get('ifsc_code'),
            'bank_staff_id':[[6, 0, ids]],
        })

        return request.render('bank_mgmt.newstaff_form', {'staff': staff, })
