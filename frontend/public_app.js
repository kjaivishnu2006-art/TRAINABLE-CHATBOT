// public_app.js - Logic for the Public Showcase of VYOMA AI

const BACKEND_URL = 'http://127.0.0.1:8000';

document.addEventListener('DOMContentLoaded', () => {
    const sendBtn = document.getElementById('send-btn');
    const queryInput = document.getElementById('public-query');
    const messagesContainer = document.getElementById('public-messages');

    // Handle floating scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = 1;
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.feature-card, .demo-content').forEach(el => {
        el.style.opacity = 0;
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease-out';
        observer.observe(el);
    });

    // Chatbot functionality
    const appendMessage = (text, sender) => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender} slide-in`;
        msgDiv.textContent = text;
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    };

    const handleChat = async () => {
        const query = queryInput.value.trim();
        if (!query) return;

        // User message
        appendMessage(query, 'user');
        queryInput.value = '';

        // API Call
        try {
            const res = await fetch(`${BACKEND_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: query })
            });

            if (!res.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await res.json();
            
            // Format response beautifully
            let botReply = '';
            if (data.reply) {
                botReply = data.reply;
            } else {
                 botReply = JSON.stringify(data);
            }

            setTimeout(() => {
                appendMessage(botReply, 'bot');
            }, 600); // Artificial delay for natural feel

        } catch (error) {
            console.error('Chat error:', error);
            setTimeout(() => {
                appendMessage("Uh oh! It looks like my backend brain is currently offline. Please deploy `python app.py` to bring me to life!", 'bot');
            }, 600);
        }
    };

    sendBtn.addEventListener('click', handleChat);
    queryInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleChat();
    });
});
