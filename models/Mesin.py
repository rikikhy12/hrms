
from odoo import api , fields ,models 

class Mesin(models.Model):
    _name           ='hrms.mesin' 
    _description    ='hrms.mesin' 
    
    nama        =fields.Char(string='Nama Mesin')
    ip_address  =fields.Char(string='Ip Address')