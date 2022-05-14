from odoo import fields , models , api 

class Attendance_m(models.Model):
    
    _inherit        = 'hr.attendance'
    status_absen   = fields.Selection([('0', 'Hadir'),('1', 'Sakit'),('2', 'Izin'),('3', 'Alpha')])
    