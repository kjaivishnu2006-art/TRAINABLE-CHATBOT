# Vyoma AI: System Architecture

The core of the Vyoma AI Trainable Chatbot is separating the heavy NLP matrix computations from the rapid application delivery API layer. This decoupling allows MIT App Inventor developers to consume the platform reliably.

## Complete System Flow 

### 1. The Knowledge Representation (Database Phase)
Users define their desired logic purely inside `ai-model/dataset.json`. The engine processes these dictionaries asynchronously rather than relying on bloated SQL databases, maximizing speed for small-to-medium datasets.

### 2. Semantic Embedding (The AI Phase)
Running `ai-model/train.py` calls HuggingFace's `SentenceTransformer` (`all-MiniLM-L6-v2`) locally to vector encode strings into a matrix. It then boots up `faiss-cpu`, compiling a Flat L2 geometric index map representing the knowledge boundaries.
- **Artifacts Generated:** `chatbot_index.faiss` and `metadata.pkl`.

### 3. FastAPI Gateway (The Backend Phase)
`backend/app.py` exposes the `POST /chat` route wrapped by ASGI protocols (via Uvicorn). The internal `backend/chatbot.py` script waits for requests, takes the string, dynamically vector-encodes it via the AI Phase models, queries the FAISS index, retrieves the Nearest Neighbor inference, and parses it cleanly.

### 4. Client Consumption (The Frontend Phase)
Two main consumers exist:
1. `frontend/index.html` via `app.js` which natively uses `fetch()` logic to append chatbot answers cleanly onto the DOM.
2. MIT App Inventor applications via native Web component blocks parsing the exact same JSON.

---
### Text Format High-Level Diagram

```text
       [ MIT App Inventor / Frontend Web UI ]
                       |
               (HTTP POST /chat)
                       |
                       v
             [ FastAPI Backend Engine ] 
             (Parses { "message": ... })
                       |
                       v
         [ Inference Engine (chatbot.py) ]
      (Generates 384-dimensional Vector Query)
                       |
                       v
[============= FAISS Flat L2 Index ===============]
|  Calculates closest Cosine/Euclidian Distance |
|  Finds Exact `Tag` Metadata inside `.pkl`     |
[==============================================]
                       |
                       v
               (Matches Best Response)
                       |
             [ FastAPI Backend Engine ]
          (Returns { "reply": ... })
                       |
       [ MIT App Inventor / Frontend Web UI ]
```
