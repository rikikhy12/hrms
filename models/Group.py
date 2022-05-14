from ast import Store
from odoo.exceptions import ValidationError
from odoo import fields ,api , models
class ModelName(models.Model):
    _name           = 'hrms.group'
    _description    = 'hrms.group'
    
    name             =fields.Char(string='Nama Group')
    periode          =fields.Date(string='Tanggal')
    sd               =fields.Date(string='Sampai Dengan')
    active           =fields.Boolean(string="Active", default=True)
    shift_ids        =fields.Many2many(comodel_name='hrms.shift',string='Pilih Shift')
    departements_id  =fields.Many2many(comodel_name='hrms.departement',string='Departement')
    totalshift       =fields.Integer(string='Jumlah shift',compute='_def_count_shift',Store=True)

    @api.onchange('shift_ids','name')
    def _cekshifid(self):
        if self.shift_ids and len(self.shift_ids)== 0 :
         return {
                    'warning': {
                    'title'  : "Bad Value",
                    'message': "Master Shift tidak boleh kosong",
                }
            }
        elif self.shift_ids and len(self.shift_ids)>1 :
             return {
                    'warning': {
                    'title'  : "Bad Value",
                    'message': "Hanya di perbolehkan memilih 1 shift",
                }
            }
    
   

    @api.depends('shift_ids')
    def _def_count_shift(self):
        self.totalshift=len(self.shift_ids)

    @api.constrains('totalshift','shift_ids')
    def _check_attendees(self):
        for rec in self:
            if rec.totalshift > 1:
                raise ValidationError("Master shift tidak boleh lebih dari  1")
            if rec.totalshift == 0:
                raise ValidationError("Master shift tidak boleh boleh kosong")