
dependencies = [
    "openrouter",
    "os",
]

import os
from openrouter import OpenRouter

with OpenRouter(
    bearer_auth=os.getenv("OPENROUTER_API_KEY"),
) as sdk:
    result = sdk.chat.complete(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello, world!"},
        ],
    )

print(result)