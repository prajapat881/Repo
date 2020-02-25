{
    'name': "Bank Management App",
    'author': 'xyz',
    'sequence   ': 10,
    'installable': True,
    'auto_install': False,
    'version': '1.1',
    'summary': 'Bank App',
    'depends': ['base', 'website'],
    'data': ['views/bank_info_view.xml',
             'views/customer_info_view.xml',
             'views/staff_info_view.xml',
             'views/new_customer_form_view.xml',
             'views/new_staff_form_view.xml',
             'views/website_menu_view.xml',
             'report/menu_report_view.xml',
             'report/bank_report_view.xml', ],

    # 'demo': ['data/customer_info_demo.xml',
    #          'data/bank_info_demo.xml',
    #          'data/staff_info_demo.xml'],

    'demo': [],
    'category': 'Hidden',
    'description': 'TEST',
    'images': ['static/description/icon.png']
}
# -*- coding: utf-8 -*-
