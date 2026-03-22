from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

try:
    from chatbot import get_response
except ImportError:
    # Handle the fact that we might be run from root or from backend folder
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from chatbot import get_response


logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title="Vyoma AI Engine",
    description="GSoC FastAPI gateway for MIT App Inventor."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestPayload(BaseModel):
    message: str

@app.post("/chat")
async def process_chat(payload: RequestPayload):
    try:
        reply = get_response(payload.message)
        return {"reply": reply}
    except Exception as e:
        logging.error(f"Chat error: {e}")
        raise HTTPException(status_code=500, detail="Internal AI Error")

@app.get("/health")
async def health():
    return {"status": "operational", "system": "Vyoma GSoC Backend"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
