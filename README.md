
# MyChatbot

This is a terminal-based chatbot that interacts with the DeepSeek API. It uses Redis to store conversation history and summarize when the chat grows large. The project is modularized for maintainability.

---

## Folder Structure

```

MyChatbot/
├── chatbot/
│   ├── **init**.py
│   ├── config.py
│   ├── redis\_manager.py
│   ├── markdown\_utils.py
│   ├── summarizer.py
│   └── chatbot\_core.py
├── main.py
├── .env
├── requirements.txt
└── README.md

````

---

## Features

- Uses DeepSeek LLM via API to generate responses.
- Redis used to cache and manage conversation history.
- When token limit approaches, the history is summarized automatically.
- Command line interface with streaming output.

---

## Prerequisites

- Python 3.8 or above
- Redis server running locally
- A valid API key from [DeepSeek](https://deepseek.com) (or the appropriate provider)

---

## Setup Instructions

1. **Clone or download this repository**

   Make sure you are inside a working directory:
   ```bash
   cd MyChatbot

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**

   Create a `.env` file in the root directory and add:

   ```
   API_KEY=your_deepseek_api_key
   ```

6. **Start your Redis server**

   Ensure Redis is running on the default port 6379:

   ```bash
   redis-server
   ```

   You can check with:

   ```bash
   redis-cli ping
   # Should return PONG
   ```

---

## Running the Chatbot

After setup:

```bash
python main.py
```

You’ll get a prompt:

```
Vijay:
```

You can start chatting. Example:

```
Vijay: Tell me a short story about a robot who learns to code.
```

---

## In-Chat Commands

* `clear`: Clears the current conversation history from Redis.
* `exit`: Exits the chatbot.

---

## Notes

* The chatbot summarizes old messages to stay under token limits.
* All requests are streamed to simulate a natural typing effect.
* No UI is used — this is fully CLI-based.

---

## License

This is a personal/educational project. No license applied.

