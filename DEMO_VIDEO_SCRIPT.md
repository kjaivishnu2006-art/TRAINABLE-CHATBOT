# 🎬 Vyoma AI Demo Video - 1 Minute Script

## Project: TRAINABLE-CHATBOT (Google Summer of Code 2026)

---

## 📺 DEMO BREAKDOWN (60 Seconds Total)

### ⏱️ [INTRO] 0:00 - 0:05 (5 seconds)

**Script:**
> "Hi, welcome to Vyoma AI — a trainable chatbot platform built specifically for MIT App Inventor. This GSoC project makes AI accessible to non-programmers."

**Visual:**
- Show Vyoma AI Studio title screen
- Display GitHub repo
- Show project logo/branding

**Assets Needed:**
- `docs/screenshots/chat_ui.png` - Hero/intro shot

---

### 💬 [CHAT DEMO] 0:05 - 0:20 (15 seconds)

**Script:**
> "Watch this. I'll type 'hello' and the bot responds instantly using semantic understanding from SentenceTransformers and FAISS vector search. Unlike traditional regex chatbots, it understands meaning, not just keywords."

**Actions:**
1. Show chat input field (2 sec)
2. Type "hello" slowly (2 sec)
3. Press Enter (1 sec)
4. Show bot response (3 sec)
5. Type another message like "What can you do?" (2 sec)
6. Show response (3 sec)

**Visual:**
- Show browser at http://localhost:8000/index.html
- Chat window with messages
- Glassmorphic UI design

**Assets Needed:**
- `docs/screenshots/chat_ui.png` - Chat interface
- `docs/screenshots/chat_ui_conversation.png` - With messages

---

### 🔌 [API DEMO] 0:20 - 0:35 (15 seconds)

**Script:**
> "Behind the scenes, the FastAPI backend handles incoming requests. Here's a real API call using curl. We send a simple JSON message and get back the chatbot's response with confidence scores."

**Actions:**
1. Show terminal with backend running (1 sec)
2. Show curl command (2 sec)
3. Execute curl request (2 sec)
4. Show JSON response with reply, intent, and confidence (5 sec)
5. Explain the response structure (3 sec)

**Example Command:**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What can you do?"}'
```

**Expected Response:**
```json
{
  "reply": "I can classify text, images, and audio! I am a multi-modal trainable AI.",
  "intent": "capabilities",
  "confidence": 0.89
}
```

**Visual:**
- Terminal/PowerShell window
- FastAPI backend logs
- curl command execution
- JSON formatted response

**Assets Needed:**
- `docs/screenshots/api_test.png` - API request/response

---

### 📱 [INTEGRATION] 0:35 - 0:50 (15 seconds)

**Script:**
> "The magic happens here: MIT App Inventor integration. No custom extensions needed. We simply use the native Web component, send a JSON payload, and parse the response. This allows non-programmers to add AI to their mobile apps."

**Actions:**
1. Show MIT App Inventor project (2 sec)
2. Show Web component block (2 sec)
3. Show request/response payload blocks (2 sec)
4. Show message display in label (2 sec)
5. Summarize: explain benefits (5 sec)

**Talking Points:**
- Zero custom extensions required
- Uses only native App Inventor blocks
- REST API based communication
- Any student can build intelligent apps

**Visual:**
- MIT App Inventor screenshot
- Block-based code
- Chat interface in App Inventor preview

**Assets Needed:**
- `docs/screenshots/appinventor_blocks.png` - Integration example

---

### 🎯 [OUTRO] 0:50 - 1:00 (10 seconds)

**Script:**
> "This project enables non-programmers worldwide to build AI-powered applications without paying for expensive cloud APIs or writing complex code. Vyoma AI is open-source, free, and built for education. Check out the GitHub repo to get started."

**Actions:**
1. Show key stats (3 sec):
   - 50-77ms response time
   - 91% accuracy
   - FREE (no API costs)
2. Show GitHub link (2 sec)
3. Show project tagline (3 sec)

**Visual:**
- Project statistics
- GitHub repository URL
- Call-to-action

**Assets Needed:**
- README.md stats section
- GitHub repo link

---

## 📊 Demo Statistics to Highlight

| Metric | Value |
|--------|-------|
| Response Time | 50-77ms |
| Accuracy | 91% |
| Cost per Query | $0 (free) |
| Setup Time | 15 minutes |
| API Port | 5000 |
| Frontend Port | 8000 |

---

## 🎥 Recording Tips

### Setup
1. **Resolution:** 1280x720 (720p) minimum for clean recording
2. **Zoom:** 125-150% for better text visibility
3. **Font Size:** Increase terminal font to 14-16pt
4. **Background:** Dark mode (already have dark theme)
5. **Frame Rate:** 30fps is sufficient

### Tools
- **Video Recording:** OBS Studio (free), ScreenFlow, or built-in OS tools
- **Audio:** Use microphone with clear voice, speak slowly
- **Editing:** DaVinci Resolve (free), Adobe Premiere, or iMovie

### Timing
- Intro: 5 sec (read calmly)
- Chat: 15 sec (type at visible speed, wait for response)
- API: 15 sec (show output clearly, pause on response)
- Integration: 15 sec (explain while showing blocks)
- Outro: 10 sec (close with call-to-action)

---

## 📝 Script Reading Guide

### Pacing
- **Intro:** Measured introduction, set expectations
- **Chat:** Emphasize speed and accuracy
- **API:** Technical but accessible explanation
- **Integration:** Focus on accessibility for non-programmers
- **Outro:** Inspiring call-to-action

### Tone
- Professional but approachable
- Enthusiastic about democratizing AI
- Clear explanations without jargon

### Camera Angles
- Wide shot of full screen for intro
- Zoom in on chat interface for interaction
- Terminal output for API demo
- App Inventor blocks close-up for integration
- Full screen for closing shots

---

## 🎬 Recording Sequence

1. **Start Recording**
2. Read intro slowly (calibrate microphone level)
3. Interact with chat interface
4. Show terminal/API calls
5. Display App Inventor blocks
6. End with call-to-action
7. Stop Recording

### Total Time: ~75 seconds (allows for buffer)

---

## 📁 Required Screenshots (for reference)

- ✅ `docs/screenshots/chat_ui.png` - Chat interface
- ⏳ `docs/screenshots/api_test.png` - API response example
- ⏳ `docs/screenshots/appinventor_blocks.png` - Block integration

---

## 🚀 Quick Start to Record

### Prerequisite: Start Services
```bash
# Terminal 1: Backend
cd backend
python app.py

# Terminal 2: Frontend
cd frontend
python -m http.server 8000
```

### Record Using OBS Studio (Free)
1. Download: https://obsproject.com
2. Create new scene
3. Add screen capture source
4. Set audio input to microphone
5. Click "Start Recording"
6. Present as per script
7. Export as MP4

---

## ✨ Key Messages

**Primary:** "Vyoma AI makes AI accessible to non-programmers"

**Secondary Messages:**
- Free and open-source
- No expensive cloud APIs
- Native MIT App Inventor integration
- 50ms response time
- 91% semantic accuracy
- Built for education

---

## 📞 Call-to-Action

**End with:**
- GitHub: https://github.com/kjaivishnu2006-art/TRAINABLE-CHATBOT
- Stars: ⭐ Star the repo
- Learn: Read documentation
- Build: Create your first AI app

---

**Status:** Ready to record ✅
**Duration:** 60 seconds
**Framework:** Script-based with live demo
**Target Audience:** Educators, students, developers
