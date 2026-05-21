import os

os.environ["OPENAI_API_KEY"] = "ollama"

DEBUG = False
OLLAMA_URL = "http://76e18fb5-ollama:11434"
if DEBUG:
    OLLAMA_URL = "http://localhost:11434"

CHAT_MODEL = "qwen3:4b-instruct"
EMBED_MODEL = "nomic-embed-text"
EMBED_DIMENSIONS = 768
DB_NAME = "mem"
DB_PATH = "./mem.db"
