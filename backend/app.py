import os
import logging
from flask import Flask, jsonify
from config import config
from routes.text_routes import text_bp
from routes.image_routes import image_bp
from routes.audio_routes import audio_bp

# Configure global logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def dict_error_response(app):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not Found', 'message': str(error)}), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({'error': 'Internal Server Error', 'message': str(error)}), 500

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Ensure upload directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register error handlers
    dict_error_response(app)

    # Register Blueprints
    app.register_blueprint(text_bp, url_prefix='/api/v1/text')
    app.register_blueprint(image_bp, url_prefix='/api/v1/image')
    app.register_blueprint(audio_bp, url_prefix='/api/v1/audio')

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy", "service": "VYOMA AI Backend"})

    return app

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_ENV', 'default'))
    app.run(host='0.0.0.0', port=5000)
