dependencies = [
    "openrouter",
    "os",
    "asyncio",
]

import os
import asyncio
from openrouter import OpenRouter

async def main():
    open_router = OpenRouter(
        api_key=os.getenv("OPENROUTER_API_KEY", ""),
    )
    res = await open_router.chat.complete_async(
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?",
            },
        ],
        model="openai/gpt-3.5-turbo",
        stream=True
    )

    async for event in res:  # type: ignore
        if event.data.choices and event.data.choices[0].delta.content:
            print(event.data.choices[0].delta.content, end='', flush=True)
    print()

if __name__ == "__main__":
    asyncio.run(main())