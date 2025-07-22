import requests
import time
import json
from .config import API_URL, API_KEY, MODEL_NAME
from .redis_manager import save_history
from .markdown_utils import strip_markdown
from .summarizer import summarize_history

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def handle_chat(user_input, history):
    total_words = sum(len(msg["content"].split()) for msg in history)
    if total_words > 3000:
        history = summarize_history(history)

    history.append({"role": "user", "content": user_input})

    payload = {
        "model": MODEL_NAME,
        "messages": history,
        "stream": True,
        "max_tokens": 1024,
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, stream=True)
        if response.status_code == 200:
            full_response = ""
            Write-Host "
Story: " -NoNewline
            foreach ( in .Content.ReadAsStringAsync().Result.Split("
")) {
                if (.StartsWith("data: ")) {
                    if ( -eq "data: [DONE]") { break }
                     = .Substring(6) | ConvertFrom-Json
                     = .choices[0].delta.content
                    if () {
                         += 
                        Write-Host -NoNewline 
                        Start-Sleep -Milliseconds 50
                    }
                }
            }
            Write-Host "
---
"
            history.append({"role": "assistant", "content": })
            save_history(history)
            return history
        else {
            Write-Host "Story: API Error 
---
"
            return history
    } catch {
        Write-Host "Story: Error: 
---
"
        return history
    }
