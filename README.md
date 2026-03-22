# VYOMA AI: Multi-Modal Trainable AI Platform

<div align="center">
  <h3>A GSoC-Level Machine Learning Infrastructure for MIT App Inventor</h3>
</div>

**VYOMA AI** empowers educators, students, and hobbyists to effortlessly build, evaluate, and deploy text, image, and audio classification models locally. Inspired heavily by MIT App Inventor's Personal Image Classifier (PIC) and Personal Audio Classifier (PAC), this project modernizes and consolidates these standalone tools into a single, cohesive, decoupled micro-monolith.

---

## 🌟 Core Architecture & Features

This platform is structured around three primary pillars:

1. **The Abstract Backend (Flask/FastAPI-style)**: A stateless, asynchronous I/O gateway engineered to handle heavy multi-modal file streams without blocking.
2. **The ML Training Pipelines (Decoupled Workers)**:
   - **Text (NLP)**: TF-IDF vectorization with Cosine Similarity math for lightweight conversational agents.
   - **Vision (CNN)**: Headless `MobileNetV2` deep-feature extraction compiled over a fast-training Support Vector Machine (SVC).
   - **Audio (Time-Series)**: `librosa` MFCC signal processing mapped via K-Nearest Neighbor (KNN) prediction boundaries.
3. **The Studio UI**: A Vanilla HTML/CSS/JS glassmorphism Single Page Application prioritizing extreme usability, clarity, and modern design principles.

---

## 📁 Repository Structure

```text
VYOMA AI/
├── backend/
│   ├── app.py                   # Central routing and Error configuration
│   ├── config.py                # Environment configurations
│   ├── requirements.txt         # Core Dependencies (librosa, tensorflow-cpu, scikit-learn, flask)
│   ├── routes/                  # Controller layer
│   │   ├── audio_routes.py
│   │   ├── image_routes.py
│   │   └── text_routes.py
│   ├── services/                # Business logic and ML integration
│   │   ├── audio_service.py
│   │   ├── image_service.py
│   │   ├── text_service.py
│   │   ├── audio_ml/            # Sub-module: librosa + KNN
│   │   ├── chatbot/             # Sub-module: TF-IDF
│   │   └── vision/              # Sub-module: MobileNetV2 + SVC
│   ├── models/                  # Database / JSON ORM mappings
│   ├── data/                    # Dynamic upload storage (WAVs, JPGs)
│   └── tests/                   # Pytest automation suite
├── frontend/
│   ├── index.html               # Multi-tab UI Shell
│   ├── styles.css               # Glassmorphism dark mode definitions
│   └── app.js                   # Async Fetch APIs integrating with backend
├── docs/                        # Complete GSoC Technical Documentation
│   ├── api.md
│   ├── appinventor_integration.md
│   ├── architecture.md
│   ├── improvements.md
│   └── training_pipeline.md
└── README.md                    # You are here!
```

---

## 🚀 Setup & Installation (Local Development)

### 1. Backend Environment
Navigate to the backend directory and establish an isolated virtual environment to prevent dependency collisions.
```bash
cd backend
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
```

### 2. Ignite the Server
The development server will boot the ML environment and attach it to port 5000.
```bash
python app.py
```
*Health Check:* Visit `http://127.0.0.1:5000/health` in your browser to verify the JSON footprint.

### 3. Launch the Studio UI
There is no `npm install` required to run this high-performance UI! Simply open `frontend/index.html` locally in any modern web browser to interact seamlessly with the trained algorithms.

---

## 🧠 MIT App Inventor Integration
VYOMA AI runs cleanly without custom `.aix` extensions. You only need the native **Web**, **Camera**, and **SoundRecorder** components. 
- *To read the exact block-by-block logic, refer to `docs/appinventor_integration.md`.*

---

## 🔬 Running the Test Suite
A suite of Pytest assertions guards the multi-modal endpoints against regression.
```bash
cd backend
pytest tests/
```
