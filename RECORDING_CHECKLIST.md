# 📋 RECORDING SESSION CHECKLIST

## 🔧 PRE-RECORDING (Do this first)

```
Terminal 1: Start Backend
┌─────────────────────────────────────────────────────────┐
│ cd "c:\Users\Admin\OneDrive\Desktop\VYOMA AI"           │
│ .\.venv\Scripts\activate                                │
│ cd backend                                              │
│ python app.py                                           │
│ ✅ Wait for: "Uvicorn running on http://127.0.0.1:5000" │
└─────────────────────────────────────────────────────────┘

Terminal 2: Start Frontend
┌─────────────────────────────────────────────────────────┐
│ cd "c:\Users\Admin\OneDrive\Desktop\VYOMA AI\frontend"  │
│ python -m http.server 8000                              │
│ ✅ Wait for: "Serving HTTP on 0.0.0.0 port 8000"       │
└─────────────────────────────────────────────────────────┘

Browser: Open Chat UI
┌─────────────────────────────────────────────────────────┐
│ URL: http://localhost:8000/index.html                   │
│ ✅ See: Chat UI with "Interact with embeddings..."      │
└─────────────────────────────────────────────────────────┘

OBS Studio: Configure
┌─────────────────────────────────────────────────────────┐
│ ✅ Add Scene: "Vyoma AI Demo"                           │
│ ✅ Add Browser Source: http://localhost:8000/index.html │
│ ✅ Add Microphone Input                                 │
│ ✅ Output: 1920x1080, 30fps, 6000 Kbps                 │
│ ✅ Recording Path: recordings/ folder                   │
└─────────────────────────────────────────────────────────┘
```

---

## 🎬 RECORDING (≈60 seconds)

**Keep this visible while recording!**

```
🔴 Click: START RECORDING (OBS)
⏱️ Wait 2 seconds...

┌──────────────────────────────────────────────────────────┐
│  [0:00-0:05] INTRO (5 seconds)                          │
│  Script: "Hi, welcome to Vyoma AI — a trainable        │
│           chatbot platform built specifically for       │
│           MIT App Inventor..."                          │
│  Action: Speak clearly, hold camera on screen          │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│  [0:05-0:20] CHAT DEMO (15 seconds)                     │
│  Script: "Watch this. I'll type 'hello'..."            │
│  Action: 1. Click chat input field                      │
│          2. Type "hello" (slow, 2 sec)                 │
│          3. Press Enter                                │
│          4. Wait for response (3-5 sec)                │
│          5. Type "What can you do?" (slow, 2 sec)      │
│          6. Press Enter                                │
│          7. Wait for response (3-5 sec)                │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│  [0:20-0:35] API DEMO (15 seconds)                      │
│  Script: "Under the hood, we're using a REST API..."   │
│  Action: Show JSON response in browser/console         │
│  Expected: {"reply": "...", "intent": "greeting",      │
│             "confidence": 0.92}                         │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│  [0:35-0:50] APP INVENTOR (15 seconds)                  │
│  Script: "What makes this special? MIT App Inventor..." │
│  Action: Show integration example or screenshot        │
│  Reference: examples/appinventor_integration.md         │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│  [0:50-0:60] OUTRO (10 seconds)                         │
│  Script: "Check out the GitHub repository..."          │
│  Action: Show: https://github.com/kjaivishnu2006-art/  │
│                TRAINABLE-CHATBOT                       │
│          End with project logo/GitHub page             │
└──────────────────────────────────────────────────────────┘

🔴 Click: STOP RECORDING (OBS)
✅ File saved to: recordings/Vyoma_AI_Demo_[timestamp].mp4
```

---

## ✅ POST-RECORDING (Do this after)

```
1. Close OBS
2. Locate file: recordings/Vyoma_AI_Demo_*.mp4
3. Preview video:
   ✅ Audio clear?
   ✅ All 5 sections visible?
   ✅ ~60 seconds duration?
   ✅ No major mistakes?
4. [OPTIONAL] Edit video (DaVinci Resolve/CapCut)
5. Export as: 1920x1080 MP4, 8-12 Mbps bitrate
6. [OPTIONAL] Upload to YouTube
```

---

## 🆘 Quick Fixes

| Problem | Fix |
|---------|-----|
| Backend not connecting | Restart Terminal 1: `python app.py` |
| OBS blank canvas | Refresh browser source or restart frontend |
| No audio | Check mic in Audio Mixer (-6dB+) |
| Stuttering video | Lower bitrate to 4000 Kbps |
| Chat not responding | Run: `python test_api.py` |

---

## 📞 Help Files

- Full script: `DEMO_VIDEO_SCRIPT.md`
- Setup guide: `OBS_SESSION_SETUP.md` (this file's parent)
- API testing: `test_api.py`
- Integration docs: `examples/appinventor_integration.md`

---

**✨ Ready? Open DEMO_VIDEO_SCRIPT.md and START RECORDING!**
