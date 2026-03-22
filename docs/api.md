# VYOMA AI REST API Reference

All routes are prefixed with `/api/v1`. The API consumes standard JSON payloads and generic HTTP `multipart/form-data` requests.

---

## 1. Text Classification (`/text`)

### `POST /train`
Trigger TF-IDF intent training.
- **Headers**: `Content-Type: application/json`
- **Body**: 
```json
{
  "dataset": {
     "intents": [
       {
         "tag": "greeting", 
         "patterns": ["Hi", "Hello"], 
         "responses": ["Welcome!"]
       }
     ]
  }
}
```
- **Returns**: `202 Accepted` | `{"job_id": "uuid-string"}`

### `POST /chat`
Predict text intent based on trained models.
- **Headers**: `Content-Type: application/json`
- **Body**: `{"message": "raw text input"}`
- **Returns**: `200 OK` | `{"response": "matched_intent_response"}`

---

## 2. Image Classification (`/image`)

### `POST /upload`
Buffer raw images into structured class folders.
- **Headers**: `multipart/form-data`
- **Form-Data**:
  - `dataset_id` (String)
  - `class_name` (String: Label for this batch)
  - `image` (File Blob: .jpg/.png)
- **Returns**: `201 Created`

### `POST /train`
Compile MobileNet vectors into SVM spaces.
- **Headers**: `Content-Type: application/json`
- **Body**: `{"dataset_id": "project_vision_1"}`
- **Returns**: `200 OK`

### `POST /predict`
Assess image confidence levels.
- **Form-Data**: 
  - `dataset_id` (String)
  - `image` (File Blob)
- **Returns**: `200 OK`
```json
{
  "predictions": [
    {"class": "Cat", "confidence": 0.942},
    {"class": "Dog", "confidence": 0.058}
  ]
}
```

---

## 3. Audio Classification (`/audio`)

### `POST /upload`
Store `.wav` samples to the dataset structure.
- **Headers**: `multipart/form-data`
- **Form-Data**:
  - `dataset_id` (String)
  - `class_name` (String)
  - `audio` (File Blob: .wav)
- **Returns**: `201 Created`

### `POST /train`
Extract MFCC coefficients and train the KNN cluster.
- **Headers**: `Content-Type: application/json`
- **Body**: `{"dataset_id": "project_audio_1"}`
- **Returns**: `200 OK`

### `POST /predict`
Map raw decibels into intent clusters.
- **Form-Data**: 
  - `dataset_id` (String)
  - `audio` (File Blob)
- **Returns**: `200 OK`
```json
{
  "predictions": [
    {"class": "Dog_Bark", "confidence": 0.88},
    {"class": "Siren", "confidence": 0.12}
  ]
}
```
