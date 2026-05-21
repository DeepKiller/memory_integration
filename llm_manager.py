from ollama import Client
import const


def get_ollama():
    return Client(host=const.OLLAMA_URL)


def embed(data):
    return get_ollama().embed(
        model=const.EMBED_MODEL,
        input=data,
        truncate=False,
        dimensions=const.EMBED_DIMENSIONS,
    )["embeddings"]


def chat(messages):
    return get_ollama().chat(model=const.CHAT_MODEL, messages=messages)["message"][
        "content"
    ]
