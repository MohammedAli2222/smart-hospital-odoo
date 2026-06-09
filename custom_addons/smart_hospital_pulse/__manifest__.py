{
    'name': 'Smart Hospital Pulse (IoT Triage)',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Automated triage engine using simulated IoT vitals.',
    # الاعتماد على تطبيق CRM الأساسي لأننا نورث منه
    'depends': ['crm'],
   'data': [
        'views/crm_triage_views.xml',
    ],
    'installable': True,
    'application': False,
}