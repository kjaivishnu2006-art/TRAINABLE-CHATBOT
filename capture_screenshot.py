#!/usr/bin/env python3
"""
Screenshot capture utility for Vyoma AI Chat UI
This script interacts with the chat interface and captures screenshots
"""

import time
import subprocess
import os
from pathlib import Path

# Ensure screenshots directory exists
screenshots_dir = Path("docs/screenshots")
screenshots_dir.mkdir(parents=True, exist_ok=True)

def take_screenshot_with_pyautogui():
    """Take a screenshot using pyautogui"""
    try:
        import pyautogui
        
        # Wait for page to render
        time.sleep(2)
        
        # Take screenshot
        screenshot = pyautogui.screenshot()
        screenshot.save(str(screenshots_dir / "chat_ui.png"))
        
        print(f"✅ Screenshot saved to: {screenshots_dir / 'chat_ui.png'}")
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"❌ Error with pyautogui: {e}")
        return False

def take_screenshot_with_pil():
    """Take a screenshot using PIL/Pillow ImageGrab"""
    try:
        from PIL import ImageGrab
        
        # Wait for page to render
        time.sleep(2)
        
        # Take screenshot
        screenshot = ImageGrab.grab()
        screenshot.save(str(screenshots_dir / "chat_ui.png"))
        
        print(f"✅ Screenshot saved to: {screenshots_dir / 'chat_ui.png'}")
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"❌ Error with PIL: {e}")
        return False

def take_screenshot_with_powershell():
    """Take a screenshot using PowerShell and .NET"""
    try:
        ps_script = r"""
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.Screen]::PrimaryScreen | ForEach-Object {
    $bitmap = New-Object System.Drawing.Bitmap($_.Bounds.Width, $_.Bounds.Height)
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.CopyFromScreen($_.Bounds.Location, [System.Drawing.Point]::Empty, $_.Bounds.Size)
    $bitmap.Save('""" + str(screenshots_dir / "chat_ui.png") + r"""')
    $graphics.Dispose()
    $bitmap.Dispose()
}
Write-Host "Screenshot saved successfully"
"""
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✅ Screenshot saved to: {screenshots_dir / 'chat_ui.png'}")
            return True
        else:
            print(f"❌ PowerShell error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error with PowerShell: {e}")
        return False

if __name__ == "__main__":
    print("🎬 Vyoma AI Chat UI Screenshot Capture")
    print("=" * 50)
    print(f"Browser should be open at: http://localhost:8000/index.html")
    print("Waiting for page to load...")
    
    # Try different methods in order of preference
    success = False
    
    # Try PIL/Pillow first (most reliable)
    if not success:
        print("\n📸 Trying PIL/Pillow ImageGrab method...")
        success = take_screenshot_with_pil()
    
    # Try pyautogui next
    if not success:
        print("\n📸 Trying pyautogui method...")
        success = take_screenshot_with_pyautogui()
    
    # Try PowerShell as fallback
    if not success:
        print("\n📸 Trying PowerShell method...")
        success = take_screenshot_with_powershell()
    
    if not success:
        print("\n❌ All screenshot methods failed.")
        print("\n📋 Alternative: Manual Screenshot Instructions")
        print("-" * 50)
        print("1. Frontend is running at: http://localhost:8000/index.html")
        print("2. Backend is running at: http://localhost:5000")
        print("3. Manually take a screenshot and save as: docs/screenshots/chat_ui.png")
        print("4. Make sure to show:")
        print("   - Chat header with 'Vyoma AI Engine'")
        print("   - Message from bot in chat window")
        print("   - Input field with text 'hello'")
        print("   - Clean UI with gradient background")
