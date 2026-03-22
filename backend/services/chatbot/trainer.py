import json
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from .preprocessing import clean_text

class ChatbotTrainer:
    def __init__(self, data_path, model_dir):
        self.data_path = data_path
        self.model_dir = model_dir
        self.vectorizer = TfidfVectorizer(preprocessor=clean_text)
        
    def train(self):
        """
        Reads intents.json, fits TF-IDF on all patterns, 
        and maps them to their respective tags.
        """
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Training data not found at {self.data_path}")
            
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        patterns = []
        tags = []
        
        for intent in data.get('intents', []):
            for pattern in intent.get('patterns', []):
                patterns.append(pattern)
                tags.append(intent['tag'])
                
        if not patterns:
            raise ValueError("No training patterns found.")
            
        # Fit vectorizer and transform patterns to TF-IDF matrix
        tfidf_matrix = self.vectorizer.fit_transform(patterns)
        
        # Save models and metadata
        os.makedirs(self.model_dir, exist_ok=True)
        joblib.dump(self.vectorizer, os.path.join(self.model_dir, 'vectorizer.joblib'))
        joblib.dump(tfidf_matrix, os.path.join(self.model_dir, 'tfidf_matrix.joblib'))
        joblib.dump(tags, os.path.join(self.model_dir, 'tags.joblib'))
        
        # Copy the JSON responses for inference lookup
        joblib.dump(data, os.path.join(self.model_dir, 'intents_data.joblib'))
        
        return len(patterns), len(set(tags))
