import os
import uuid
import logging
from .vision.trainer import ImageTrainer
from .vision.inference import ImageInference

logger = logging.getLogger(__name__)

class ImageService:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_base_dir = os.path.join(self.base_dir, '..', 'models', 'vision')
        self.dataset_base_dir = os.path.join(self.base_dir, '..', 'data', 'images')
        
    def _get_model_dir(self, dataset_id):
        return os.path.join(self.model_base_dir, str(dataset_id))
        
    def _get_dataset_dir(self, dataset_id):
        return os.path.join(self.dataset_base_dir, str(dataset_id))

    def train_model(self, dataset_id):
        if not dataset_id:
            raise ValueError("dataset_id is required")
            
        job_id = str(uuid.uuid4())
        logger.info(f"Image training starting for dataset {dataset_id}, job {job_id}")
        
        dataset_dir = self._get_dataset_dir(dataset_id)
        model_dir = self._get_model_dir(dataset_id)
        
        trainer = ImageTrainer(dataset_dir, model_dir)
        num_images, num_classes = trainer.train()
        
        logger.info(f"Image training job {job_id} finished. Images: {num_images}, Classes: {num_classes}")
        return job_id

    def predict(self, dataset_id, filepath):
        logger.info(f"Running image inference on {filepath} for dataset {dataset_id}")
        
        model_dir = self._get_model_dir(dataset_id)
        inference = ImageInference(model_dir)
        
        results = inference.predict(filepath)
        return results
