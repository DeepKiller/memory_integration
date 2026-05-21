from mem0 import Memory
import ollama

def init_memory():
    memory = Memory.from_config({
        "llm": {
            "provider": "ollama",
            "config": {
                "model": CHAT_MODEL,
                "temperature": 0,
                "max_tokens": 2000,
                "ollama_base_url": OLLAMA_URL,
            },
        },
        "embedder": {
            "provider": "ollama",
            "config": {
                "model": "nomic-embed-text",
                "ollama_base_url": OLLAMA_URL,
            }
        }
    })
    return (memory,ollama)

@service
def memorize(user_input, chat_id):
    memory, ollama_chat = init_memory()
    memory.add(
        [
            {"role": "user", "content": user_input},
        ],
        user_id=chat_id,
    )

@service
def chat(user_input, chat_id, system_promt):
    memory, ollama_chat = init_memory()
    # Retrieve relevant memories
    memories = memory.search(user_input, filters={"chat_id": user_id}, top_k=10)
    context = "\n".join(m["memory"] for m in memories["results"])

    # Call LLM with memory context (Ollama via OpenAI-compatible API)
    response = ollama_chat.chat(
        model=CHAT_MODEL,
        messages=[
            {"role": "system", "content": f"{system_promt} Твои воспоминания:\n{context}"},
            {"role": "user", "content": user_input},
        ],
    )['message']['content']

    # Store the exchange
    memory.add(
        [
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": response},
        ],
        user_id=chat_id,
    )

    return response