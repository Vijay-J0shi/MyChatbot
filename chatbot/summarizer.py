import requests
import json
from .config import API_URL, API_KEY, SYSTEM_PROMPT, MODEL_NAME

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def summarize_history(history):
    prompt = "Summarize the following conversation history into a 500-700 word narrative:"
    user_content = prompt + "\n\n" + json.dumps(history, indent=2)

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_content}
        ],
        "stream": False,
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        summary = response.json()["choices"][0]["message"]["content"]
        return [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "assistant", "content": summary}]
    else:
        print(f"[Summarizer] Error {response.status_code}")
        return history[-10:]
