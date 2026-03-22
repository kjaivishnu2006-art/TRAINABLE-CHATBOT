# 🎬 Vyoma AI Demo - Auto Start Recording Session
# This script starts everything you need. Just run it and then hit Record in OBS!

Write-Host "🚀 Starting Vyoma AI Record Session..." -ForegroundColor Green
Write-Host ""

# Create recordings folder if it doesn't exist
$RecordingsPath = "C:\Users\Admin\OneDrive\Desktop\VYOMA AI\recordings"
if (-not (Test-Path $RecordingsPath)) {
    New-Item -ItemType Directory -Path $RecordingsPath | Out-Null
    Write-Host "✅ Created recordings folder: $RecordingsPath" -ForegroundColor Green
}

# Terminal 1: Start Backend
Write-Host "📡 Starting Backend (FastAPI on port 5000)..." -ForegroundColor Cyan
$BackendScript = {
    cd "c:\Users\Admin\OneDrive\Desktop\VYOMA AI"
    .\.venv\Scripts\activate
    cd backend
    python app.py
}
Start-Process pwsh -ArgumentList "-NoExit -Command `"$BackendScript`""
Write-Host "   ✅ Backend terminal opened" -ForegroundColor Green

# Wait for backend to start
Start-Sleep -Seconds 3

# Terminal 2: Start Frontend
Write-Host "🌐 Starting Frontend (HTTP server on port 8000)..." -ForegroundColor Cyan
$FrontendScript = {
    cd "c:\Users\Admin\OneDrive\Desktop\VYOMA AI\frontend"
    python -m http.server 8000
}
Start-Process pwsh -ArgumentList "-NoExit -Command `"$FrontendScript`""
Write-Host "   ✅ Frontend terminal opened" -ForegroundColor Green

# Open browser
Write-Host "🌍 Opening Vyoma AI in browser..." -ForegroundColor Cyan
Start-Sleep -Seconds 2
Start-Process "http://localhost:8000/index.html"
Write-Host "   ✅ Browser opened" -ForegroundColor Green

# Open recording checklist
Write-Host "📋 Opening Recording Checklist..." -ForegroundColor Cyan
Start-Process notepad "c:\Users\Admin\OneDrive\Desktop\VYOMA AI\RECORDING_CHECKLIST.md"
Write-Host "   ✅ Checklist opened" -ForegroundColor Green

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "✨ READY TO RECORD!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "1️⃣  Open OBS Studio" -ForegroundColor Yellow
Write-Host "2️⃣  Add Browser Source: http://localhost:8000/index.html" -ForegroundColor Yellow
Write-Host "3️⃣  Add Microphone audio input" -ForegroundColor Yellow
Write-Host "4️⃣  Follow RECORDING_CHECKLIST.md timeline" -ForegroundColor Yellow
Write-Host "5️⃣  Click START RECORDING and follow the script" -ForegroundColor Yellow
Write-Host ""
Write-Host "Video will save to: $RecordingsPath" -ForegroundColor Green
Write-Host ""
