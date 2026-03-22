# Integrating Vyoma AI with MIT App Inventor

This beginner-friendly guide will walk you through seamlessly connecting your MIT App Inventor mobile application directly to the Vyoma AI Chatbot! 

The brilliant part about this architecture is that **you do not need to download or install any custom extensions (`.aix`)**. We use standard Web components to communicate securely over the internet.

---

## 1. Web Component Setup

First, let's set up the blocks you need in the Designer view:

1. Look on the left side of the screen and find the **Connectivity** palette.
2. Drag a **Web** component onto your phone screen (it will appear at the bottom as a hidden component).
3. Find the **User Interface** palette and drag in a **TextBox** (where users will type their message), a **Button** (to send), and a **Label** (to read the AI's reply).
4. Click on the **Web1** component. In the properties panel on the right, look for `Url`. Set this to your running backend address (for example: `http://192.168.1.50:8000/chat` if you are testing on your local Wi-Fi, or your public IP/Cloud URL).

---

## 2. POST Request Configuration

Now, switch to the **Blocks** editor. We need to tell the Web component to send data dynamically.

When the user clicks the Send Button (`when Button1.Click`):
1. **Set the Headers:**
   - Grab the block `set Web1.RequestHeaders to`.
   - Attach a `make a list` block.
   - Inside that list, add another `make a list` block containing two text pieces: `"Content-Type"` and `"application/json"`. *(This tells the AI engine you are sending structured data, not random text).*
2. **Send the Payload:**
   - Grab the block `call Web1.PostText`.
   - The `text` parameter needs to be converted properly. Attach a `call Web1.MakeJson` block.
   - Now, snap a `make a dictionary` block into it. Create a single pair where the key is `"message"` and the value is `TextBox1.Text`.

---

## 3. JSON Request Format

If you set up the blocks above correctly, MIT App Inventor silently converts your blocks into a pristine **JSON Payload** that looks exactly like this and beams it to the server:

```json
{
  "message": "Who essentially created you?"
}
```

---

## 4. JSON Response Format

Once the Vyoma AI server receives your message, it thinks about it, and sends back an answer in the exact same format!

**Expected Server Reply:**
```json
{
  "reply": "I am a GSoC project built for MIT App Inventor!"
}
```

### How to Decode the Reply in App Inventor:

To read this reply and show it to the user:
1. Bring out the `when Web1.GotText` block.
2. Grab an `if / then` block. Check if `responseCode = 200` *(this means the server worked perfectly).*
3. Use a dictionary lookup block: `get value for key "reply" of dictionary`.
4. The dictionary you are targeting is `call Web1.JsonTextDecode` attached to `responseContent`.
5. Snap all of this into `set Label1.Text to`!

---

## 5. Explanation: How It Works! 🧠

You might be wondering—how does the AI actually figure out what you said?

In older chatbots, developers had to write hundreds of lines of code asking *"If the user says exact word X, reply Y"*. This breaks constantly if the user makes a typo! 

**Vyoma AI solves this using Mathematics:**
1. When your phone sends the JSON payload, our server uses **SentenceTransformers** (a powerful machine learning model) to calculate the "meaning" of your sentence and turns it into a list of 384 numbers (a vector).
2. It then uses **FAISS** (an ultra-fast math library built by Facebook) to measure the distance between your numbers and the numbers it memorized during training.
3. The server finds the closest mathematical match and sends the exact string back down to your phone in milliseconds—even if you made a typo or phrased your question strangely!
