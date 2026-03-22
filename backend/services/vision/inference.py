import os
import joblib
import numpy as np

class ImageInference:
    def __init__(self, model_dir):
        self.model_dir = model_dir
        self.clf = None
        self.classes = None
        self.mobilenet = None
        self._load_models()

    def _load_models(self):
        try:
            self.clf = joblib.load(os.path.join(self.model_dir, 'classifier.joblib'))
            self.classes = joblib.load(os.path.join(self.model_dir, 'classes.joblib'))
        except FileNotFoundError:
            pass

    def _load_extractor(self):
        from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
        from tensorflow.keras.preprocessing import image
        self.preprocess_input = preprocess_input
        self.image = image
        self.mobilenet = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

    def predict(self, img_path):
        if not self.clf:
            return {"error": "Model not trained yet."}
            
        if not self.mobilenet:
            self._load_extractor()

        # Extract features
        img = self.image.load_img(img_path, target_size=(224, 224))
        x = self.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = self.preprocess_input(x)
        features = self.mobilenet.predict(x, verbose=0)
        
        # Predict using SVM
        proba = self.clf.predict_proba(features)[0]
        
        predictions = []
        for i, class_name in enumerate(self.clf.classes_):
            predictions.append({
                "class": class_name,
                "confidence": float(proba[i])
            })
            
        # Sort by confidence
        predictions.sort(key=lambda x: x['confidence'], reverse=True)
        return predictions
