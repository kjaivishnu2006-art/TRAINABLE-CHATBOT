import os
import joblib
import random
from sklearn.metrics.pairwise import cosine_similarity
from .preprocessing import clean_text

class ChatbotInference:
    def __init__(self, model_dir):
        self.model_dir = model_dir
        self._load_models()
        
    def _load_models(self):
        try:
            self.vectorizer = joblib.load(os.path.join(self.model_dir, 'vectorizer.joblib'))
            self.tfidf_matrix = joblib.load(os.path.join(self.model_dir, 'tfidf_matrix.joblib'))
            self.tags = joblib.load(os.path.join(self.model_dir, 'tags.joblib'))
            self.intents_data = joblib.load(os.path.join(self.model_dir, 'intents_data.joblib'))
        except FileNotFoundError:
            self.vectorizer = None
            
    def predict(self, query: str, threshold=0.1) -> str:
        if not self.vectorizer:
            return "Model not trained yet. Please trigger training first by sending a POST to /api/v1/text/train."
            
        query_vec = self.vectorizer.transform([clean_text(query)])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        
        best_match_idx = similarities.argmax()
        max_sim = similarities[best_match_idx]
        
        if max_sim < threshold:
            return "I'm not sure I understand. Could you rephrase that?"
            
        best_tag = self.tags[best_match_idx]
        
        # Look up the responses for the best tag
        for intent in self.intents_data.get('intents', []):
            if intent['tag'] == best_tag:
                return random.choice(intent['responses'])
                
        return "I don't have a specific response for that."
