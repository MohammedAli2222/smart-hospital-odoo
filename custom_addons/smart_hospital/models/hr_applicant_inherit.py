# -*- coding: utf-8 -*-
from odoo import models, fields

class HrApplicantInherit(models.Model):
    # توريث النموذج الأساسي لطلبات التوظيف في أودو
    _inherit = 'hr.applicant'

    # إضافة حقل رقم الرخصة الطبية (نوع نصي)
    medical_license_number = fields.Char(string='Medical License Number')
    
    # إضافة حقل تاريخ انتهاء الرخصة الطبية (نوع تاريخ)
    license_expiry_date = fields.Date(string='License Expiry Date')