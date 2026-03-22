# System Architecture

## Overview
VYOMA AI is a modular, high-performance Multi-Modal Trainable AI Platform engineered as a decoupled micro-monolith. The ecosystem is designed to be highly accessible for MIT App Inventor integrations while maintaining production-grade robustness.

## Core Components

### 1. The Gateway (FastAPI)
The central nervous system of VYOMA AI. 
- **Role**: Handles highly concurrent I/O operations, stream multiplexing of large file uploads (images and audio), and acts as a router.
- **Why FastAPI?**: Because of its native asynchronous architecture. AI inference and training usually block event loops; FastAPI ensures that concurrent MIT App Inventor clients are serviced instantly while ML jobs execute asynchronously in the background.

### 2. Multi-Modal Machine Learning Modules
Isolated "Trainer" and "Inference" modules adhering strictly to SOLID principles.

* **Text Module (NLP):**
  - Consumes JSON strings. Uses `scikit-learn`'s `TfidfVectorizer` and Cosine Similarity to construct dialogue intent graphs. Extremely lightweight and fast.
* **Vision Module (CNN Extraction):**
  - Consumes `.jpg` and `.png` blobs. Incorporates a headless `MobileNetV2` neural network via TensorFlow to compute deep dimensional feature maps. These maps are cached and evaluated against a lightweight Support Vector Machine (SVC).
* **Audio Module (Time-Series Extractor):**
  - Consumes `.wav` blobs. Uses the `librosa` library to map waveform frequencies into 1D Mel-frequency cepstral coefficients (MFCCs). These coefficients are evaluated by a K-Nearest Neighbor (KNN) cluster network.

### 3. Persistent Storage Layer
- **Datasets**: Physical `.jpg` and `.wav` file structures organized dynamically on the Server (`/data/{modality}/{project_id}/{class_label}/items`).
- **Models**: Saved securely into stateful artifacts via `joblib` (`classifier.joblib`, `vectorizer.joblib`), ensuring extreme portability and offline caching capabilities for the App Inventor extension layer.

## The Scaling Strategy (Fast-Training)
By heavily utilizing feature caching (e.g., passing a fresh image through MobileNetV2 *once* during upload to extract vectors), the architecture compresses neural network epoch training from minutes to bare milliseconds. This bypasses the need for powerful, expensive GPU clusters and democratizes AI training scaling for all educational users.
