import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ai-model'))

try:
    from inference import ChatbotInference
    engine = ChatbotInference()
except Exception as e:
    engine = None
    print(f"Warning: Engine offline. Did you run train.py? Error: {e}")

def get_response(msg: str) -> str:
    if not engine:
        return "Backend AI Offline: Please run ai-model/train.py"
    if not msg.strip():
        return "Empty text received."
    return engine.predict(msg)
