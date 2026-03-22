import os
import glob
import numpy as np
import joblib
import logging

logger = logging.getLogger(__name__)

class ImageTrainer:
    def __init__(self, dataset_dir, model_dir):
        self.dataset_dir = dataset_dir
        self.model_dir = model_dir
        
        # We lazy-load TensorFlow to avoid slowing down startup
        self.mobilenet = None 
        
    def _load_extractor(self):
        from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
        from tensorflow.keras.preprocessing import image
        self.preprocess_input = preprocess_input
        self.image = image
        self.mobilenet = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

    def extract_features(self, img_path):
        img = self.image.load_img(img_path, target_size=(224, 224))
        x = self.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = self.preprocess_input(x)
        features = self.mobilenet.predict(x, verbose=0)
        return features[0]

    def train(self):
        if not self.mobilenet:
            self._load_extractor()
            
        from sklearn.svm import SVC
        
        classes = [d for d in os.listdir(self.dataset_dir) if os.path.isdir(os.path.join(self.dataset_dir, d))]
        if len(classes) < 2:
            raise ValueError("Need at least 2 classes to train. Ensure structured folders exist.")
            
        features_list = []
        labels_list = []
        
        for idx, cls_name in enumerate(classes):
            cls_dir = os.path.join(self.dataset_dir, cls_name)
            images = glob.glob(os.path.join(cls_dir, '*.[jp][pn]*g')) # jpg, png, jpeg
            for img_path in images:
                try:
                    feat = self.extract_features(img_path)
                    features_list.append(feat)
                    labels_list.append(cls_name)
                except Exception as e:
                    logger.error(f"Error extracting features from {img_path}: {e}")
                    
        if not features_list:
            raise ValueError("No valid images found for training")
            
        X = np.array(features_list)
        y = np.array(labels_list)
        
        # Train lightweight classifier
        clf = SVC(kernel='linear', probability=True)
        clf.fit(X, y)
        
        # Save models
        os.makedirs(self.model_dir, exist_ok=True)
        joblib.dump(clf, os.path.join(self.model_dir, 'classifier.joblib'))
        joblib.dump(classes, os.path.join(self.model_dir, 'classes.joblib'))
        
        return len(X), len(classes)
