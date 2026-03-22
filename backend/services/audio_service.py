import os
import uuid
import logging
from .audio_ml.trainer import AudioTrainer
from .audio_ml.inference import AudioInference

logger = logging.getLogger(__name__)

class AudioService:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_base_dir = os.path.join(self.base_dir, '..', 'models', 'audio')
        self.dataset_base_dir = os.path.join(self.base_dir, '..', 'data', 'audio')
        
    def _get_model_dir(self, dataset_id):
        return os.path.join(self.model_base_dir, str(dataset_id))
        
    def _get_dataset_dir(self, dataset_id):
        return os.path.join(self.dataset_base_dir, str(dataset_id))

    def train_model(self, dataset_id):
        if not dataset_id:
            raise ValueError("dataset_id is required")
            
        job_id = str(uuid.uuid4())
        logger.info(f"Audio training starting for dataset {dataset_id}, job {job_id}")
        
        dataset_dir = self._get_dataset_dir(dataset_id)
        model_dir = self._get_model_dir(dataset_id)
        
        trainer = AudioTrainer(dataset_dir, model_dir)
        num_samples, num_classes = trainer.train()
        
        logger.info(f"Audio training job {job_id} finished. Samples: {num_samples}, Classes: {num_classes}")
        return job_id

    def predict(self, dataset_id, filepath):
        logger.info(f"Running audio inference on {filepath} for dataset {dataset_id}")
        
        model_dir = self._get_model_dir(dataset_id)
        inference = AudioInference(model_dir)
        
        results = inference.predict(filepath)
        return results
