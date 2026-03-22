#!/usr/bin/env python3
"""
Browser-based screenshot capture for Vyoma AI Chat UI
Uses Selenium to interact with the page and capture screenshots
"""

import time
import os
from pathlib import Path

def capture_with_selenium():
    """Capture screenshot using Selenium and Chrome"""
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.chrome.options import Options
        
        # Create screenshots directory
        screenshots_dir = Path("docs/screenshots")
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        
        # Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1280,800")
        # Uncomment below to run in headless mode
        # chrome_options.add_argument("--headless")
        
        # Initialize Chrome driver
        print("🌐 Launching Chrome browser...")
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            # Navigate to the frontend
            print("📍 Navigating to http://localhost:8000/index.html...")
            driver.get("http://localhost:8000/index.html")
            
            # Wait for page to load
            print("⏳ Waiting for page to load...")
            time.sleep(3)
            
            # Find the input field
            input_field = driver.find_element(By.ID, "chat-query")
            send_button = driver.find_element(By.ID, "send-btn")
            
            # Type "hello" in the input field
            print("✍️  Typing 'hello' into chat...")
            input_field.send_keys("hello")
            time.sleep(1)
            
            # Take screenshot with text in input
            screenshot_path = screenshots_dir / "chat_ui_with_input.png"
            driver.save_screenshot(str(screenshot_path))
            print(f"✅ Screenshot saved: {screenshot_path}")
            
            # Click send button
            print("🚀 Sending message...")
            send_button.click()
            
            # Wait for response
            print("⏳ Waiting for bot response...")
            time.sleep(2)
            
            # Take screenshot with response
            screenshot_path = screenshots_dir / "chat_ui_with_response.png"
            driver.save_screenshot(str(screenshot_path))
            print(f"✅ Screenshot saved: {screenshot_path}")
            
            # Get full chat window for better screenshot (focused on chat area)
            chat_window = driver.find_element(By.CLASS_NAME, "live-chat-wrapper")
            location = chat_window.location
            size = chat_window.size
            
            # Take focused screenshot
            driver.save_screenshot(str(screenshots_dir / "chat_ui_focused.png"))
            print(f"✅ Focused screenshot saved: {screenshots_dir / 'chat_ui_focused.png'}")
            
            print("\n✨ All screenshots captured successfully!")
            return True
            
        finally:
            driver.quit()
            print("🔌 Browser closed")
            
    except ImportError as e:
        print(f"❌ Selenium or WebDriver not available: {e}")
        print("   Install with: pip install selenium")
        return False
    except Exception as e:
        print(f"❌ Error during screenshot capture: {e}")
        return False

def manual_instructions():
    """Print manual screenshot instructions"""
    print("\n" + "="*60)
    print("📷 MANUAL SCREENSHOT INSTRUCTIONS")
    print("="*60)
    print("""
✅ STEP 1: Frontend & Backend Running
   - Backend: http://localhost:5000 (FastAPI)
   - Frontend: http://localhost:8000/index.html (Running)

✅ STEP 2: Take Screenshot of Chat UI
   1. Open: http://localhost:8000/index.html in your browser
   2. Type "hello" in the input field
   3. Press Enter or click Send button
   4. Take a screenshot showing:
      - Chat header: "Vyoma AI Engine"
      - Welcome message from bot
      - Your message "hello" in blue
      - Bot's response
      - Clean gradient background effect

✅ STEP 3: Save Screenshot
   - Save as: docs/screenshots/chat_ui.png
   - Recommended size: 1280x800px
   - Zoom: 100% (no zoom in/out)

💡 TIP: Use Windows Snipping Tool or screenshot app if Selenium fails
""")

if __name__ == "__main__":
    print("🎬 Vyoma AI Chat UI - Selenium Screenshot Capture")
    print("="*60)
    
    if capture_with_selenium():
        print("\n✨ Screenshot capture completed!")
    else:
        manual_instructions()
