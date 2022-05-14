# -*- coding: utf-8 -*-
{
    'name': "Hrms",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "HRIT",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','resource'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/menu.xml',
        'views/bonus.xml',
        'views/kontrak.xml',
        'views/slip_gaji.xml',
        'views/hrms_payroll_component.xml',
        'views/hrms_master_salary.xml',
        'views/mesin.xml',
        'views/validation_attendance.xml',
        'views/jam_kerja.xml',
        'views/shift.xml',
        'views/group.xml',
        'views/sp.xml',
        'views/Schedule.xml',
        'views/departement.xml',
        'views/tax.xml',
        'views/jht.xml',
        'views/attendance.xml',
        'views/pp.xml',
        'views/sp.xml',
        'views/pph21.xml',
        'views/cal_interen.xml',
        'views/cal_nasional.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images' : ['static/description/icon.png']
}
