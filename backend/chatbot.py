import os
import json
import random
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class VyomaChatbotEngine:
    """
    Core AI Engine for Vyoma AI.
    Loads dataset patterns, vectorizes them using SentenceTransformers,
    and maps them to a FAISS index for high-speed semantic retrieval natively at runtime.
    """
    
    def __init__(self):
        # Define the exact path to our training dataset located in the ai-model directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.dataset_path = os.path.join(base_dir, 'ai-model', 'dataset.json')
        
        # Load the HuggingFace Model (MiniLM is highly optimized for performance & accuracy)
        print("Initializing SentenceTransformer (all-MiniLM-L6-v2) inference engine...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Internal state variables mapping the FAISS index strictly with our string answers
        import typing
        self.index: 'typing.Any' = None
        self.metadata = []
        
        self._build_index()

    def _build_index(self):
        """
        Reads the dataset, converts standard strings into massive mathematical 
        vector arrays, and generates a dynamic FAISS Flat-L2 structure in memory.
        """
        print(f"Loading conversational knowledge base from: {self.dataset_path}")
        if not os.path.exists(self.dataset_path):
            raise FileNotFoundError("dataset.json could not be localized on the server.")
            
        with open(self.dataset_path, 'r', encoding='utf-8') as f:
            dataset = json.load(f)

        corpus = []
        
        # Iterate over the JSON grouping to segregate trigger phrases from corresponding replies
        for intent in dataset.get('intents', []):
            for pattern in intent.get('patterns', []):
                corpus.append(pattern)
                self.metadata.append({
                    "tag": intent.get("tag", "unknown"),
                    "responses": intent.get("responses", ["I'm not quite sure how to respond."])
                })

        print(f"Vectorizing {len(corpus)} conversational patterns rapidly in memory...")
        # Calculate mathematical embedding vectors representing identical 384 dimensions
        embeddings = self.model.encode(corpus).astype('float32')
        
        # Boot FAISS L2 Search geometry structures
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)
        print("FAISS structural index bound! The Vyoma Chatbot Engine is completely online.")

    def get_response(self, query: str) -> str:
        """
        Takes a raw string query input from the user/frontend, vector-encodes it flawlessly,
        and asks FAISS mathematically which text intent is the closest conceptual match.
        """
        if not query or not query.strip():
            return "Please provide conversational text to analyze."
            
        # Convert user's English sentence directly into mathematics
        query_embedding = self.model.encode([query]).astype('float32')
        
        # Request FAISS to return exactly 1 mathematical Nearest Neighbor distance
        distances, indices = self.index.search(query_embedding, k=1)
        
        best_distance = distances[0][0]
        match_index = indices[0][0]
        
        # Dynamic distance threshold to prevent the AI from guessing nonsensical answers
        THRESHOLD = 1.45
        if best_distance > THRESHOLD:
            return "I apologize, but my current training dataset does not understand that context."
            
        # Safely extract the matched intent and yield a randomized corresponding response
        matched_intent = self.metadata[match_index]
        return random.choice(matched_intent["responses"])


# Generate a singular persistant application instance during FastAPI ASGI mounting
try:
    engine = VyomaChatbotEngine()
except Exception as e:
    engine = None
    print(f"CRITICAL FAISS / MODEL CORE FAILURE: {e}")


def get_response(message: str) -> str:
    """Global wrapper bridging the FastAPI Pydantic routes to the underlying AI intelligence natively."""
    if engine is None:
        return "Backend Offline: Unable to spin up SentenceTransformers or dataset resources."
    return engine.get_response(message)
