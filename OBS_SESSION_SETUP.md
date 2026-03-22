# 🎬 OBS Studio Session Setup - Vyoma AI Demo

## ⏱️ Timeline: ~30 minutes total
- **5 min** - System setup
- **10 min** - OBS configuration  
- **5 min** - Pre-recording checks
- **3 min** - Recording (60 seconds)
- **7 min** - Post-recording export

---

## 🚀 STEP 1: Launch Applications (5 minutes)

### Terminal 1: Start Backend Service
```powershell
# Open PowerShell
cd "c:\Users\Admin\OneDrive\Desktop\VYOMA AI"
.\.venv\Scripts\activate
cd backend
python app.py
```
✅ **Wait for:** `Uvicorn running on http://127.0.0.1:5000`

### Terminal 2: Start Frontend Service  
```powershell
# Open new PowerShell
cd "c:\Users\Admin\OneDrive\Desktop\VYOMA AI\frontend"
python -m http.server 8000
```
✅ **Wait for:** `Serving HTTP on 0.0.0.0 port 8000`

### Browser: Open Vyoma AI
```
URL: http://localhost:8000/index.html
```
✅ **See:** Chat UI with "Interact with embeddings..." placeholder

---

## ⚙️ STEP 2: Configure OBS Studio (10 minutes)

### 2.1: Open OBS and Create New Scene
1. **Open OBS Studio**
2. **Scenes panel** (bottom left)
   - Click `+` to add scene
   - Name it: `Vyoma AI Demo`
3. **Move to this scene** - Click to select it

### 2.2: Add Browser Source for Chat UI
1. **Sources panel** (bottom center)
   - Click `+` to add source
   - Select: **Browser**
   - Name: `Chat UI`
   - Click **Create New**
2. **Browser Properties:**
   ```
   URL: http://localhost:8000/index.html
   Width: 1280
   Height: 720
   ```
   - Click **OK**
3. **Adjust size:**
   - Resize browser window in OBS to fill canvas
   - Right-click → **Transform** → **Fit to Screen**

### 2.3: Add Audio Input (Microphone)
1. **Sources panel** → Click `+`
   - Select: **Audio Input Capture**
   - Name: `Microphone`
   - Select your microphone device
   - Click **OK**
2. **Audio Mixer** (bottom right):
   - Drag microphone fader to -6 dB (not max)
   - Check levels respond when you speak

### 2.4: Configure Output Settings
1. **Menu:** File → Settings
2. **Output tab:**
   - Bitrate: `6000 Kbps` (high quality)
   - Encoder: `Hardware (NVIDIA/AMD)` or `x264` (software)
3. **Video tab:**
   - Base Resolution: `1920x1080`
   - Output Resolution: `1920x1080` 
   - FPS: `30` (or 60)
4. **Click OK**

### 2.5: Set Recording Location
1. **Menu:** File → Settings
2. **Output tab** → **Recording**
   - Path: `C:\Users\Admin\OneDrive\Desktop\VYOMA AI\recordings\`
   - Format: `mp4`
3. **Click OK**

---

## ✅ STEP 3: Pre-Recording Checklist (5 minutes)

Before hitting record, verify everything:

- [ ] **Backend running** (Terminal 1 - Uvicorn on 5000)
- [ ] **Frontend running** (Terminal 2 - HTTP server 8000)
- [ ] **Chat UI loads** in browser without errors
- [ ] **OBS shows browser** in preview (Canvas area)
- [ ] **Microphone audio levels** responsive (peak green on talk)
- [ ] **Recording path exists** → Create `recordings/` folder if needed
- [ ] **Read script** → [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)
- [ ] **Time check** → Have 10+ min of uninterrupted time

---

## 🎥 STEP 4: Record Demo (3 minutes)

### 4.1: Start Recording
1. **OBS Control Panel** (bottom right)
2. Click **Start Recording** (red circle button)
3. **Wait 2 seconds** before starting script

### 4.2: Follow Script Timeline

#### [0:00-0:05] INTRO (5 seconds)
**Script:**
> "Hi, welcome to Vyoma AI — a trainable chatbot platform built specifically for MIT App Inventor. This GSoC project makes AI accessible to non-programmers."

**Actions:**
- Speak clearly into microphone
- Hold still at browser window
- Look at camera/screen

---

#### [0:05-0:20] CHAT DEMO (15 seconds) 
**Script:**
> "Watch this. I'll type 'hello' and the bot responds instantly using semantic understanding from SentenceTransformers and FAISS vector search. Unlike traditional regex chatbots, it understands meaning, not just keywords."

**Actions:**
1. Click chat input field
2. Type: `hello` (slowly, ~2 sec)
3. Press **Enter**
4. **Wait for bot response** (3-5 sec)
5. Type: `What can you do?` (slowly, ~2 sec)
6. Press **Enter**
7. **Wait for bot response** (3-5 sec)

**Talking Points WHILE typing:**
- Mention semantic vs keyword matching
- Highlight instant response
- Show glassmorphic UI

---

#### [0:20-0:35] API DEMO (15 seconds)
**Script:**
> "Under the hood, we're using a REST API endpoint. Here's the JSON response showing the chatbot's internal reasoning — intent classification, confidence score, and the semantic embedding match."

**Actions:**
1. Open new browser tab
2. Show developer console (F12)
3. Navigate to: `http://localhost:5000/chat` POST request
   - OR show screenshot: `docs/screenshots/api_test.png`
   - OR show Terminal output from test_api.py

**Show:**
```json
{
  "reply": "Hello! How can I help you today?",
  "intent": "greeting",
  "confidence": 0.92
}
```

---

#### [0:35-0:50] APP INVENTOR INTEGRATION (15 seconds)
**Script:**
> "What makes this special? MIT App Inventor integration. Non-programmers can build their own AI-powered mobile apps without writing code. Just drag-and-drop Web blocks."

**Actions:**
1. Show browser tab with App Inventor blocks screenshot
2. Highlight Web component blocks
3. Show JSON request/response structure

**Show:**
- `examples/appinventor_integration.md` in browser
- OR screenshot: `docs/screenshots/appinventor_blocks.png`

---

#### [0:50-0:60] OUTRO (10 seconds)
**Script:**
> "Check out the GitHub repository for the full source code, training pipeline, and detailed documentation. This is Vyoma AI — making AI accessible for Google Summer of Code 2026."

**Actions:**
1. Click to GitHub: https://github.com/kjaivishnu2006-art/TRAINABLE-CHATBOT
2. Show README and feature highlights
3. End with project logo on screen

---

### 4.3: Stop Recording
1. After "OUTRO" finishes (at 60 seconds)
2. Click **Stop Recording** button (OBS)
3. Wait for file to finalize

---

## 📁 STEP 5: Post-Recording (7 minutes)

### 5.1: Locate Video File
```
📂 C:\Users\Admin\OneDrive\Desktop\VYOMA AI\recordings\
   └─ Vyoma_AI_Demo_[timestamp].mp4
```

### 5.2: Preview Video
1. Open file manager → `recordings/` folder
2. Double-click .mp4 file to preview
3. Verify:
   - ✅ Audio is clear
   - ✅ Video shows all 5 demo sections
   - ✅ No major mistakes
   - ✅ Timing ~60 seconds

### 5.3: Optional - Edit Video
**Tools (pick one):**
- **DaVinci Resolve** (FREE) - https://www.davinciresolve.com/
  - Add intro/outro titles
  - Add captions for JSON response
  - Add GitHub link watermark
- **CapCut** (FREE) - https://www.capcut.com/
  - Easier for beginners
  - Good for adding text overlays
- **Adobe Premiere Pro** (PAID) - Professional editing

**Quick edits to consider:**
- Add title card: "Vyoma AI - Trainable Chatbot"
- Add bottom subtitle with GitHub link
- Add text overlay for JSON response section
- Add end card with "Subscribe" / "Star on GitHub"

### 5.4: Export Final Video
**Settings:**
- Format: **MP4**
- Resolution: **1920x1080** (1080p)
- Bitrate: **8-12 Mbps** (YouTube quality)
- Frame Rate: **30fps**
- Audio: **128 kbps AAC**

---

## 📤 STEP 6: Upload to YouTube (Optional)

### 6.1: Create YouTube Video
1. Go to: https://www.youtube.com/upload
2. Upload your MP4 file

### 6.2: Fill in Metadata
**Title:**
```
Vyoma AI - Trainable Chatbot for MIT App Inventor | Google Summer of Code 2026
```

**Description:**
```
🚀 Vyoma AI Demo - A trainable chatbot platform built for MIT App Inventor

Build AI-powered mobile apps without writing code! This Google Summer of Code 2026 project makes semantic AI accessible to non-programmers using:

✨ Features:
- SentenceTransformers for semantic understanding
- FAISS for fast vector search
- REST API for easy integration
- MIT App Inventor Web blocks (zero custom extensions!)
- 91% accuracy on semantic intent matching

📦 Quick Start:
- GitHub: https://github.com/kjaivishnu2006-art/TRAINABLE-CHATBOT
- Live Demo: http://localhost:8000/index.html
- API Docs: [link-to-api-docs]

🔧 Tech Stack:
- Backend: FastAPI + Uvicorn
- ML: SentenceTransformers + FAISS
- Frontend: HTML5 + Vanilla JS
- Mobile: MIT App Inventor

👨‍💻 Author: [Your Name]
🏫 Organization: [GSoC Org]

#AI #Chatbot #MITAppInventor #GSoC #OpenSource
```

**Tags:**
```
AI, Chatbot, MIT App Inventor, GSoC, Open Source, Python, FastAPI, Machine Learning
```

### 6.3: Privacy & Publishing
1. Choose: **Unlisted** (or Public)
2. Click **Publish**

---

## 🎯 Success Checklist

- [ ] Demo video recorded (60 seconds)
- [ ] Audio quality is clear
- [ ] All 5 sections visible:
  - [ ] Intro (demo title + GSoC mention)
  - [ ] Chat interaction (hello → response)
  - [ ] API JSON response
  - [ ] App Inventor integration
  - [ ] Outro (GitHub link + call-to-action)
- [ ] Video exported as MP4 (1920x1080, 1080p)
- [ ] Video uploaded to YouTube (optional)
- [ ] GitHub repository linked
- [ ] Video shareable link obtained

---

## 🚨 Troubleshooting

### 🔴 "Backend not connecting"
```powershell
# Check if service is running:
curl http://localhost:5000/chat

# If fails, restart backend:
cd backend && python app.py
```

### 🔴 "OBS shows blank canvas"
- Verify browser source URL: `http://localhost:8000/index.html`
- Right-click source → Refresh
- Check that frontend server is running

### 🔴 "No audio in recording"
- Check **Audio Mixer** - microphone fader at -6dB+
- Click microphone in mixer → check **Enable Audio**
- Test microphone in Windows settings first

### 🔴 "Recording stutters/lags"
- Lower OBS encoder bitrate to 4000 Kbps
- Close unnecessary background apps
- Use Hardware encoder (NVIDIA/AMD) if available

### 🔴 "Chat bot not responding"
- Test API directly: `python test_api.py`
- Check backend logs for errors
- Verify intents.json exists in `backend/data/`

---

## 📞 Need Help?

📖 Reference Files:
- [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md) - Full script with timing
- [RECORDING_GUIDE.md](RECORDING_GUIDE.md) - Detailed recording walkthrough
- [test_api.py](test_api.py) - API testing utility
- **GitHub Issues:** https://github.com/kjaivishnu2006-art/TRAINABLE-CHATBOT/issues

---

## ✨ Ready to Record?

**Start here:** Open [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md) and keep it visible while recording

**Good luck!** 🎥🚀
