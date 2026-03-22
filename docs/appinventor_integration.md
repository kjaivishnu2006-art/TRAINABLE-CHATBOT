# Connecting to MIT App Inventor

VYOMA AI does **not** rely on custom `.aix` extensions for baseline use, maximizing device compatibility. All integrations run natively through the App Inventor `Web` block.

## Integration Environment Setup
Ensure your smartphone (testing via Companion) and your local desktop are on the identical Wi-Fi network. **Do NOT use `127.0.0.1` inside App Inventor**, use the active IPv4 address assigned to the machine running the FastAPI backend.

---

## 1. Interfacing Text (Chatbot Interface)

**Blocks Overview:**
- `Web.Url` = `http://<YOUR_IP>:5000/api/v1/text/chat`
- `Web.RequestHeaders` = `Make a list -> "Content-Type" , "application/json"`
- Generate JSON via Dictionaries: `local dict -> key: "message", value: TextBox.Text`
- Trigger evaluation via `Web.PostText( Web.JsonTextEncode(dict) )`

**Retrieving Outputs:**
- Inside the Event block: `When Web.GotText(responseContent)`
- Use `Web.JsonTextDecode(responseContent)` to isolate dictionary keys.
- The chatbot's response string is actively mapped to the key `"response"`. 

---

## 2. Interfacing Images (Using the Phone Camera)

**Blocks Overview:**
Because you are shifting raw image buffers, App Inventor utilizes `Web.PostFile` over `multipart/form-data`.
- To attach Metadata (like the Dataset ID), inject it strictly as a URL Query Parameter immediately bypassing JSON headers.
- `Web.Url` = `http://<YOUR_IP>:5000/api/v1/image/predict?dataset_id=project_1`
- `Web.PostFile(Camera1.TakePicture.ImagePath)`

**Retrieving Outputs:**
- Inside `When Web.GotText(responseContent)` -> `Web.JsonTextDecode(responseContent)`
- The payload surfaces an ordered Dictionary array containing the key `"predictions"`.
- Use the `select list item (index 1)` block on the nested `predictions` list to pluck the Top-1 Highest Confident inference directly from the Support Vector boundaries.

---

## 3. Interfacing Audio (Using SoundRecorder)

**Blocks Overview:**
- `Web.Url` = `http://<YOUR_IP>:5000/api/v1/audio/predict?dataset_id=project_1`
- `SoundRecorder` captures `.wav` automatically locally.
- Use `Web.PostFile(SoundRecorder.AfterSoundRecorded.soundPath)`

**Retrieving Outputs:**
- Functions identically to the Image Parser. Pluck the `"predictions"` array from the resulting JSON blob inside the `GotText` block hook to extract the matched audio profile.
