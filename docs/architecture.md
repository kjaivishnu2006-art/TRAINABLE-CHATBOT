# Vyoma AI: System Architecture

This document outlines the decoupled, 5-layer pipeline that powers the Vyoma AI Trainable Chatbot platform. By separating concerns at every level, the platform guarantees high stability and seamless MIT App Inventor integration.

---

## High-Level Data Flow

```text
+----------------+        +--------------------------+        +--------------------------+        +------------------------+        +--------------------------+
|  1. User       | -----> |  2. Frontend             | -----> |  3. Backend              | -----> |  4. AI Engine          | -----> |  5. Dataset              |
|  (Input text)  |        |  (Web / App Inventor)    |        |  (FastAPI Router)        |        |  (SentenceTransformers)|        |  (JSON Intents Matrix)   |
+----------------+        +--------------------------+        +--------------------------+        +------------------------+        +--------------------------+
       ^                               |                              |                                   |                                 |
       |                               |                              |                                   v                                 v
       +-------------------------------+------------------------------+-----------------------------------+---------------------------------+
                                       (Response payloads propagate upwards synchronously via HTTP JSON Returns)
```

---

## Detailed Component Analysis

### 1. The User 👤
The entry point of the entire application. The end-user interfaces with a visual layout—either typing a message mechanically or tapping an interface button to request assistance. 
* **Input Example:** *"What can this project do?"*

### 2. The Frontend 🖥📱
The client layer responsible for capturing the user's intent and securely packaging it over an HTTP network. 
* **Web Implementation (`frontend/`):** Utilizes Vanilla ES6 JavaScript `fetch()` promises inside a sleek glassmorphism UI.
* **Mobile Implementation (`App Inventor`):** Utilizes the native Web Connectivity (`call Web1.PostText`) block components to fire the payload securely.
* **Task:** Packages the raw text string into a strict JSON dictionary: `{"message": "What can this project do?"}`.

### 3. The Backend ⚡
The routing orchestrator completely decoupled from both the UI and the ML mathematics.
* **Component:** `fastapi` & `uvicorn` (ASGI Server).
* **Location:** `backend/app.py`.
* **Task:** Exposes the `POST /chat` endpoint. It securely intercepts the Frontend JSON, unwraps it, validates it against Pydantic constraint models, and passes it strictly to the connected AI wrapper.

### 4. The AI Engine 🧠
The core mathematical brain of Vyoma AI, replacing rigid Regex limits with advanced geometric algorithms.
* **Component:** HuggingFace `SentenceTransformers` & `faiss-cpu`.
* **Task:** When `backend/app.py` passes the string down, the AI Engine converts the user string into a robust 384-dimensional vector array. It then cross-references this dense vector against a pre-loaded FAISS index (`chatbot_index.faiss`) to find the mathematically closest "Nearest Neighbor" intent pattern.

### 5. The Dataset 🗄️
The ultimate source-of-truth mapping representing the localized knowledge base.
* **Component:** `ai-model/dataset.json` + `chatbot.pkl` metadata.
* **Task:** Once the FAISS engine determines exactly which vector is closest, it grabs the corresponding index from the flat Dataset mapping. It pulls the grouped `responses` list natively generated from the JSON matrix, and returns a dynamic, localized text reply all the way up the chain.
