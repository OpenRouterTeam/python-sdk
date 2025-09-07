
dependencies = [
    "openrouter",
    "os",
]

import os
from openrouter import OpenRouter

with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:
    res = open_router.chat.complete(
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?",
            },
        ],
        model="openai/gpt-3.5-turbo",
        stream=True
    )

    with res as event_stream:
        for event in event_stream:
            if event.data.choices and event.data.choices[0].delta.content:
                print(event.data.choices[0].delta.content, end='', flush=True)
        print()