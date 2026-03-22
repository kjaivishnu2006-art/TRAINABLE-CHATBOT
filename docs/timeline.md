# GSoC 2026: 350-Hour Weekly Timeline
**Project:** Vyoma AI – Trainable Chatbot Interface for MIT App Inventor
**Format:** Large Size (~350 Hours, ~30 hours/week)

---

## Pre-Coding Phase: Community Bonding (May - June)
* **Goal:** Understand architectural boundaries and configure CI/CD pipelines.
* **Workload:** ~30 hours total.
* **Deliverables:**
  * Define the exact structure of `dataset.json`.
  * Setup Github Actions for linting and PyTest execution on pushes.
  * Establish weekly sync schedules with mentoring organizations.

---

## Phase 1: Core AI & NLP Infrastructure
* **Goal:** Abstract text matching into semantic embeddings.

### Week 1 (30 hrs)
* Initialize HuggingFace local models (`all-MiniLM-L6-v2`) via `sentence-transformers`.
* Design data-loaders to read and serialize patterns/intents safely.
* Write unit tests ensuring embeddings maintain geometric distance integrity.

### Week 2 (30 hrs)
* Embed `faiss-cpu` vector indices using Flat-L2 mappings.
* Develop the core logic storing pattern vectors alongside their string mappings via `.pkl` binaries.
* Ensure training loop completes in <2 seconds for standard JSON scopes.

### Week 3 (30 hrs)
* Develop `inference.py` to handle runtime nearest-neighbor distance calculating.
* Implement the Fallback Routine (if L2 distance > `1.4` -> route to Fallback response) to prevent AI hallucination.

---

## Phase 2: FastAPI Backend Engine
* **Goal:** Expose the AI pipeline securely to MIT App Inventor mobile devices.

### Week 4 (30 hrs)
* Transition synchronous AI class objects into a stateless Python `FastAPI` ASGI structure.
* Design the `POST /chat` endpoint logic holding the Pydantic BaseModels.

### Week 5 (30 hrs)
* Configure CORS logic natively allowing wildcard fetching from App Inventor components.
* Design comprehensive Error Models (500 Internal Error, 400 Bad Schema) returning cleanly.
* Start profiling end-to-end lookup latency (Target: <100ms per text block).

---

## Phase 3: MIT App Inventor Integration
* **Goal:** Bridge the HTTP functionality seamlessly into blocks.

### Week 6 (30 hrs)
* Spin up native App Inventor `.aia` test projects targeting local development URLs.
* Validate JSON encoding blocks and Web Component header rendering securely.
* Document strict differences in List vs Dictionary nesting within MIT App Inventor.

### Week 7 (30 hrs)
* Begin drafting `appinventor_integration.md`.
* Screen-capture every single necessary Web Block, from creating the payload down to traversing the JSON Decode tree.
* Submit early API payload formats to Mentors for UI feedback.

### Week 8 (30 hrs)
* Publish two massive sample applications:
  1. A minimal UI chatbot implementation.
  2. A highly designed "Virtual Assistant" template demonstrating intent capability.

---

## Phase 4: Frontend Web Studio
* **Goal:** Create a stunning desktop portal showcasing the underlying logic API.

### Week 9 (30 hrs)
* Wire JavaScript `fetch()` APIs inside `app.js` mapping user input synchronously over HTML endpoints.
* Handle API lag gracefully through Promise-based Javascript architectures.

### Week 10 (30 hrs)
* Implement advanced CSS elements (glassmorphism, drifting neon orbs, gradient accents).
* Record initial demonstration videos proving end-to-end functionality.

---

## Phase 5: Hardening & Final Submission
* **Goal:** Stress-test, polish, and formally deliver the final GSoC product.

### Week 11 (20 hrs)
* Squash minor memory leaks in the `faiss` context loads via object scoping.
* Clean up GitHub Issues, review Pull Requests, polish Docstrings globally across python functions.

### Week 12 (20 hrs)
* Compile the final GSoC writeup spanning problem scope, architecture proofs, and metric testing results.
* Submit the official Final Evaluation material.
* Create a YouTube presentation summarizing the 350-hour journey and feature set.
