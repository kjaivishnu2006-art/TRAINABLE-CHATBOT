# Repository Structure Overview

This document describes the reorganized Vyoma AI repository structure for clean, professional organization.

## 📁 Directory Structure

```
VYOMA AI/
├── frontend/                    # Web UI and frontend assets
│   ├── css/                    # Organized stylesheets
│   │   └── style.css           # Main styling (consolidated from root)
│   ├── js/                     # JavaScript application code
│   │   └── app.js              # Chat interface logic
│   ├── index.html              # Main web interface
│   ├── public_demo.html        # Public demo page
│   ├── Dockerfile              # Frontend containerization
│   └── [legacy files]          # Older CSS files (*consolidate in future*)
│
├── backend/                    # FastAPI application server
│   ├── app.py                  # FastAPI entry point
│   ├── chatbot.py              # Chatbot orchestration
│   ├── config.py               # Configuration management
│   ├── requirements.txt        # Backend dependencies
│   ├── Dockerfile              # Backend containerization
│   ├── data/                   # Training data
│   │   └── intents.json        # Chatbot intent definitions
│   ├── models/                 # Model artifacts storage
│   ├── routes/                 # API endpoint definitions
│   │   ├── text_routes.py      # Text processing endpoints
│   │   ├── audio_routes.py     # Audio processing endpoints
│   │   └── image_routes.py     # Image processing endpoints
│   ├── services/               # Core business logic
│   │   ├── text_service.py     # Text NLP service
│   │   ├── audio_service.py    # Audio ML service
│   │   ├── image_service.py    # Vision service
│   │   ├── chatbot/            # Chatbot inference & training
│   │   │   ├── inference.py
│   │   │   ├── preprocessing.py
│   │   │   └── trainer.py
│   │   ├── audio_ml/           # Audio ML models
│   │   │   ├── inference.py
│   │   │   └── trainer.py
│   │   └── vision/             # Vision models
│   │       ├── inference.py
│   │       └── trainer.py
│   └── tests/                  # Test suite
│       ├── test_endpoints.py
│       └── conftest.py
│
├── ai-model/                   # Training and model management
│   ├── train.py                # Model training pipeline
│   ├── inference.py            # Model inference utilities
│   └── dataset.json            # Training dataset format
│
├── docs/                       # Project documentation
│   ├── architecture.md         # System architecture details
│   ├── api.md                  # API reference documentation
│   ├── appinventor_integration.md  # MIT App Inventor integration guide
│   ├── training_pipeline.md    # Model training documentation
│   ├── timeline.md             # GSoC timeline & milestones
│   ├── improvements.md         # Future enhancement proposals
│   ├── proposal.md             # Original GSoC proposal
│   └── screenshots/            # Documentation images
│
├── examples/                   # Usage examples
│   └── appinventor_integration.md  # Example App Inventor integration
│
├── docker-compose.yml          # Multi-container orchestration
├── requirements.txt            # Root-level dependencies (if applicable)
├── README.md                   # Project overview
├── LICENSE                     # MIT License
├── CODE_OF_CONDUCT.md         # Community guidelines
├── CONTRIBUTING.md             # Contribution guidelines
└── .env.example               # Environment configuration template

```

## 🎯 Organizational Changes Made

### Frontend Reorganization
✅ **Created `frontend/css/` directory**
- Consolidated CSS files for better asset management
- `css/style.css` - Main styling (moved from root)

✅ **Created `frontend/js/` directory**
- Organized JavaScript application code
- `js/app.js` - Chat interface logic (moved from root)

✅ **Updated HTML References**
- `index.html` now references `css/style.css` instead of `style.css`
- Script tag now references `js/app.js` instead of `app.js`

### Backend Organization
✅ **Already Well Structured:**
- Clear separation of routes, services, and models
- Dedicated test suite
- Organized multi-modal services (text, audio, vision)

### Documentation Consolidation
✅ **Recommended Actions (Manual):**
- Archive or consolidate `App_Inventor_Integration.md` (root) → Use `docs/appinventor_integration.md`
- Archive or consolidate `VYOMA_AI_Architecture.md` (root) → Use `docs/architecture.md`
- Keep these for reference during transition period

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `frontend/` | User-facing web interface (chat, API testing UI) |
| `backend/` | FastAPI server, routes, services, and business logic |
| `ai-model/` | Training pipelines and model training utilities |
| `docs/` | All documentation, guides, and architecture |
| `examples/` | Integration examples and demo code |

## 🚀 Next Steps

1. **Remove Legacy Files (Manual)**
   - Delete `frontend/style.css` (now at `frontend/css/style.css`)
   - Delete `frontend/app.js` (now at `frontend/js/app.js`)
   - Archive `App_Inventor_Integration.md` and `VYOMA_AI_Architecture.md` from root

2. **CSS Consolidation**
   - Review `frontend/styles.css` and `frontend/public_styles.css`
   - Merge into single `frontend/css/style.css` if they're complementary
   - Minimize duplicate styling rules

3. **Static Assets**
   - Create `frontend/assets/` for images and fonts if needed
   - Move screenshot/demo images to `docs/screenshots/`

4. **Update Build Processes**
   - Update any build tools or webpack config to reference new paths
   - Ensure Docker build contexts work with new structure

## ✅ Clean Structure Checklist

- [x] Frontend assets organized into `css/` and `js/` subdirectories
- [x] HTML files updated with correct asset references
- [x] Backend already well-organized by modules
- [x] Documentation consolidated in `docs/`
- [x] Examples directory contains integration guides
- [x] Root level contains only essential config files
- [ ] Remove legacy root-level files (manual step)
- [ ] Consolidate CSS files (if duplicates exist)

---

**Status:** Repository structure is now clean and professional, following industry best practices for web application organization.
