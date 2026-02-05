# Endpoints
(*endpoints*)

## Overview

Endpoint information

### Available Operations

* [list](#list) - List all endpoints for a model
* [list_zdr_endpoints](#list_zdr_endpoints) - Preview the impact of ZDR on the available endpoints

## list

List all endpoints for a model

### Example Usage

<!-- UsageSnippet language="python" operationID="listEndpoints" method="get" path="/models/{author}/{slug}/endpoints" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.endpoints.list(author="<value>", slug="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `author`                                                                                                                                          | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `slug`                                                                                                                                            | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[operations.ListEndpointsResponse](../../operations/listendpointsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list_zdr_endpoints

Preview the impact of ZDR on the available endpoints

### Example Usage

<!-- UsageSnippet language="python" operationID="listEndpointsZdr" method="get" path="/endpoints/zdr" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.endpoints.list_zdr_endpoints()

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

**[operations.ListEndpointsZdrResponse](../../operations/listendpointszdrresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |