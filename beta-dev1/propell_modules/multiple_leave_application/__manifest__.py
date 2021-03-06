# -*- coding: utf-8 -*-
{
    'name': "multiple_leave_application",

    'description': """
        Multiple leave application
    """,

    'author': "HashMicro/Vu",
    'website': "http://www.hashmicro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_holidays_multiple_view.xml',
        'views/hr_holidays_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}