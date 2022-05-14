
from datetime import datetime
from odoo import api ,fields,models 

class validasi_absen (models.Model):
     #_logger            = logging.getLogger(__name__)
     _name              ='hrms.validasi_attendance'
     _description       ='hrms.validasi_attendance'

     employee_id        = fields.Many2one(comodel_name='hr.employee',string ='Nama Kariawan')
     date               = fields.Date(string='Tanggal')
     check_in           = fields.Datetime(string='Check in')
     check_out          = fields.Datetime(string='Check Out')
     status_absen       = fields.Selection([('0', 'Hadir'),('1', 'Sakit'),('2', 'Izin'),('3', 'Alpha')])
     postingabsen       = fields.Selection([('0','Belum Posting'),('1','Posting')])
     group_id           = fields.Many2one(comodel_name='hrms.group', string='Group_id')
     
     @api.model
     def create(self,values):
        # your logic goes here
        override_create = super(validasi_absen,self).create(values)
        return override_create


     def funct_to_approve(self):
        for rec in self :
           workedhours =0
           if rec.check_in  == False :
                checkin="1990-02-21 00:00:00"
           elif rec.check_in != False :
                checkin=rec.check_in
                
           if rec.check_out  == False :
                check_out="1990-02-21 00:00:00"
           elif rec.check_out != False :
                check_out=rec.check_out

           if rec.check_in == True and rec.check_out == True :
                datechekin = datetime.datetime(int(rec.check_in[0:4]), 
                              int(rec.check_in[5:7]), int(rec.check_in[8:10]),
                              int(rec.check_in[11:13]),int(rec.check_in[14:16]),
                              int(rec.check_in[17:19])
                              )
                datechekout = datetime.datetime(int(rec.check_out[0:4]), 
                              int(rec.check_out[5:7]), int(rec.check_out[8:10]),
                              int(rec.check_out[11:13]),int(rec.check_out[14:16]),
                              int(rec.check_out[17:19])
                              )
                time_diff     = datechekout - datechekin
                total_seconds =time_diff.total_seconds()
                workedhours   =total_seconds/(60*60)
                

           employez_id   = rec.employee_id.id   
           rec.env['hr.attendance'].create({
                         'employee_id' :employez_id,
                         'check_in'    :checkin,
                         'check_out'   :check_out,
                         'status_absen':rec.status_absen,
                         'worked_hours':workedhours
           })

           ##Update Posting Absen
           query = """update hrms_validasi_attendance set postingabsen='1' 
           where id='""" +str(rec.id)+ """' """
           rec.env.cr.execute(query)

     def defhadir(self):
          query = """update hrms_validasi_attendance set status_absen='0' 
           where id='""" +str(self.id)+ """' """
          self.env.cr.execute(query)

     def defsakit(self):
          query = """update hrms_validasi_attendance set status_absen='1' 
           where id='""" +str(self.id)+ """' """
          self.env.cr.execute(query)

     def defizin(self):
          query = """update hrms_validasi_attendance set status_absen='2' 
           where id='""" +str(self.id)+ """' """
          self.env.cr.execute(query)

     def defalpha(self):
          query = """update hrms_validasi_attendance set status_absen='3' 
           where id='""" +str(self.id)+ """' """
          self.env.cr.execute(query)

    
