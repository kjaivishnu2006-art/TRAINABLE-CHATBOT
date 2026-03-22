from flask import Blueprint, request, jsonify
import logging
from services.text_service import TextService

text_bp = Blueprint('text_bp', __name__)
logger = logging.getLogger(__name__)
text_service = TextService()

@text_bp.route('/train', methods=['POST'])
def train_text():
    try:
        data = request.get_json()
        if not data or 'dataset' not in data:
            return jsonify({'error': 'Invalid payload, missing dataset'}), 400
            
        logger.info("Initiating text training...")
        job_id = text_service.train_model(data['dataset'])
        return jsonify({'message': 'Training started', 'job_id': job_id}), 202
    except Exception as e:
        logger.error(f"Error in train_text: {str(e)}")
        return jsonify({'error': str(e)}), 500

@text_bp.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid payload, missing message'}), 400
            
        response = text_service.predict(data['message'])
        return jsonify({'response': response}), 200
    except Exception as e:
        logger.error(f"Error in chat prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500
