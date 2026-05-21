import db_manager
import llm_manager


@service
def memorize(user_input, message_id):
    db_manager.insert_data(user_input, message_id)


@service
def chat(user_input, system_promt):
    # Retrieve relevant memories
    memories = db_manager.load_data(user_input)
    context = "\n".join(m["memory"] for m in memories["results"])

    # Call LLM with memory context (Ollama via OpenAI-compatible API)
    response = llm_manager.chat(
        [
            {
                "role": "system",
                "content": f"{system_promt} Твои воспоминания:\n{context}",
            },
            {"role": "user", "content": user_input},
        ]
    )

    return response
