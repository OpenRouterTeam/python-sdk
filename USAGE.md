<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openrouter import OpenRouter, models
import os


with OpenRouter(
    bearer_auth=os.getenv("OPENROUTER_BEARER_AUTH", ""),
) as open_router:

    res = open_router.chat.complete(messages=[
        {
            "role": models.ChatCompletionUserMessageParamRole.USER,
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
from openrouter import OpenRouter, models
import os

async def main():

    async with OpenRouter(
        bearer_auth=os.getenv("OPENROUTER_BEARER_AUTH", ""),
    ) as open_router:

        res = await open_router.chat.complete_async(messages=[
            {
                "role": models.ChatCompletionUserMessageParamRole.USER,
                "content": "Hello, how are you?",
            },
        ], stream=False, temperature=1, top_p=1)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->