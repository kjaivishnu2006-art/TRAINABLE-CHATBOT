import os
import faiss
import pickle
import random
from sentence_transformers import SentenceTransformer

class ChatbotInference:
    def __init__(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        index_path = os.path.join(self.base_dir, "chatbot.faiss")
        meta_path = os.path.join(self.base_dir, "chatbot.pkl")
        
        if not os.path.exists(index_path) or not os.path.exists(meta_path):
            raise FileNotFoundError("FAISS index missing. Run ai-model/train.py first.")
            
        self.index = faiss.read_index(index_path)
        with open(meta_path, "rb") as f:
            self.metadata = pickle.load(f)

    def predict(self, query: str) -> str:
        query_embedding = self.model.encode([query]).astype('float32')
        distances, indices = self.index.search(query_embedding, 1)
        
        best_distance = distances[0][0]
        if best_distance > 1.4: 
            return "I'm sorry, I'm not trained to understand that yet."
            
        matched_intent = self.metadata[indices[0][0]]
        return random.choice(matched_intent["responses"])
