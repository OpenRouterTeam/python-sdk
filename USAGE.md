<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_open_router_title="<value>",
    x_open_router_categories="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.analytics.get_user_activity()

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
        http_referer="<value>",
        x_open_router_title="<value>",
        x_open_router_categories="<value>",
        api_key=os.getenv("OPENROUTER_API_KEY", ""),
    ) as open_router:

        res = await open_router.analytics.get_user_activity_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->