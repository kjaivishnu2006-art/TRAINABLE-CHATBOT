from flask import Blueprint, request, jsonify, current_app
import logging
import os
from services.audio_service import AudioService
from werkzeug.utils import secure_filename

audio_bp = Blueprint('audio_bp', __name__)
logger = logging.getLogger(__name__)
audio_service = AudioService()

@audio_bp.route('/upload', methods=['POST'])
def upload_audio():
    """Uploads a WAV audio file to the structured dataset folder."""
    dataset_id = request.form.get('dataset_id')
    class_name = request.form.get('class_name')
    
    if not dataset_id or not class_name:
        return jsonify({'error': 'dataset_id and class_name are required in form data'}), 400
        
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
        
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
        
    try:
        filename = secure_filename(file.filename)
        # Structure: root/data/audio/<dataset_id>/<class_name>/<filename>
        target_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], '..', 'data', 'audio', dataset_id, class_name)
        os.makedirs(target_dir, exist_ok=True)
        
        filepath = os.path.join(target_dir, filename)
        file.save(filepath)
        return jsonify({'message': 'Audio uploaded successfully', 'path': filepath}), 201
    except Exception as e:
        logger.error(f"Error in upload_audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

@audio_bp.route('/train', methods=['POST'])
def train_audio():
    logger.info("Initiating audio training...")
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        if not dataset_id:
            return jsonify({'error': 'dataset_id is required JSON param'}), 400
            
        job_id = audio_service.train_model(dataset_id)
        return jsonify({'message': 'Audio training completed', 'job_id': job_id}), 200
    except Exception as e:
        logger.error(f"Error in train_audio: {str(e)}")
        return jsonify({'error': str(e)}), 500

@audio_bp.route('/predict', methods=['POST'])
def predict_audio():
    dataset_id = request.form.get('dataset_id')
    if not dataset_id:
        return jsonify({'error': 'dataset_id is required for prediction context'}), 400
        
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
        
    file = request.files['audio']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
        
    try:
        filename = secure_filename(file.filename)
        temp_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'temp_predict_audio')
        os.makedirs(temp_dir, exist_ok=True)
        
        filepath = os.path.join(temp_dir, filename)
        file.save(filepath)
        
        predictions = audio_service.predict(dataset_id, filepath)
        
        if os.path.exists(filepath):
            os.remove(filepath)
            
        return jsonify({'predictions': predictions}), 200
    except Exception as e:
        logger.error(f"Error in predict_audio: {str(e)}")
        return jsonify({'error': str(e)}), 500
