<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.chat.complete(messages=[
        {
            "role": "user",
            "content": "Hello, how are you?",
        },
    ], stream=False, temperature=1, top_p=1)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from openrouter import OpenRouter
import os

async def main():

    async with OpenRouter(
        api_key=os.getenv("OPENROUTER_API_KEY", ""),
    ) as open_router:

        res = await open_router.chat.complete_async(messages=[
            {
                "role": "user",
                "content": "Hello, how are you?",
            },
        ], stream=False, temperature=1, top_p=1)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->