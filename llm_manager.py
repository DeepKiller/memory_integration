from ollama import Client
import const

@pyscript_compile
def get_ollama():
    return Client(host=const.OLLAMA_URL)


def embed(data):
    return get_ollama().embed(
        model=const.EMBED_MODEL,
        input=data,
        truncate=False,
    )["embeddings"]


@pyscript_compile
def chat(messages):
    return get_ollama().chat(model=const.CHAT_MODEL, messages=messages, stream=False).message.content
