
from unicodedata import name
from odoo.exceptions import UserError, ValidationError
from odoo import api ,fields ,models
class Payroll(models.Model):
    _name = 'hrms.payroll'
    _description ='hrms.payroll'

    #name         = fields.Char(String="Name")
    employee_id  = fields.Many2one(
        comodel_name='hr.employee',
        string      ='Nama Kariawan',
        )
    name = fields.Char(string='Payslip Name')
    noslip         = fields.Char(String="No slip")
    date_from      = fields.Date(String="Periode Gaji")
    ref            = fields.Char(String="Referensi")
    input_line_ids = fields.One2many(comodel_name='hrms.payroll.input_lines',inverse_name='payroll_id',String='input Lain-lain')
    workeddayline  = fields.One2many(comodel_name='hrms.payroll.working_days',inverse_name='payroll_id',String="Hari Kerja")
    date_to        = fields.Date(String="")
    contract_id    =  fields.Many2one(
        comodel_name='hr.contract',
        string      ='Nama Kariawan',
        )
    line_ids      =  fields.One2many(comodel_name='hrms.payroll.line_componen',inverse_name='payroll_id',String='Perhitungan gaji')   
    @api.depends('workeddayline')
    def isi(self):
        if self.workingdayline:
            code = self.workeddayline.code
            name = self.workeddayline.name

class worked_days(models.Model):
    _name        ='hrms.payroll.working_days'
    _description ='hrms.paryoll.working_days'

    payroll_id   = fields.Many2one(
                    string='payroll id',
                    comodel_name='hrms.payroll',
                    
    )
   
    code         = fields.Char(
        string   ='Kode',
    )
    sequence        = fields.Integer(required=True, index=True, default=10)
    name            = fields.Char(string='Description', required=True)
    number_of_days  = fields.Float(string='Number of Days')
    number_of_hours = fields.Float(string='Number of Hours')
    
class inputlines(models.Model):
    _name           ='hrms.payroll.input_lines'
    _description    ='hrms.payroll.input_lines'
    _order          ='payroll_id, sequence'

    payroll_id      =fields.Many2one(comodel_name='hrms.payroll', string='Pay Slip', required=True, ondelete='cascade', index=True)
    name            =fields.Char(String='description',required=True)
    code            =fields.Char(String='code',required=True)
    sequence        =fields.Integer(required=True, index=True, default=10)
    amount          =fields.Float(help="It is used in computation. For e.g. A rule for sales having "
                               "1% commission of basic salary for per product can defined in expression "
                               "like result = inputs.SALEURO.amount * contract.wage*0.01.")
    contract_id     = fields.Many2one('hr.contract', string='Contract', required=True,
        help="The contract for which applied this input")
        
class rulePayroll(models.Model):
      _name         ='hrms.payroll.line_componen'
      _description  ='hrms.payroll.line_componen'
      _order        ='payroll_id'


      payroll_id    = fields.Many2one('hrms.payroll','Payroll id') 
      name          = fields.Char('Description') 
      code          = fields.Char('Kode')
      #employee_id   = fields.Many2one('hr.employee', string='Employee', required=True)
      #contract_id   = fields.Many2one('hr.contract', string='Contract', required=True, index=True)
      component     = fields.Many2one('hrms.payroll_component', string='Componen', required=True)
      rate          = fields.Float(string='Rate (%)', default=100.0)
      amount        = fields.Float()
      quantity      = fields.Float(default=1.0)
      total         = fields.Float(compute='_compute_total', string='Total')

      @api.depends('quantity', 'amount', 'rate')
      def _compute_total(self):
        for line in self:
            line.total = float(line.quantity) * line.amount * line.rate / 100
            
class PayrollComponent(models.Model):
      _name           ='hrms.payroll_component'
      _description    ='hrms.payroll_component'


      name            =fields.Char(string="name")
      description     =fields.Char(string="description")
      component_id    =fields.Many2one(comodel_name='hrms.master_salary',String='Komponen id')
 
class hrms_masterSalary(models.Model):
     _name                   ='hrms.master_salary'
     _description            ='hrms.master_salary'

     name                    = fields.Char(
         string='Kode Referensi',
         required=True
     )
     employee_id            = fields.Many2one( 
         comodel_name='hr.employee',
         string='Kariawan'
                        
     )
     kontrak            = fields.Many2one( 
         comodel_name   ='hr.contract',
         string         ='Kontrak'
                        
     )
    
     componen_id     = fields.One2many(
         string      ='komponen',
         comodel_name='hrms.master_pay_line_component',
         inverse_name='com_id'
     )
     grandtotal   =fields.Float(string="Total Bruto")
      
     

     class MasterPaycomponent(models.Model):
         _name        = 'hrms.master_pay_line_component'
         _description = 'hrms.master_pay_line_component'

         
         name         =fields.Char(string='Name')
         description  =fields.Char(string='Description')
         amount       =fields.Float(string="Jumlah")
         total        =fields.Float(string="Total",compute='_compute_total')
         rate         =fields.Float(string='Rate (%)', default=100.0)
         quantity     =fields.Float(default=1.0,string='Kuantitas')
         componen_id  = fields.Many2one(
         string       ='komponen',
         comodel_name ='hrms.payroll_component'
       
         )

         
         com_id        =fields.Many2one(
             string      ='kom_id',
             comodel_name='hrms.master_salary'
         )
        
         @api.depends('quantity', 'amount', 'rate')
         def _compute_total(self):
            for line in self:
                line.total = float(line.quantity) * line.amount * line.rate / 100