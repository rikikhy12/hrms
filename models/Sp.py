from odoo import api , fields , models

class hrms_master_sp(models.Model):
    _name         = 'hrms.master_sp'
    _description  = 'hrms.master_sp'


    name            =fields.Char(string='Nama Sp')
    description     =fields.Char(string='Description')
    is_active       =fields.Boolean()



    
