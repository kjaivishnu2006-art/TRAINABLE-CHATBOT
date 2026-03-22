import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pickle
import os

def train_model():
    print("Loading AI dataset...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, 'dataset.json')

    with open(dataset_path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)

    print("Booting SentenceTransformer (all-MiniLM-L6-v2)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')

    corpus = []
    metadata = []

    for intent in dataset['intents']:
        for pattern in intent['patterns']:
            corpus.append(pattern)
            metadata.append({
                "tag": intent["tag"],
                "responses": intent["responses"]
            })

    print(f"Vectorizing {len(corpus)} strings...")
    embeddings = model.encode(corpus).astype('float32')

    print("Indexing FAISS logic...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, os.path.join(base_dir, "chatbot.faiss"))
    with open(os.path.join(base_dir, "chatbot.pkl"), "wb") as f:
        pickle.dump(metadata, f)
        
    print("Training complete! Vectors serialized.")

if __name__ == "__main__":
    train_model()
