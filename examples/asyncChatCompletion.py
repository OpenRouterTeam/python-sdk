dependencies = [
    "openrouter",
    "os",
    "asyncio",
]

import os
import asyncio
from openrouter import OpenRouter

async def main():
    sdk = OpenRouter(
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )
    result = await sdk.chat.complete_async(
        messages=[
            {"role": "user", "content": "Hello, world!"},
        ],
        model="openai/gpt-3.5-turbo",
    )
    print("Basic async completion:", result)

if __name__ == "__main__":
    asyncio.run(main())