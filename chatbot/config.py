import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "https://llm.chutes.ai/v1/chat/completions"
API_KEY = os.getenv("API_KEY")

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_KEY = "vijay:conversation_history"
MODEL_NAME = "deepseek-ai/DeepSeek-V3-0324"
SYSTEM_PROMPT = "yo"
