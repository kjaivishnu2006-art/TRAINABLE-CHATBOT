# 🎬 Vyoma AI - Demo Recording Guide

## Overview
This guide provides everything you need to record a professional 1-minute demo video of Vyoma AI for YouTube/GitHub.

---

## 📋 Demo Checklist

- [x] **Script written** - `DEMO_VIDEO_SCRIPT.md`
- [x] **Chat UI screenshot** - `docs/screenshots/chat_ui.png`
- [ ] **API demo screenshot** - `docs/screenshots/api_test.png`
- [ ] **App Inventor integration screenshot** - `docs/screenshots/appinventor_blocks.png`
- [ ] **Video recorded** - (20-60 minutes)
- [ ] **Video edited** - (30-60 minutes)
- [ ] **Video uploaded** - YouTube/GitHub

---

## 🎥 Recording Setup

### System Requirements
- **OS:** Windows 10+, macOS, or Linux
- **RAM:** 4GB+ (8GB recommended for smooth recording)
- **Storage:** 2GB free space for 1-minute 1080p video
- **Microphone:** Built-in or USB microphone recommended

### Software Needed

#### Option A: OBS Studio (FREE - Recommended)
```
Download: https://obsproject.com
- Open source
- Cross-platform
- Professional quality
- Free to use
```

#### Option B: ScreenFlow (macOS)
```
Download: https://www.telestream.net/screenflow/overview.html
- Built for Mac
- High quality
- Easy to use
```

#### Option C: Windows Built-in (FREE)
```
Use Windows Game Bar:
- Press: Windows + G
- Click "Record" to start
- Simple but limited features
```

---

## ⚙️ System Preparation

### 1. Start Backend & Frontend
```bash
# Terminal 1: Start Backend (FastAPI)
cd backend
python app.py
# Should see: "Uvicorn running on http://127.0.0.1:5000"

# Terminal 2: Start Frontend (Web Server)
cd frontend
python -m http.server 8000
# Should see: "Serving HTTP on 0.0.0.0 port 8000"
```

### 2. Verify Services Are Running
```bash
# Test Backend
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'

# Test Frontend
Open: http://localhost:8000/index.html in browser
```

### 3. Optimize Display
- **Resolution:** Set to 1920x1080 or 1280x720
- **Zoom:** Browser zoom 100% (or 125% if text too small)
- **Theme:** Dark mode (matches Vyoma UI)
- **Font Size:** Increase terminal to 14-16pt for visibility
- **Close Distractions:** Disable notifications, close Slack/Discord

---

## 🎬 Recording Instructions (OBS Studio)

### Step 1: Download & Install OBS
```
1. Go to https://obsproject.com
2. Download for your OS
3. Install and launch
4. Run first-time wizard (optional)
```

### Step 2: Create Recording Scene
```
1. Click "+" under "Scenes"
2. Name it: "Vyoma AI Demo"
3. Click "+" under "Sources"
4. Select: "Display Capture" or "Window Capture"
5. Choose your browser/window showing localhost:8000
```

### Step 3: Add Audio
```
1. In "Sources", click "+"
2. Select: "Audio Input Capture"
3. Choose your microphone
4. Use headphones to avoid echo
```

### Step 4: Configure Settings
```
1. Go to Settings (bottom-left gear icon)
2. Output → Recording Tab
3. Recording Path: Choose location for MP4
4. Encoder: H.264 (default is fine)
5. Recording Quality: Same as stream
6. Click "Apply"
```

### Step 5: Start Recording
```
1. Click: "Start Recording" button (red circle)
2. You'll see a timer showing elapsed time
3. Wait for scene to render (2 sec)
4. Begin narration
```

---

## 📹 What to Record (60 Seconds)

### Scene 1: Intro (0:00-0:05)
- **What to Show:**
  - Browser with Vyoma AI Studio open
  - Title screen visible
  - Clean, dark interface
- **What to Say:**
  > "Hi, welcome to Vyoma AI — a trainable chatbot platform built specifically for MIT App Inventor. This GSoC project makes AI accessible to non-programmers."
- **Technical:**
  - Read slowly and clearly
  - Pause after intro for emphasis

### Scene 2: Chat Demo (0:05-0:20)
- **What to Show:**
  1. Input field empty (0:05-0:06)
  2. Type "hello" slowly (0:06-0:09)
  3. Click send / Press Enter (0:09-0:10)
  4. Show bot response (0:10-0:15)
  5. Type "What can you do?" (0:15-0:17)
  6. Show response (0:17-0:20)

- **What to Say:**
  > "Watch this. I'll type 'hello' and the bot responds instantly using semantic understanding from SentenceTransformers and FAISS vector search. Unlike traditional regex chatbots, it understands meaning, not just keywords."

- **Key Points:**
  - Type at natural, visible speed
  - Wait for bot response to appear
  - Highlight instant response time

### Scene 3: API Demo (0:20-0:35)
- **What to Show:**
  1. Terminal with backend running (0:20-0:22)
  2. Show backend port 5000 (0:22-0:24)
  3. Show curl command (0:24-0:28)
  4. Execute curl request (0:28-0:30)
  5. Show JSON response (0:30-0:35)

- **What to Say:**
  > "Behind the scenes, the FastAPI backend handles incoming requests. Here's a real API call using curl. We send a simple JSON message and get back the chatbot's response with confidence scores."

- **Expected Response:**
  ```json
  {
    "reply": "I can classify text, images, and audio! I am a multi-modal trainable AI.",
    "intent": "capabilities",
    "confidence": 0.89
  }
  ```

### Scene 4: Integration (0:35-0:50)
- **What to Show:**
  1. MIT App Inventor project open (0:35-0:37)
  2. Show Web component block (0:37-0:40)
  3. Show request/response blocks (0:40-0:43)
  4. Show app preview with chat (0:43-0:50)

- **What to Say:**
  > "The magic happens here: MIT App Inventor integration. No custom extensions needed. We simply use the native Web component, send a JSON payload, and parse the response. This allows non-programmers to add AI to their mobile apps."

- **Key Points:**
  - Only native blocks used
  - No custom extensions
  - Completely drag-and-drop

### Scene 5: Outro (0:50-1:00)
- **What to Show:**
  1. Key statistics (0:50-0:55)
  2. GitHub repo link (0:55-0:58)
  3. Call-to-action (0:58-1:00)

- **What to Say:**
  > "This project enables non-programmers worldwide to build AI-powered applications without paying for expensive cloud APIs or writing complex code. Vyoma AI is open-source, free, and built for education. Check out the GitHub repo to get started."

- **Statistics to Display:**
  - Response Time: 50-77ms
  - Accuracy: 91%
  - Cost: FREE
  - Setup: 15 minutes

---

## 🛑 Stopping Recording

```
1. Read outro script completely
2. Pause 2 seconds (let text settle)
3. Click: "Stop Recording" button
4. OBS will save file to your chosen location
5. File should be ~50-200MB for 1-minute video
```

---

## ✂️ Post-Production (Video Editing)

### Basic Edits Needed
- Trim intro/outro (remove blank space)
- Add title card: "Vyoma AI - GSoC 2026"
- Add subtitles for API JSON response
- Add text overlays with key stats
- Background music (optional)

### Recommended Free Tools
1. **DaVinci Resolve** (Professional)
   - Download: https://www.blackmagicdesign.com/products/davinciresolve/
   - Free version is full-featured

2. **CapCut** (Mobile/Simple)
   - Easy for beginners
   - Works on Windows/Mac/Mobile

3. **OpenShot** (Linux)
   - Cross-platform free video editor

---

## 📤 Video Optimization

### YouTube Optimization
```
Resolution: 1920x1080 (1080p) or 1280x720 (720p)
Format: MP4 (H.264 codec)
Frame Rate: 30fps
Bitrate: 5-15 Mbps
Audio: 192 kbps, 48kHz
File Size: 50-150MB
Duration: 60 seconds
```

### Export Settings (OBS/DaVinci)
```
Container: MP4
Video Codec: H.264
Audio Codec: AAC
Resolution: 1920x1080
Frame Rate: 30fps
Bitrate: 10000 kbps
```

---

## 🎞️ YouTube Upload Checklist

```
Title:
"Vyoma AI - Trainable Chatbot for MIT App Inventor (Google Summer of Code 2026)"

Description:
GitHub: https://github.com/kjaivishnu2006-art/TRAINABLE-CHATBOT
Learn more: Check README for comprehensive documentation

Build intelligent AI-powered applications without coding!

Tags:
AI, chatbot, MIT App Inventor, machine learning, GSoC, education, semantic search, no-code

Thumbnail:
- Vyoma AI logo prominently
- Bold text: "Vyoma AI"
- Colors: Purple/blue gradient
```

---

## 📊 Demo Statistics for Video

| Metric | Value |
|--------|-------|
| **Response Time** | 50-77ms |
| **Accuracy** | 91% |
| **Cost** | FREE |
| **Setup Time** | 15 minutes |
| **Cloud APIs Cost** | $500-2000/year |
| **Supported Intents** | Unlimited (trainable) |
| **Typo Tolerance** | 82-94% |
| **Video Duration** | 60 seconds |

---

## 🎯 Key Talking Points

1. **Democratizes AI Education**
   - No coding required
   - Students can understand semantic NLP
   - Works on student laptops

2. **Cost Savings**
   - FREE (open-source)
   - No API charges
   - No vendor lock-in

3. **Perfect for MIT App Inventor**
   - Native integration
   - No extensions needed
   - REST API based
   - Beginner-friendly

4. **Production Ready**
   - 91% accuracy
   - Sub-100ms latency
   - Handles paraphrases
   - Typo tolerant

---

## 🚀 Publishing Checklist

- [ ] Video recorded (60 seconds)
- [ ] Video edited (titles, subtitles)
- [ ] Audio is clear (no background noise)
- [ ] Visuals are sharp (1080p)
- [ ] All 5 scenes complete
- [ ] Outro includes CTA
- [ ] File is labeled: `vyoma_ai_demo_final.mp4`
- [ ] YouTube metadata ready
- [ ] Social media captions prepared
- [ ] Video tested on mobile device

---

## 📞 Final Call-to-Action

**End Frame Should Include:**
```
🔗 GitHub: https://github.com/kjaivishnu2006-art/TRAINABLE-CHATBOT
⭐ Star the repo
📖 Read the docs
🚀 Build your first AI app
```

---

**Status: Ready to Record! 🎬**
