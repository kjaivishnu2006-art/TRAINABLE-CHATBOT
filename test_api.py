#!/usr/bin/env python3
"""Test Vyoma AI API and display response"""

import requests
import json

print("🧪 Testing Vyoma AI API")
print("=" * 60)

try:
    # Make API request
    url = "http://localhost:5000/chat"
    payload = {"message": "What can you do?"}
    headers = {"Content-Type": "application/json"}
    
    print(f"\n📍 API Endpoint: {url}")
    print(f"📤 Request Payload:\n{json.dumps(payload, indent=2)}")
    print("\n⏳ Sending request...")
    
    response = requests.post(url, json=payload, headers=headers, timeout=5)
    response.raise_for_status()
    
    result = response.json()
    
    print(f"\n✅ Response Status: {response.status_code}")
    print(f"📥 Response Body:\n{json.dumps(result, indent=2)}")
    
    print("\n" + "=" * 60)
    print("🎯 API Test Successful!")
    print("=" * 60)
    
except requests.exceptions.ConnectionError:
    print("❌ Error: Cannot connect to backend at http://localhost:5000")
    print("   Make sure backend is running: python backend/app.py")
except requests.exceptions.RequestException as e:
    print(f"❌ Error: {e}")
except json.JSONDecodeError:
    print(f"❌ Error: Invalid JSON response")
    print(f"Response text: {response.text}")
