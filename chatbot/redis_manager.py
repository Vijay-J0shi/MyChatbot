import redis
import pickle
from .config import REDIS_HOST, REDIS_PORT, REDIS_KEY, SYSTEM_PROMPT

client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def load_history():
    try:
        cached = client.get(REDIS_KEY)
        if cached:
            print("[Redis] Loaded conversation history.")
            return pickle.loads(cached)
        else:
            print("[Redis] Initialized new conversation history.")
            return [{"role": "system", "content": SYSTEM_PROMPT}]
    except Exception as e:
        print(f"[Redis] Error: {str(e)}")
        return [{"role": "system", "content": SYSTEM_PROMPT}]

def save_history(history):
    client.set(REDIS_KEY, pickle.dumps(history))

def clear_history():
    client.delete(REDIS_KEY)
    print("[Redis] Conversation history cleared.")
