from flask import Blueprint, request, jsonify, current_app
import logging
import os
from services.image_service import ImageService
from werkzeug.utils import secure_filename

image_bp = Blueprint('image_bp', __name__)
logger = logging.getLogger(__name__)
image_service = ImageService()

@image_bp.route('/upload', methods=['POST'])
def upload_image():
    """Uploads an image to the structured dataset folder."""
    dataset_id = request.form.get('dataset_id')
    class_name = request.form.get('class_name')
    
    if not dataset_id or not class_name:
        return jsonify({'error': 'dataset_id and class_name are required in form data'}), 400
        
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
        
    try:
        filename = secure_filename(file.filename)
        # Structure: root/data/images/<dataset_id>/<class_name>/<filename>
        target_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], '..', 'data', 'images', dataset_id, class_name)
        os.makedirs(target_dir, exist_ok=True)
        
        filepath = os.path.join(target_dir, filename)
        file.save(filepath)
        return jsonify({'message': 'Image uploaded successfully', 'path': filepath}), 201
    except Exception as e:
        logger.error(f"Error in upload_image: {str(e)}")
        return jsonify({'error': str(e)}), 500

@image_bp.route('/train', methods=['POST'])
def train_image():
    logger.info("Initiating image training...")
    try:
        data = request.get_json()
        dataset_id = data.get('dataset_id')
        if not dataset_id:
            return jsonify({'error': 'dataset_id is required JSON param'}), 400
            
        job_id = image_service.train_model(dataset_id)
        return jsonify({'message': 'Image training completed', 'job_id': job_id}), 200
    except Exception as e:
        logger.error(f"Error in train_image: {str(e)}")
        return jsonify({'error': str(e)}), 500

@image_bp.route('/predict', methods=['POST'])
def predict_image():
    dataset_id = request.form.get('dataset_id')
    if not dataset_id:
        return jsonify({'error': 'dataset_id is required for prediction context'}), 400
        
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
        
    try:
        filename = secure_filename(file.filename)
        temp_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'temp_predict')
        os.makedirs(temp_dir, exist_ok=True)
        
        filepath = os.path.join(temp_dir, filename)
        file.save(filepath)
        
        predictions = image_service.predict(dataset_id, filepath)
        
        if os.path.exists(filepath):
            os.remove(filepath)
            
        return jsonify({'predictions': predictions}), 200
    except Exception as e:
        logger.error(f"Error in predict_image: {str(e)}")
        return jsonify({'error': str(e)}), 500
