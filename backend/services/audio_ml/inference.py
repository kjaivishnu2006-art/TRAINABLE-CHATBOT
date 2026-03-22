import os
import joblib
import numpy as np

class AudioInference:
    def __init__(self, model_dir):
        self.model_dir = model_dir
        self.clf = None
        self.classes = None
        self._load_models()

    def _load_models(self):
        try:
            self.clf = joblib.load(os.path.join(self.model_dir, 'classifier.joblib'))
            self.classes = joblib.load(os.path.join(self.model_dir, 'classes.joblib'))
        except FileNotFoundError:
            pass

    def predict(self, audio_path):
        import librosa
        if not self.clf:
            return {"error": "Model not trained yet."}
            
        try:
            y, sr = librosa.load(audio_path, sr=16000)
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
            features = np.mean(mfccs.T, axis=0)
        except Exception as e:
            return {"error": f"Failed to process audio: {str(e)}"}
        
        features = np.expand_dims(features, axis=0)
        
        # Predict using KNN probabilities
        proba = self.clf.predict_proba(features)[0]
        
        predictions = []
        for i, class_name in enumerate(self.clf.classes_):
            predictions.append({
                "class": class_name,
                "confidence": float(proba[i])
            })
            
        predictions.sort(key=lambda x: x['confidence'], reverse=True)
        return predictions
