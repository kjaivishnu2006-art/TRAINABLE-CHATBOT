# MIT App Inventor Integration Guide (Vyoma AI)

Integrating Vyoma AI directly into MIT App Inventor requires **ZERO custom extensions**. You only need the native `Web` component.

## 1. Step-by-Step Web Component Setup
Drag a `Web` component into your application from the Connectivity palette.
You will also likely want a `TextBox` for user input, a `Button` to send, and a `Label` to read the reply.

- Set `Web1.Url` to your hosted deployment (e.g., `http://192.168.1.XX:8000/chat`).

## 2. The API POST Request
The logic requires configuring headers and passing a dictionary inside a POST payload dynamically.

### Block Configuration
When `Button1.Click`:
1. Use `set Web1.RequestHeaders to` and connect a `make a list`.
2. Inside that list, attach another `make a list` containing `"Content-Type"` and `"application/json"`.
3. Use `call Web1.PostText`.
4. The `text` parameter for PostText should be `call Web1.MakeJson`.
5. Pass a `make a dictionary` block containing a pair: `"message"` as the Key, and `TextBox1.Text` as the Value.

## 3. Expected JSON Format Sent
Behind the scenes, the blocks translate exactly into this payload to the server:
```json
{
  "message": "Hello robot, what can you do?"
}
```

## 4. Expected Response & Proof Explanation
Vyoma FAISS vector searches this input and answers structurally.

When `Web1.GotText`:
1. Check if `responseCode = 200`.
2. Set a local variable `decodedResponse` to `call Web1.JsonTextDecode` with the `responseContent`.
3. Use a dictionary lookup block: `get value for key "reply" of dictionary get decodedResponse`.
4. Set `Label.Text` to the extracted dictionary chunk.

### Proof Explanation
Because Vyoma AI utilizes SentenceTransformers, parsing "Hello robot, what can you do?" mathematically reduces to the core intent of "capabilities" in the FAISS index, seamlessly returning a high-accuracy result back to the mobile phone via HTTP. It bypasses the App Inventor memory limits completely!
