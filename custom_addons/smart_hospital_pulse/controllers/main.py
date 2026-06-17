import json
from odoo import http
from odoo.http import request, Response
import logging

_logger = logging.getLogger(__name__)

class IotVitalsController(http.Controller):
    
    @http.route('/api/hospital/vitals/update', type='http', auth='public', methods=['POST'], csrf=False)
    def update_patient_vitals(self, **kwargs):
        try:

            data = request.httprequest.data.decode('utf-8')
            payload = json.loads(data)
            
            ticket_id = payload.get('ticket_id')
            heart_rate = payload.get('heart_rate')

            if not ticket_id or heart_rate is None:
                return Response(json.dumps({'status': 'error', 'message': 'Missing ticket_id or heart_rate'}), status=400, content_type='application/json')

            ticket = request.env['crm.lead'].sudo().search([('id', '=', int(ticket_id))], limit=1)

            if not ticket:
                return Response(json.dumps({'status': 'error', 'message': 'Ticket not found'}), status=404, content_type='application/json')

            ticket.write({'patient_heart_rate': int(heart_rate)})

            return Response(json.dumps({
                'status': 'success',
                'message': 'Vitals updated successfully',
                'ticket_id': ticket.id,
                'new_heart_rate': heart_rate
            }), status=200, content_type='application/json')

        except Exception as e:
            _logger.error(f"IoT API Error: {str(e)}")
            return Response(json.dumps({'status': 'error', 'message': 'Internal Server Error', 'details': str(e)}), status=500, content_type='application/json')