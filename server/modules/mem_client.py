# modules/mem_client.py
from dotenv import load_dotenv
from mem0 import Memory
import os

load_dotenv()

config = {
    "version": "v1.1",
    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model": "gemini-2.5-flash"
        }
    },
    "embedder": {
        "provider": "gemini",
        "config": {
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model": "models/text-embedding-004"  # 768 dims
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "url": os.getenv("QDRANT_URL"),
            "api_key": os.getenv("QDRANT_API_KEY"),
            "collection_name": "mem0_memory",
            "embedding_model_dims": 768
        }
    }
}

mem_client = Memory.from_config(config)
