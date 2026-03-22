import os
import glob
import numpy as np
import joblib
import logging

logger = logging.getLogger(__name__)

class AudioTrainer:
    def __init__(self, dataset_dir, model_dir):
        self.dataset_dir = dataset_dir
        self.model_dir = model_dir
        
    def extract_features(self, audio_path):
        import librosa
        # Load audio file (resample to 16kHz for consistency)
        y, sr = librosa.load(audio_path, sr=16000)
        
        # Extract MFCCs (Mel-frequency cepstral coefficients)
        # We take the mean across the time axis to get a 1D vector
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfccs_mean = np.mean(mfccs.T, axis=0)
        
        return mfccs_mean

    def train(self):
        from sklearn.neighbors import KNeighborsClassifier
        
        classes = [d for d in os.listdir(self.dataset_dir) if os.path.isdir(os.path.join(self.dataset_dir, d))]
        if len(classes) < 2:
            raise ValueError("Need at least 2 classes to train. Ensure structured folders exist.")
            
        features_list = []
        labels_list = []
        
        for idx, cls_name in enumerate(classes):
            cls_dir = os.path.join(self.dataset_dir, cls_name)
            audio_files = glob.glob(os.path.join(cls_dir, '*.wav'))
            
            for audio_path in audio_files:
                try:
                    feat = self.extract_features(audio_path)
                    features_list.append(feat)
                    labels_list.append(cls_name)
                except Exception as e:
                    logger.error(f"Error extracting features from {audio_path}: {e}")
                    
        if not features_list:
            raise ValueError("No valid .wav files found for training")
            
        X = np.array(features_list)
        y = np.array(labels_list)
        
        # Train lightweight K-Nearest Neighbors classifier
        clf = KNeighborsClassifier(n_neighbors=min(3, len(X)))
        clf.fit(X, y)
        
        # Save models
        os.makedirs(self.model_dir, exist_ok=True)
        joblib.dump(clf, os.path.join(self.model_dir, 'classifier.joblib'))
        joblib.dump(classes, os.path.join(self.model_dir, 'classes.joblib'))
        
        return len(X), len(classes)
