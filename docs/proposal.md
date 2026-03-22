# GSoC 2026 Proposal Draft
# Trainable Chatbot Interface for MIT App Inventor (Vyoma AI)

## Abstract
The MIT App Inventor platform empowers millions to build mobile applications, yet lacks a sophisticated, natively decoupled conversational AI infrastructure. This project proposes a Trainable Chatbot Interface that allows users to seamlessly author training patterns, generate embeddings via SentenceTransformers, and evaluate them through a high-performance FAISS vector database. 

## Problem Statement
Current App Inventor extensions often rely on basic regex string matching or require complex setups connecting to paid external APIs (like OpenAI limits). There is no native, localized, and mathematically rigorous pipeline for educators to teach the mechanics of Natural Language Processing entirely from scratch.

## Technical Approach
1. **Model Generation (`ai-model/`)**: Uses HuggingFace `all-MiniLM-L6-v2` to vectorize JSON dictionaries of intents/responses.
2. **Indexing (FAISS)**: Accelerates high-dimensional matching to sub-millisecond speeds.
3. **Gateway API (`backend/`)**: A FastAPI stateless server exposes semantic search over HTTP perfectly to App Inventor.

## Timeline (12 Weeks)
- **Weeks 1-3:** Basic chatbot logic drifting and GitHub scaffold setup.
- **Weeks 4-6:** Build out FAISS querying optimization and fallback logic structure.
- **Weeks 7-9:** Construct the FastAPI gateways and cross-origin security integrations.
- **Weeks 10-11:** Develop the frontend Studio UI and MIT App Inventor block examples.
- **Week 12:** Intense unit testing, UI refinements, scaling metrics mapping.

## Deliverables
- Functional `ai-model` FAISS embedding script logic.
- Production-ready FastAPI interface (`/chat`).
- Comprehensive MIT App Inventor block integration guides.

## Risks
- CPU calculation bottlenecks.
  - *Mitigation:* FAISS optimizes for native C++ bound local hardware ensuring minimal lag.

## Impact
This project dynamically democratizes Artificial Intelligence within educational environments without relying blindly on external LLM paywalls!
