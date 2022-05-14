
from ast import Store
from odoo import api ,fields , models
class shift_kerja(models.Model):
    _name           = 'hrms.shift'
    _description    = 'hrms.shift'


    nama            = fields.Char(string="Nama Shift")
    keterangan      = fields.Char(string="Keterangan")
    description     = fields.Char(string="Description")
    
    workingdays_ids = fields.Many2many(     
        comodel_name='hrms.jam_kerja',
        string      ='Jam Kerja'
        )
    total_day    =  fields.Integer(string="Jumlah Hari Kerja",compute='_cek_count_shift',Store=True)


    @api.depends('workingdays_ids')
    def _cek_count_shift(self):
        self.total_day  =len(self.workingdays_ids)
