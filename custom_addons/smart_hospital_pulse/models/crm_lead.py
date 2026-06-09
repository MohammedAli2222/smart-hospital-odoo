from odoo import models, fields, api

class CrmLead(models.Model):
    # وراثة نموذج التذاكر الطبية لتوسيع خصائصه
    _inherit = 'crm.lead'

    # تعريف حقل معدل نبضات القلب للمريض كعدد صحيح
    patient_heart_rate = fields.Integer(string="Patient Heart Rate")
    
    # تعريف حقل التنبيه الحرج لحالة إنترنت الأشياء، القيمة الافتراضية هي خطأ
    is_critical_iot_alert = fields.Boolean(string="Critical IoT Alert", default=False)

    # تجاوز الدالة الأساسية لحفظ البيانات لتطبيق منطق التنبيه التلقائي بأمان
    def write(self, vals):
        # التحقق مما إذا كان تحديث البيانات يحتوي على معدل نبضات القلب
        if 'patient_heart_rate' in vals:
            hr = vals.get('patient_heart_rate')
            
            # تطبيق شرط الخطر: النبض أقل من 40 أو أعلى من 140
            if hr < 40 or hr > 140:
                # تحديث حالة التنبيه والأولوية إلى 3 نجوم قبل الحفظ في قاعدة البيانات
                vals['is_critical_iot_alert'] = True
                vals['priority'] = '3'
                
        # استدعاء الدالة الأصلية باستخدام super للحفاظ على سلامة النظام الأساسي وتجنب الأخطاء الفادحة
        res = super(CrmLead, self).write(vals)
        
        # إرسال رسالة تحذيرية عالية الأهمية في نظام المحادثات بعد نجاح الحفظ
        if 'patient_heart_rate' in vals:
            hr = vals.get('patient_heart_rate')
            if hr < 40 or hr > 140:
                for record in self:
                    record.message_post(body="SYSTEM OVERRIDE: CRITICAL VITALS DETECTED.")
                    
        return res