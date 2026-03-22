document.addEventListener('DOMContentLoaded', () => {
    const inputField = document.getElementById('chat-query');
    const sendButton = document.getElementById('send-btn');
    const chatWindow = document.getElementById('chat-messages');
    
    // Abstract FastAPI routing
    const API_URL = 'http://localhost:8000/chat';

    function appendMessage(text, sender) {
        const msgWrapper = document.createElement('div');
        msgWrapper.className = `message ${sender} slide-in`;
        msgWrapper.textContent = text;
        
        chatWindow.appendChild(msgWrapper);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    async function processMessage() {
        const message = inputField.value.trim();
        if (!message) return;

        appendMessage(message, 'user');
        inputField.value = '';
        
        sendButton.style.opacity = '0.5';
        sendButton.disabled = true;

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message }) // Send dictionary payload
            });

            if(!response.ok) {
                throw new Error("API Failure");
            }

            const data = await response.json();
            
            // Artificial delay to make feeling natural
            setTimeout(() => {
                appendMessage(data.reply, 'bot');
            }, 500);
            
        } catch (error) {
            console.error('Fetch error:', error);
            setTimeout(() => {
                appendMessage("CRITICAL ERROR: Unable to reach FastAPI backend. Is it running on port 8000?", 'bot');
            }, 500);
        } finally {
            sendButton.style.opacity = '1';
            sendButton.disabled = false;
        }
    }

    sendButton.addEventListener('click', processMessage);
    
    inputField.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            processMessage();
        }
    });
});
