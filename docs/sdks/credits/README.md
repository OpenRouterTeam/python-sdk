# Credits
(*credits*)

## Overview

Credit management endpoints

### Available Operations

* [get_credits](#get_credits) - Get remaining credits
* [create_coinbase_charge](#create_coinbase_charge) - Create a Coinbase charge for crypto payment

## get_credits

Get total credits purchased and used for the authenticated user. [Management key](/docs/guides/overview/auth/management-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="getCredits" method="get" path="/credits" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.credits.get_credits()

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

**[operations.GetCreditsResponse](../../operations/getcreditsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.ForbiddenResponseError      | 403                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## create_coinbase_charge

Create a Coinbase charge for crypto payment

### Example Usage

<!-- UsageSnippet language="python" operationID="createCoinbaseCharge" method="post" path="/credits/coinbase" -->
```python
from openrouter import OpenRouter, operations
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
) as open_router:

    res = open_router.credits.create_coinbase_charge(security=operations.CreateCoinbaseChargeSecurity(
        bearer=os.getenv("OPENROUTER_BEARER", ""),
    ), amount=100, sender="0x1234567890123456789012345678901234567890", chain_id=1)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                        | [operations.CreateCoinbaseChargeSecurity](../../operations/createcoinbasechargesecurity.md)                                                       | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `amount`                                                                                                                                          | *float*                                                                                                                                           | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `sender`                                                                                                                                          | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `chain_id`                                                                                                                                        | [components.ChainID](../../components/chainid.md)                                                                                                 | :heavy_check_mark:                                                                                                                                | N/A                                                                                                                                               |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |

### Response

**[operations.CreateCoinbaseChargeResponse](../../operations/createcoinbasechargeresponse.md)**

### Errors

| Error Type                          | Status Code                         | Content Type                        |
| ----------------------------------- | ----------------------------------- | ----------------------------------- |
| errors.BadRequestResponseError      | 400                                 | application/json                    |
| errors.UnauthorizedResponseError    | 401                                 | application/json                    |
| errors.TooManyRequestsResponseError | 429                                 | application/json                    |
| errors.InternalServerResponseError  | 500                                 | application/json                    |
| errors.OpenRouterDefaultError       | 4XX, 5XX                            | \*/\*                               |