from ast import Store
from odoo import api ,fields , models
class Departement(models.Model):
    _name                   ='hrms.departement'
    _description            ='hrms.departement'

    name                    =fields.Char(string='Nama Departement')
    parent_departement      =fields.Many2one(comodel_name='hr.department',string='Pilih Parent Departement')
    employes_id             =fields.Many2many(comodel_name='hr.employee' ,string='Pilih Kariawan')
    manager                 =fields.Char(string='Manager')
    totalemployes           =fields.Float(compute='_def_hitung_kariawan',string='Total Kariawan', Store=True)


   
    @api.onchange('employes_id','totalemployes')
    def _def_hitung_kariawan(self):
        if self.employes_id :
         self.totalemployes =  len(self.employes_id)
    