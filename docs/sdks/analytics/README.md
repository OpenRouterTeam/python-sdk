# Analytics

## Overview

Analytics and usage endpoints

### Available Operations

* [get_user_activity](#get_user_activity) - Get user activity grouped by endpoint

## get_user_activity

Returns user activity data grouped by endpoint for the last 30 (completed) UTC days. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="getUserActivity" method="get" path="/activity" -->
```python
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

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |                                                                                                                                                   |
| `x_open_router_title`                                                                                                                             | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |                                                                                                                                                   |
| `x_open_router_categories`                                                                                                                        | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Comma-separated list of app categories (e.g. "cli-agent,cloud-agent"). Used for marketplace rankings.<br/>                                        |                                                                                                                                                   |
| `date_`                                                                                                                                           | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Filter by a single UTC date in the last 30 days (YYYY-MM-DD format).                                                                              | 2025-08-24                                                                                                                                        |
| `api_key_hash`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Filter by API key hash (SHA-256 hex string, as returned by the keys API).                                                                         | abc123def456...                                                                                                                                   |
| `user_id`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Filter by org member user ID. Only applicable for organization accounts.                                                                          | user_abc123                                                                                                                                       |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[components.ActivityResponse](../../components/activityresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.ForbiddenResponseError      | 403                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |