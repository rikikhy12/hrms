
from ast import Store
import datetime
from odoo  import api ,fields , models 
class jam_kerja(models.Model):
    _name        = 'hrms.jam_kerja'
    _description = 'hrms.jam_kerja'


    nama                = fields.Char(string="Nama")
    jam_in              = fields.Char(string="Jam in",default='00.00')
    jam_out             = fields.Char(string="Jam Out",default='00.00')
    toleransi_in        = fields.Char(string="Toleransi In")
    toleransi_out       = fields.Char(string="Toleransi Out")
    totaljamkerja       = fields.Char(string="Total jam Kerja",compute='_def_count_jam',Store=True)
    days                = fields.Selection([
                        ('Monday', 'Monday'),
                        ('Tuesday', 'Tuesday'),
                        ('Wednesday', 'Wednesday'),
                        ('Thursday', 'Thursday'),
                        ('Friday', 'Friday'),
                        ('Saturday', 'Saturday'),
                        ('Sunday', 'Sunday')
                        ], 'Day of Week', required=True, index=True, default='Monday')


    @api.depends('jam_in','jam_out')
    def _def_count_jam(self):
                #jamin
     
                jamin   = self.jam_in
                timein  =str(jamin)
                timeinz =timein.split(".")
                jamins  =float(timeinz[0])
                if len(timeinz)>1 :
                    menitin =timeinz[1]
                elif len(timeinz)==1 :
                    menitin ='00'
                
                menitinx=menitin[0:2]
                if len(menitinx) > 1 :
                    menitinx    =round(float((float(menitinx)*6)/10))
                elif len(menitinx) == 1 :
                    menitinx    = round(float(float(menitinx)*6))

                jamout  = self.jam_out
                timeout =str(jamout)
                timeoutz=timeout.split(".")
                jamouts  =float(timeoutz[0])
                if len(timeoutz)>1 :
                    menitout =timeoutz[1]
                elif len(timeoutz)==1 :
                    menitout ='00'
                
                menitoutx=menitout[0:2]
                if len(menitoutx) > 1 :
                    menitoutx    =round(float((float(menitoutx)*6)/10))
                elif len(menitoutx) == 1 :
                    menitoutx    = round(float(float(menitoutx)*6))
              
              
                
                time_1 = datetime.timedelta(hours= round(jamins) , minutes=menitinx)
                time_2 = datetime.timedelta(hours= round(jamouts), minutes=menitoutx)
                self.totaljamkerja=time_2-time_1
          


