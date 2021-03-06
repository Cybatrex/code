# -*- coding: utf-8 -*-
{
    'name': "mgm_sales_dashboard",

    'summary': """
        Modifier sales dashboard""",

    'description': """
        Long description of module's purpose
    """,

    'author': "HashMicro /Luc",
    'website': "http://www.hashmicro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sales_team','mgm_sales_contract','mgm_sales_bar_chart'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        'views/sales_dashboard.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
