from odoo import api , fields , models

class hrms_master_sp(models.Model):
    _name         = 'hrms.master_sp'
    _description  = 'hrms.master_sp'


    name            =fields.Char(string='Nama Sp')
    description     =fields.Char(string='Description')
    is_active       =fields.Boolean()


class hrms_sp_employee(models.Model):

    _name        = 'hrms.sp_employee'
    _description = 'hrms.sp_employee'


    employee_id     = fields.Many2one(comodel_name='hr.employee',string='Karyawan')
    jenis_sp        = fields.Many2one(comodel_name='hrms.master_sp',string='Jenis pelanggaran')
    tgl_awal_sp     = fields.Date(string='Tanggal awal sp')
    tgl_akhir_sp    = fields.Date(string='Tanggal Akhir sp')
    tgl_terbit_sp   = fields.Date(string='Tanggal Terbit sp')
    pelanggaran     = fields.Text(string='Pelanggaran')
    potongan        = fields.Float(string='Potongan (%)', default=100.0)






    
