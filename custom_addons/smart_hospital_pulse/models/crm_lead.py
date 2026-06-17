from odoo import models, fields, api

class CrmLead(models.Model):

    _inherit = 'crm.lead'

    patient_heart_rate = fields.Integer(string="Patient Heart Rate")
    
    is_critical_iot_alert = fields.Boolean(string="Critical IoT Alert", default=False)

    def write(self, vals):

        new_vals = vals.copy()
        
        records_to_alert = []
        
        if 'patient_heart_rate' in new_vals:
            
            try:
                hr = int(new_vals.get('patient_heart_rate') or 0)
                is_now_critical = hr < 40 or hr > 140
                
                if is_now_critical:
                    new_vals['is_critical_iot_alert'] = True
                    new_vals['priority'] = '3'
                    
                    for record in self:
                        if not record.is_critical_iot_alert:
                            records_to_alert.append(record)
                else:
                    new_vals['is_critical_iot_alert'] = False
                    
            except (ValueError, TypeError):
                new_vals['is_critical_iot_alert'] = False
                
        res = super(CrmLead, self).write(new_vals)
        
        for record in records_to_alert:
            record.message_post(body="SYSTEM OVERRIDE: CRITICAL VITALS DETECTED.")
                
        return res