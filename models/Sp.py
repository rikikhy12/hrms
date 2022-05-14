from odoo import api , fields , models

class hrms_master_sp(models.Model):
    _name         = 'hrms.master_sp'
    _description  = 'hrms.master_sp'


    name            =fields.Char(string='Nama Sp')
    description     =fields.Char(string='Description')
    is_active       =fields.Boolean()


class hrms_sp_employee(models.Model):
    _name ='hrms.sp_employee'
    _description  = 'hrms.sp_employee'

    employee_id = fields.Many2one(
        string='Karyawan',
        comodel_name='hr.employee',
    )

    status_sp = fields.Many2one(
        string='Status Sp',
        comodel_name='hrms.master_sp',
    )

    tanggal_awal = fields.Date(
        string='Tanggal Awal SP',
        default=fields.Date.context_today,
    )
    tanggal_akhir = fields.Date(
        string='Tanggal Akhir SP',
        default=fields.Date.context_today,
    )
    tanggal_terbit = fields.Date(
        string='Tanggal Terbit SP',
        default=fields.Date.context_today,
    )
     
    pelanggaran = fields.Text(
        string='pelanggaran',
    )


    
    
    

    
