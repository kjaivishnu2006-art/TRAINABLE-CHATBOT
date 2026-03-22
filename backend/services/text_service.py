import uuid
import logging
import os
from .chatbot.trainer import ChatbotTrainer
from .chatbot.inference import ChatbotInference

logger = logging.getLogger(__name__)

class TextService:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_dir = os.path.join(self.base_dir, '..', 'models', 'text_model')
        self.data_path = os.path.join(self.base_dir, '..', 'data', 'intents.json')
        
        # Load inference module lazily if model exists
        self.inference = ChatbotInference(self.model_dir)

    def train_model(self, dataset_payload=None):
        job_id = str(uuid.uuid4())
        logger.info(f"Text training started for job {job_id}")
        
        # If payload is provided, overwrite the intents.json First
        if dataset_payload:
            import json
            os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
            with open(self.data_path, 'w', encoding='utf-8') as f:
                json.dump(dataset_payload, f, indent=2)
                
        trainer = ChatbotTrainer(self.data_path, self.model_dir)
        num_patterns, num_tags = trainer.train()
        
        # Reload inference with new model
        self.inference = ChatbotInference(self.model_dir)
        
        logger.info(f"Training completed. Patterns: {num_patterns}, Tags: {num_tags}")
        return job_id

    def predict(self, message):
        logger.info(f"Processing chat message: {message}")
        response = self.inference.predict(message)
        return response
