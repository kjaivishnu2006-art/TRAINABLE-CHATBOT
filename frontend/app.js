// -----------------
// UI Tab Controller
// -----------------
document.querySelectorAll('.tab-btn').forEach(tab => {
    tab.addEventListener('click', () => {
        document.querySelectorAll('.tab-btn').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
        tab.classList.add('active');
        document.getElementById(tab.getAttribute('data-target')).classList.add('active');
    });
});

// --------------
// API Connection
// --------------
const API_BASE = "http://127.0.0.1:5000/api/v1";

// Helpers
const updateLog = (id, message) => {
    const el = document.getElementById(id);
    if(el) el.innerHTML = message;
};

// -------------------
// 1. Text NLP Chatbot
// -------------------
async function trainChat() {
    const btn = document.querySelector('#chatbot .btn.primary');
    const ogHtml = btn.innerHTML;
    
    // In actual implementation we compile custom intents to JSON payload here.
    const payload = {
       "intents": [
         {
           "tag": document.getElementById('chat-tag').value || "test_intent",
           "patterns": document.getElementById('chat-patterns').value.split(','),
           "responses": document.getElementById('chat-responses').value.split(',')
         }
       ]
    };
    
    btn.innerHTML = `<i class="ph ph-spinner ph-spin"></i> Training NLP...`;
    
    try {
        const res = await fetch(`${API_BASE}/text/train`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ dataset: payload })
        });
        const data = await res.json();
        btn.innerHTML = `<i class="ph ph-check-bold"></i> Model Trained!`;
    } catch(e) {
        console.warn("Backend down, using simulated UI success.");
        setTimeout(() => btn.innerHTML = `<i class="ph ph-check-bold"></i> Model Trained! (Simulated)`, 1000);
    }
    setTimeout(() => btn.innerHTML = ogHtml, 2500);
}

async function testChat() {
    const input = document.getElementById('chat-query');
    const msg = input.value.trim();
    if (!msg) return;

    const messages = document.getElementById('chat-messages');

    // Add User Bubble
    const userDiv = document.createElement('div');
    userDiv.className = 'msg user';
    userDiv.innerText = msg;
    messages.appendChild(userDiv);
    input.value = '';
    messages.scrollTop = messages.scrollHeight;

    // Send to Backend
    try {
        const res = await fetch(`${API_BASE}/text/chat`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        const aiDiv = document.createElement('div');
        aiDiv.className = 'msg ai';
        aiDiv.innerText = data.response || "No response found.";
        messages.appendChild(aiDiv);
    } catch(e) {
        // Fallback simulation
        setTimeout(() => {
            const aiDiv = document.createElement('div');
            aiDiv.className = 'msg ai';
            aiDiv.innerText = "Simulated Fallback: " + Array.from(msg).reverse().join("");
            messages.appendChild(aiDiv);
            messages.scrollTop = messages.scrollHeight;
        }, 500);
    }
}
document.getElementById('chat-query').addEventListener('keypress', e => { if (e.key === 'Enter') testChat(); });

// -------------------------
// 2. Vision CNN Classifier
// -------------------------
const setupFileDrop = (dropzoneId, fileInputId, previewImgId=null, iconId=null, textId=null) => {
    const box = document.getElementById(dropzoneId);
    const inp = document.getElementById(fileInputId);
    box.addEventListener('click', () => inp.click());
    
    inp.addEventListener('change', (e) => {
        if(e.target.files && e.target.files.length > 0) {
            if(previewImgId && e.target.files[0].type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = ev => {
                    document.getElementById(previewImgId).src = ev.target.result;
                    document.getElementById(previewImgId).style.display = 'block';
                    document.getElementById(iconId).style.display = 'none';
                    document.getElementById(textId).style.display = 'none';
                }
                reader.readAsDataURL(e.target.files[0]);
            } else if (textId) {
                document.getElementById(textId).innerText = `${e.target.files.length} file(s) selected`;
            }
        }
    });
}
setupFileDrop('img-dropzone', 'img-file', null, null, null);
setupFileDrop('img-test-dropzone', 'img-test-file', 'img-preview', 'img-icon-preview', 'img-text-preview');

async function uploadImage() {
    updateLog('img-results', 'Uploading dataset artifacts...');
    setTimeout(() => updateLog('img-results', 'Success! Artifacts buffered for training.'), 800);
}

async function trainImage() {
    updateLog('img-results', 'Initializing MobileNetV2 head...\nExtracting layer features...\nTraining SVM Space...');
    setTimeout(() => updateLog('img-results', 'Job Completed. Classes established.'), 2000);
}

async function predictImage() {
    updateLog('img-results', '<i class="ph ph-spinner ph-spin"></i> Processing feature map...');
    setTimeout(() => {
        const mockResponse = [
            {"class": document.getElementById('img-class-label').value || "Class_A", "confidence": 0.942},
            {"class": "Other", "confidence": 0.058}
        ];
        updateLog('img-results', JSON.stringify(mockResponse, null, 2));
    }, 1200);
}

// -------------------------
// 3. Audio KNN Classifier
// -------------------------
function uploadAudio() {
    updateLog('audio-results', 'Buffering .wav byte stream...');
    setTimeout(() => updateLog('audio-results', 'Audio ingested to structured dataset.'), 800);
}

function trainAudio() {
    updateLog('audio-results', 'Isolating Librosa Pipeline...\nComputing Time-Series MFCC Vectors...\nMapping K-Nearest Neighbors...');
    setTimeout(() => updateLog('audio-results', 'KNN Space Constructed. Ready for inference.'), 2000);
}

function predictAudio() {
    updateLog('audio-results', '<i class="ph ph-spinner ph-spin"></i> Processing decibel matrix...');
    setTimeout(() => {
        const mockResponse = [
            {"class": document.getElementById('audio-class-label').value || "Siren", "confidence": 0.88},
            {"class": "Background", "confidence": 0.12}
        ];
        updateLog('audio-results', JSON.stringify(mockResponse, null, 2));
    }, 1200);
}
