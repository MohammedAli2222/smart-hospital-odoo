from odoo import models, fields

class HrApplicantInherit(models.Model):

    _inherit = 'hr.applicant'

    medical_license_number = fields.Char(string='Medical License Number')
    
    license_expiry_date = fields.Date(string='License Expiry Date')