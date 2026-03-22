# GSoC 2026 Proposal Draft
# Trainable Chatbot Interface for MIT App Inventor (Vyoma AI)

## Abstract
The MIT App Inventor platform empowers millions to build mobile applications, yet lacks a sophisticated, natively decoupled conversational AI infrastructure. This project proposes a Trainable Chatbot Interface that allows users to seamlessly author training patterns, generate embeddings via SentenceTransformers, and evaluate them through a high-performance FAISS vector database. 

## Problem Statement
Current App Inventor extensions often rely on basic regex string matching or require complex setups connecting to paid external APIs (like OpenAI limits). There is no native, localized, and mathematically rigorous pipeline for educators to teach the mechanics of Natural Language Processing entirely from scratch.

## Project Size & Scope
**Size:** Large (~350 hours)  
**Duration:** 12 Weeks (approx. 30 hours/week)

## Detailed 350-Hour Evaluation Timeline

### Phase 1: Community Bonding & Architecture Validation (30 hrs)
- Set up weekly meeting schedules with mentors.
- Finalize the specific JSON schema structures for App Inventor parsing.
- Structure Github CI/CD pipelines for automated testing.

### Phase 2: Core AI Engine Engineering - Weeks 1-3 (90 hrs)
- **Week 1:** Imbed the HuggingFace `SentenceTransformers` (`all-MiniLM-L6-v2`) locally and write unit tests for vectorization accuracy.
- **Week 2:** Create the `faiss-cpu` Flat-L2 indexing system and serialize the metadata mapping to disk.
- **Week 3:** Design the fallback routines (threshold calculation to prevent hallucination) and finalize `ai-model/inference.py`.

### Phase 3: Fast API Backend Bridge - Weeks 4-5 (60 hrs)
- **Week 4:** Transition all synchronous routing to an asynchronous FastAPI ASGI gateway.
- **Week 5:** Apply CORS middleware, rate limiting stubs, and exact error schema mapping for standard HTTP responses.

### Phase 4: MIT App Inventor Integration - Weeks 6-8 (90 hrs)
- **Week 6:** Setup test Application within MIT App Inventor using raw Web Components to isolate block logic.
- **Week 7:** Author exhaustive, step-by-step pictorial guides mapping JSON dictionaries directly to nested blocks.
- **Week 8:** Develop sample `.aia` source files for the community gallery highlighting deployment.

### Phase 5: Frontend Studio Configuration - Weeks 9-10 (60 hrs)
- **Week 9:** Polish the Vanilla JavaScript `fetch()` handlers for the local demonstration UI.
- **Week 10:** Inject responsive CSS animations and prepare the visual architecture for public video demonstrations.

### Phase 6: Buffer & Final Submission - Weeks 11-12 (20 hrs)
- **Week 11:** Perform massive concurrent-request stress testing locally.
- **Week 12:** Author final project report, publish demo videos, and submit final GSoC deliverables.

## Deliverables
- Functional `ai-model` FAISS embedding script logic.
- Production-ready FastAPI interface (`/chat`).
- Comprehensive MIT App Inventor block integration guides.

## Risks
- CPU calculation bottlenecks.
  - *Mitigation:* FAISS optimizes for native C++ bound local hardware ensuring minimal lag.

## Impact
This project dynamically democratizes Artificial Intelligence within educational environments without relying blindly on external LLM paywalls!
