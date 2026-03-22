# VYOMA AI: Multi-Modal Trainable AI Platform Architecture

Here is a GSoC-level architectural design for **VYOMA AI**, focusing on robustness, modularity, and seamless integration with MIT App Inventor ecosystems. 

## 1. High-Level Architecture Diagram
The architecture is designed around an asynchronous, decoupled micro-monolith approach. Separation of the API layer from heavy training workloads ensures the UI remains responsive even under heavy ML load.

```text
       [ MIT App Inventor Client / REST / Extensions ]
                 |                  |                  |
           (Prediction V1)   (Model Export)     (Live Preview WS)
                 |                  |                  |
+-------------------------------------------------------------------------+
|                        API GATEWAY & ROUTER (FastAPI)                   |
|  [ Auth Middleware ] [ Rate Limiter ] [ App Inventor JSON Serializer ]  |
+-------------------------------------------------------------------------+
            |                        |                        |
+----------------------+ +----------------------+ +-----------------------+
|  Dataset Ingestion   | | Inference Engine     | | Training Orchestrator |
|  (Stream Processing) | | (LRU Model Cache)    | | (Task Dispatcher)     |
+----------------------+ +----------------------+ +-----------------------+
            |                        |                        |
+-------------------------------------------------------------------------+
|                  MESSAGE BROKER / PUBSUB (Redis / RabbitMQ)             |
+-------------------------------------------------------------------------+
            |                        |                        |
+----------------------+ +----------------------+ +-----------------------+
|  Audio Worker (GPU/CPU)|  Image Worker (GPU)  | | Task Worker (CPU)     |
| [Torchaudio/Librosa]|  | [MobileNet/PyTorch]| | [TF-IDF/DistilBERT]     |
| [YAMNet Feature Extr]| | [Transfer Learning]  | | [Intent Classifier]   |
+----------------------+ +----------------------+ +-----------------------+
            |                        |                        |
+-------------------------------------------------------------------------+
|                            STORAGE LAYER                                |
|  [ METADATA ]: JSON / Document DB (MongoDB) - Configs, Annotations, I/O |
|  [ ARTIFACTS ]: File System / S3 - Images, WAVs, .tflite, saved_model   |
+-------------------------------------------------------------------------+

[ Web Frontend UI ] ----> (REST & WebSockets) ----> Connects to API Gateway
```

---

## 2. Module Breakdown

### A. Central Backend (FastAPI)
- **Role:** High-concurrency I/O gateway. Manages workspace sessions, streams large dataset uploads efficiently, and proxies App Inventor HTTP requests to the appropriate handlers.
- **App Inventor API Layer:** Exposes endpoints specifically optimized for App Inventor's `Web` component (e.g., `/api/v1/predict/text/{model_id}`). Payloads are strictly typed JSON (`{"class": "string", "confidence": float}`).
- **Orchestrator:** Submits async jobs to the Message Broker rather than awaiting them directly, preventing HTTP timeouts for long training sessions.

### B. Modality-Specific Training Modules (Decoupled Workers)
Each modality is an isolated worker, adhering to an abstract factory pattern (`BaseTrainer`). This allows the Image worker to load heavy PyTorch/CUDA dependencies without bloating the Text worker.
1. **Text Chatbot Module:**
   - *Architecture:* Processes text via a tokenization pipeline. Depending on dataset size, routes to a lightweight Intent Classifier (e.g., SVM over TF-IDF vectors) or fine-tunes a distilled transformer.
   - *App Inventor Context:* Outputs a dialogue tree JSON or a compiled generic classifier capable of extracting intents and returning predefined responses.
2. **Image Classifier Module:**
   - *Architecture:* Implements Deep Feature Extraction via a headless pre-trained model (MobileNetV2/EfficientNet). Only the final dense classification head is trained. 
3. **Audio Classifier Module:**
   - *Architecture:* Converts raw `.wav`/`.webm` to Mel-spectrograms. Uses standard audio backbones (like YAMNet or VGGish) to extract embeddings, followed by a shallow neural network classifier.

### C. Dataset Storage System
- **File System (Raw Artifacts):** Stores multi-modal blobs structurally. E.g., `/data/user_pool/{project_id}/image/{class_label}/{uuid}.jpg`.
- **JSON Metadata Map:** Lightweight index storing pointers to the file system, training hyperparameters, iteration states, and cross-modality linkings. JSON is crucial here as it allows bidirectional serialization directly to App Inventor dictionaries.

---

## 3. Data Flow (Lifecycle)

### Phase 1: Ingestion & Storage
1. **Client:** User uploads an image via the React Frontend or sends a REST `POST` from App Inventor.
2. **Gateway:** FastAPI receives the multi-part form data, generates a unique UUID, and streams the blob directly to the **File System** to manage RAM usage.
3. **State Update:** FastAPI updates the `project_state.json` (or NoSQL DB) appending the UUID to a specific class array (e.g., `Class: "Healthy_Plant"`).

### Phase 2: Training (Asynchronous Orchestration)
1. **Trigger:** User initiates compilation. FastAPI queues a job via **Redis** containing the project ID and modality type.
2. **Execution:** The specialized worker (e.g., Image Worker) picks up the task.
   - *Crucial Optimization:* It passes the new images through MobileNetV2 to extract 1D feature vectors and caches them. 
   - It trains a lightweight dense layer on these cached vectors (reducing epoch times from minutes to milliseconds).
3. **WebSocket Pub/Sub:** The worker streams loss/accuracy metrics to a Redis channel, which FastAPI broadcasts via WebSockets mapping to the Frontend UI for real-time visualization.
4. **Finalization:** The weights are quantized and packaged into a `.tflite` model (or ONNX) and a `model_manifest.json`, saved to the File System.

### Phase 3: Prediction & Inference Integration
1. **App Inventor Request:** An App target sends a Base64-encoded audio payload to `/api/v1/predict/{model_id}`.
2. **Inference Engine:** The Backend routes to the prediction engine. If the `model_id` is missing from memory, it lazy-loads the `.tflite` interpreter from the File System into an LRU (Least Recently Used) RAM Cache.
3. **Execution & Return:** The payload is evaluated, and the endpoint returns `{"predictions": [{"label": "Siren", "confidence": 0.92}]}`.

---

## 4. Scalability & Engineering Considerations (The GSoC Differentiators)

1. **Feature Caching (Compute Efficiency):** For Image and Audio, running the heavy backbone model (like MobileNet) during every single epoch is a naive approach. A senior-level architecture computes the embeddings *once* during the dataset upload phase (or right before epoch 1) and caches them. The training loop only optimizes a tiny top-layer network over these cached vectors. This allows free-tier or CPU-only cloud instances to train models instantly.
2. **TFLite Quantization Pipeline:** Since the ultimate goal is App Inventor, models must operate on the edge. The system must include a post-training quantization pipeline (INT8 or Float16) to shrink a 15MB model to < 3MB without significant accuracy degradation, optimizing it for Android deployment.
3. **Stateless Scalability:** The FastAPI backend is entirely stateless. State is managed by the JSON store, and async tasks are managed by Redis. This allows you to effortlessly spin up multiple FastAPI instances behind a load balancer (NGINX/Traefik) as user traffic increases.
4. **LRU Model Offloading:** In production, you cannot keep all trained user models in RAM. Implementing an LRU (Least Recently Used) cache within the Inference Engine ensures that actively queried ML models stay in memory (sub-10ms response times), while dormant models are gracefully evicted to disk, preventing out-of-memory (OOM) crashes.
