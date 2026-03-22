# Integrating VYOMA AI with MIT App Inventor

This guide explains step-by-step how to connect your App Inventor mobile projects to the VYOMA AI Backend. We will use the native **Web** component to trigger our powerful Text, Image, and Audio capabilities without requiring custom extensions.

---

## 🏗️ Prerequisites
In MIT App Inventor, drag the following components into your project:
1. **Connectivity > Web** (Name it `Web1`)
2. **User Interface > Button** and **Label** (For triggering and displaying results)
3. **Media > Camera** (For image classification)
4. **Media > SoundRecorder** (For audio classification)

**Important Note on URLs:** 
If you are testing on your phone using the Companion app, `localhost` or `127.0.0.1` will look for a server *on the phone itself*. You must use your computer's local IP address (e.g., `http://192.168.1.15:5000/...`).

---

## 1. Text Classification / Chatbot (`/api/v1/text/chat`)

Because our Text API expects JSON `{"message": "hello"}`, we will construct a JSON dictionary and use `PostText`.

### 🧩 App Inventor Blocks Logic:
1. **When ButtonChat.Click:**
   - Set `Web1.Url` to `"http://<YOUR_IP>:5000/api/v1/text/chat"`
   - Set `Web1.RequestHeaders` to a list containing: `make a list -> "Content-Type", "application/json"`
   - Create the JSON Payload using the **Dictionaries** blocks:
     - `local payload` = `make a dictionary` with key `"message"` and value `TextBox.Text`
   - Call `Web1.PostText` with text `call Web1.JsonTextDecode(payload)` (Wait, reverse: we want to *encode* it to JSON string. App inventor usually has `Web1.JsonTextEncode` or you can manually join strings like `"{\"message\":\"" + TextBox.Text + "\"}"`).

2. **When Web1.GotText:**
   - Check if `responseCode` = 200.
   - `local responseDict` = `call Web1.JsonTextDecode(responseContent)`
   - Set `Label.Text` to `call get value for key "response" of dictionary responseDict`

---

## 2. Image Classification (`/api/v1/image/predict`)

Our backend expects an image file upload via `multipart/form-data`. Luckily, App Inventor's `Web.PostFile` block handles this natively. Note: Since `Web.PostFile` cannot easily attach text form data alongside the file, we will pass the required `dataset_id` dynamically into the URL itself as a Query Parameter (e.g., `?dataset_id=project_1`). 

### 🧩 App Inventor Blocks Logic:
1. **When ButtonCamera.Click:**
   - Call `Camera1.TakePicture`
2. **When Camera1.AfterPicture(imagePath):**
   - Set `Web1.Url` to `"http://<YOUR_IP>:5000/api/v1/image/predict?dataset_id=project_vision_1"`
   - Call `Web1.PostFile(imagePath)`
3. **When Web1.GotText:**
   - Check if `responseCode` = 200.
   - `local responseDict` = `call Web1.JsonTextDecode(responseContent)`
   - `local predictions` = `get value for key "predictions"`
   - Set `Label.Text` to `get value for key "class" in dictionary (select list item list: predictions index: 1)` *(This extracts the highest confidence class)*.

> *Backend Tweak needed:* In `image_routes.py`, change `request.form.get('dataset_id')` to `request.args.get('dataset_id')` so it reads from the URL query string!

---

## 3. Audio Classification (`/api/v1/audio/predict`)

Similar to images, audio files (.wav or .3gp from the SoundRecorder) are passed directly using `PostFile`.

### 🧩 App Inventor Blocks Logic:
1. **To Record:**
   - Call `SoundRecorder1.Start` (Wait 3-5 seconds based on a Clock timer).
   - Call `SoundRecorder1.Stop`
2. **When SoundRecorder1.AfterSoundRecorded(soundPath):**
   - Set `Web1.Url` to `"http://<YOUR_IP>:5000/api/v1/audio/predict?dataset_id=project_sonic_1"`
   - Call `Web1.PostFile(soundPath)`
3. **When Web1.GotText:**
   - Check if `responseCode` = 200.
   - `local responseDict` = `call Web1.JsonTextDecode(responseContent)`
   - `local predictions` = `get value for key "predictions"`
   - Set `Label.Text` to `get value for key "class" in dictionary (select list item: predictions index: 1)`

---

## 💡 Summary of Data Flow
1. **App Inventor:** Captures hardware inputs (Mic/Camera/Keyboard).
2. **Web Component:** Formats as bytes (`PostFile`) or strings (`PostText`) and opens an HTTP loop over Wi-Fi.
3. **FastAPI Backend:** Absorbs data, processes AI tensors in milliseconds, and returns a strictly typed JSON Dictionary.
4. **App Inventor:** Catch the response via `GotText`, parse the JSON Dictionary, and display the AI's ruling on the screen!
