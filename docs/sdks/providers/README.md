# Providers
(*providers*)

## Overview

Provider information endpoints

### Available Operations

* [list](#list) - List all providers

## list

List all providers

### Example Usage

<!-- UsageSnippet language="python" operationID="listProviders" method="get" path="/providers" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.providers.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[operations.ListProvidersResponse](../../operations/listprovidersresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |