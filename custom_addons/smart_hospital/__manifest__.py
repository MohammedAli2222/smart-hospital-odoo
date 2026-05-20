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
    ],
    'data': [
        'security/smart_hospital_groups.xml',
        'security/smart_hospital_rules.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}