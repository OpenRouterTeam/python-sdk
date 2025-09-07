
dependencies = [
    "openrouter",
    "os",
]

import os
from openrouter import OpenRouter

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY"),
) as sdk:
    result = sdk.chat.complete(
        messages=[
            {"role": "user", "content": "Hello, world!"},
        ],
        model="openai/gpt-3.5-turbo",
    )
    print("Basic completion:", result)
