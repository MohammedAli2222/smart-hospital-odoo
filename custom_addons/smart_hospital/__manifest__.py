# -*- coding: utf-8 -*-
{
    'name': 'Smart Hospital ERP',
    'version': '1.0',
    'category': 'Healthcare/ERP',
    'summary': 'Integrated Smart Mobile Hospital ERP solution',
    'description': """
        Smart Hospital ERP System for managing mobile clinics and ambulance fleets.
    """,
    'author': 'Smart Hospital Team',
    'depends': [
        'base',
        'hr',
        'stock',
        'purchase',
        'maintenance',
        'account',
        'project',
        'crm',
        'calendar',
        'fleet',
        'product_expiry',

        'hr_recruitment',         
        'website_hr_recruitment', 
        'hr_skills' 
    ],
    'data': [
        'security/smart_hospital_groups.xml',
        'security/smart_hospital_rules.xml',
        'data/crm_triage_stages.xml',
        'data/crm_triage_records.xml',
        'data/crm_triage_activities.xml',
        'data/campaign_scheduling_records.xml',
        'data/logistics_infrastructure_records.xml',
        'data/supply_chain_records.xml',
        'views/hr_applicant_views.xml',
    ],  
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}