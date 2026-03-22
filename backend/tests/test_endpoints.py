import json
import io

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert json.loads(response.data) == {"status": "healthy", "service": "VYOMA AI Backend"}

# --- TEXT ENDPOINTS ---
def test_text_train(client):
    payload = {
        "dataset": {
            "intents": [
                {"tag": "test", "patterns": ["hello"], "responses": ["hi"]}
            ]
        }
    }
    response = client.post('/api/v1/text/train', json=payload)
    assert response.status_code == 202
    assert 'job_id' in response.json

def test_text_chat_no_payload(client):
    response = client.post('/api/v1/text/chat', json={})
    assert response.status_code == 400

# --- IMAGE ENDPOINTS ---
def test_image_upload_missing_dataset(client):
    data = {}
    response = client.post('/api/v1/image/upload', data=data)
    assert response.status_code == 400
    assert 'dataset_id and class_name are required' in str(response.data)

def test_image_predict_no_file(client):
    data = {'dataset_id': 'project_1'}
    response = client.post('/api/v1/image/predict', data=data)
    assert response.status_code == 400

def test_image_predict_mock(client):
    data = {
        'dataset_id': 'project_1',
        'image': (io.BytesIO(b"fake image blob"), 'fake.jpg')
    }
    response = client.post('/api/v1/image/predict', data=data, content_type='multipart/form-data')
    # Should bounce because MobileNet cannot decode 'fake image blob'
    assert response.status_code in [400, 500]

# --- AUDIO ENDPOINTS ---
def test_audio_upload_missing_params(client):
    response = client.post('/api/v1/audio/upload', data={})
    assert response.status_code == 400

def test_audio_train_missing_dataset(client):
    response = client.post('/api/v1/audio/train', json={})
    assert response.status_code == 400
