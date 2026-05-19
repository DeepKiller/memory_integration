from mem0 import Memory

DOMAIN = "memory_integration"

config = {
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "qwen3:4b",
            "temperature": 0.1,
            "max_tokens": 2000,
        }
    }
}

m = Memory.from_config(config)

def check_memory():
    return

async def async_setup(hass, config):
    hass.services.async_register(DOMAIN,"check_memory",check_memory)

    return True