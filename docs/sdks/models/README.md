# Models
(*models*)

## Overview

Model information endpoints

### Available Operations

* [count](#count) - Get total count of available models
* [list](#list) - List all models and their properties
* [list_for_user](#list_for_user) - List models filtered by user provider preferences, privacy settings, and guardrails

## count

Get total count of available models

### Example Usage

<!-- UsageSnippet language="python" operationID="listModelsCount" method="get" path="/models/count" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.models.count()

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

**[components.ModelsCountResponse](../../components/modelscountresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list

List all models and their properties

### Example Usage

<!-- UsageSnippet language="python" operationID="getModels" method="get" path="/models" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.models.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |                                                                                                                                                   |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |                                                                                                                                                   |
| `category`                                                                                                                                        | [Optional[operations.Category]](../../operations/category.md)                                                                                     | :heavy_minus_sign:                                                                                                                                | Filter models by use case category                                                                                                                | programming                                                                                                                                       |
| `supported_parameters`                                                                                                                            | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | N/A                                                                                                                                               |                                                                                                                                                   |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[components.ModelsListResponse](../../components/modelslistresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list_for_user

List models filtered by user provider preferences, [privacy settings](https://openrouter.ai/docs/guides/privacy/logging), and [guardrails](https://openrouter.ai/docs/guides/features/guardrails). If requesting through `eu.openrouter.ai/api/v1/...` the results will be filtered to models that satisfy [EU in-region routing](https://openrouter.ai/docs/guides/privacy/logging#enterprise-eu-in-region-routing).

### Example Usage

<!-- UsageSnippet language="python" operationID="listModelsUser" method="get" path="/models/user" -->
```python
from openrouter import OpenRouter, operations
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
) as open_router:

    res = open_router.models.list_for_user(security=operations.ListModelsUserSecurity(
        bearer=os.getenv("OPENROUTER_BEARER", ""),
    ))

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                        | [operations.ListModelsUserSecurity](../../operations/listmodelsusersecurity.md)                                                                   | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[components.ModelsListResponse](../../components/modelslistresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |