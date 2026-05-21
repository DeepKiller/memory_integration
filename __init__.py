import db_manager
import llm_manager


@service
def memorize(user_input, message_id):
    db_manager.insert_data(user_input, message_id)


@service(supports_response="only")
def load_data(search, return_response=True):
    memories = db_manager.load_data(search)
    return { "memories": memories }


@service(supports_response="only")
def chat(user_input, system_promt, return_response=True):
    # Retrieve relevant memories
    response = ""
    try:
        memories = db_manager.load_data(user_input)
        context = ""
        
        for memory in memories:
            context += f'\n{memory}'

        response = task.executor(llm_manager.chat,
            [
                {
                    "role": "system",
                    "content": f"{system_promt} Твои воспоминания:\n{context}",
                },
                {"role": "user", "content": user_input},
            ]
        )
    except Exception as ex:
        response = str(ex)

    return { "response": response }
