#!/usr/bin/env python3
"""
Generate Vyoma AI Architecture Diagram
Shows data flow: User → Chat UI → FastAPI → AI Engine → Dataset → Response
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(14, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Color scheme
color_user = '#FF6B6B'
color_frontend = '#4ECDC4'
color_backend = '#45B7D1'
color_ai = '#FFA07A'
color_data = '#98D8C8'
color_response = '#A78BFA'

def draw_box(ax, x, y, width, height, text, color, fontsize=11, fontweight='bold'):
    """Draw a rounded box with text"""
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.1", 
                         edgecolor='black', 
                         facecolor=color,
                         linewidth=2,
                         alpha=0.8)
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize, 
            fontweight=fontweight, color='white')

def draw_arrow(ax, x1, y1, x2, y2, label='', color='black'):
    """Draw an arrow between two points"""
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=30, 
                           linewidth=2.5, color=color,
                           zorder=1)
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x, mid_y + 0.25, label, ha='center', fontsize=9, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Title
ax.text(5, 5.5, 'Vyoma AI Architecture Flow', fontsize=18, fontweight='bold', ha='center')

# Layer 1: User
draw_box(ax, 1, 4, 1.2, 0.8, '👤 User', color_user, fontsize=10)

# Layer 2: Chat UI (Frontend)
draw_box(ax, 2.5, 4, 1.4, 0.8, '💬 Chat UI\n(HTML/JS)', color_frontend, fontsize=10)

# Layer 3: FastAPI Backend
draw_box(ax, 4.5, 4, 1.4, 0.8, '🔌 FastAPI\n(REST API)', color_backend, fontsize=10)

# Layer 4: AI Engine (parallel processing)
draw_box(ax, 6.5, 4.5, 1.3, 0.8, '🧠 Preprocessing\n(TF-IDF)', color_ai, fontsize=9)
draw_box(ax, 6.5, 3.5, 1.3, 0.8, '🔍 FAISS Search\n(Vector Match)', color_ai, fontsize=9)

# Layer 5: Dataset
draw_box(ax, 8.5, 4, 1.2, 0.8, '📊 Dataset\n(intents.json)', color_data, fontsize=9)

# Layer 6: Response (lower level)
draw_box(ax, 6.5, 1.5, 2, 0.8, '✅ Intent + Confidence + Response', color_response, fontsize=10)

# Main flow arrows (left to right)
draw_arrow(ax, 1.6, 4, 2.15, 4, color='#333333')
draw_arrow(ax, 3.2, 4, 3.8, 4, color='#333333')
draw_arrow(ax, 5.2, 4, 5.85, 4.2, color='#333333')
draw_arrow(ax, 5.2, 4, 5.85, 3.8, color='#333333')

# AI to Dataset arrows
draw_arrow(ax, 7.15, 4.5, 7.85, 4.2, color='#666666')
draw_arrow(ax, 7.15, 3.5, 7.85, 3.8, color='#666666')

# Response flows back
draw_arrow(ax, 6.5, 3.2, 6.5, 2.1, color='#FF9800', label='Response')

# Add side annotations
ax.text(0.5, 5.8, 'Presentation Layer', fontsize=9, style='italic', 
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(4, 5.8, 'API Layer', fontsize=9, style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(6.5, 5.5, 'ML Engine', fontsize=9, style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(8.5, 5.2, 'Data Layer', fontsize=9, style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

# Add data flow labels
ax.text(1.75, 3.6, 'User input\n(text)', fontsize=8, ha='center',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.text(3.35, 3.6, 'HTTP POST\n/chat', fontsize=8, ha='center',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
ax.text(5.5, 5, 'Query text', fontsize=8, ha='center',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

# Bottom info box
info_text = """
📈 Process Flow:
1. User types message in Chat UI
2. Browser sends POST to FastAPI /chat endpoint
3. TF-IDF vectorizes user input
4. FAISS performs semantic similarity search in dataset
5. Top match returned with intent, confidence, response
6. Response displayed back in Chat UI
"""
ax.text(5, 0.3, info_text, fontsize=9, ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='#f0f0f0', edgecolor='gray', 
                 linewidth=2, alpha=0.9), family='monospace')

# Add tech stack notes
tech_text = "Tech: SentenceTransformers • FAISS • FastAPI • Uvicorn • NumPy • scikit-learn"
ax.text(5, -0.3, tech_text, fontsize=8, ha='center', style='italic', color='#666666')

plt.tight_layout()
plt.savefig('docs/architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✅ Architecture diagram saved to: docs/architecture.png")
