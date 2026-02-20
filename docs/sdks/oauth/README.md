# OAuth
(*o_auth*)

## Overview

OAuth authentication endpoints

### Available Operations

* [exchange_auth_code_for_api_key](#exchange_auth_code_for_api_key) - Exchange authorization code for API key
* [create_auth_code](#create_auth_code) - Create authorization code

## exchange_auth_code_for_api_key

Exchange an authorization code from the PKCE flow for a user-controlled API key

### Example Usage

<!-- UsageSnippet language="python" operationID="exchangeAuthCodeForAPIKey" method="post" path="/auth/keys" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.o_auth.exchange_auth_code_for_api_key(code="auth_code_abc123def456")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `code`                                                                                                                                            | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The authorization code received from the OAuth redirect                                                                                           | auth_code_abc123def456                                                                                                                            |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |                                                                                                                                                   |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |                                                                                                                                                   |
| `code_verifier`                                                                                                                                   | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The code verifier if code_challenge was used in the authorization request                                                                         | dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk                                                                                                       |
| `code_challenge_method`                                                                                                                           | [OptionalNullable[operations.ExchangeAuthCodeForAPIKeyCodeChallengeMethod]](../../operations/exchangeauthcodeforapikeycodechallengemethod.md)     | :heavy_minus_sign:                                                                                                                                | The method used to generate the code challenge                                                                                                    | S256                                                                                                                                              |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[operations.ExchangeAuthCodeForAPIKeyResponse](../../operations/exchangeauthcodeforapikeyresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.ForbiddenResponseError      | 403                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## create_auth_code

Create an authorization code for the PKCE flow to generate a user-controlled API key

### Example Usage

<!-- UsageSnippet language="python" operationID="createAuthKeysCode" method="post" path="/auth/keys/code" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    http_referer="<value>",
    x_title="<value>",
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.o_auth.create_auth_code(callback_url="https://myapp.com/auth/callback")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                         | Type                                                                                                                                              | Required                                                                                                                                          | Description                                                                                                                                       | Example                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url`                                                                                                                                    | *str*                                                                                                                                             | :heavy_check_mark:                                                                                                                                | The callback URL to redirect to after authorization. Note, only https URLs on ports 443 and 3000 are allowed.                                     | https://myapp.com/auth/callback                                                                                                                   |
| `http_referer`                                                                                                                                    | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app identifier should be your app's URL and is used as the primary identifier for rankings.<br/>This is used to track API usage per application.<br/> |                                                                                                                                                   |
| `x_title`                                                                                                                                         | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | The app display name allows you to customize how your app appears in OpenRouter's dashboard.<br/>                                                 |                                                                                                                                                   |
| `code_challenge`                                                                                                                                  | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | PKCE code challenge for enhanced security                                                                                                         | E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM                                                                                                       |
| `code_challenge_method`                                                                                                                           | [Optional[operations.CreateAuthKeysCodeCodeChallengeMethod]](../../operations/createauthkeyscodecodechallengemethod.md)                           | :heavy_minus_sign:                                                                                                                                | The method used to generate the code challenge                                                                                                    | S256                                                                                                                                              |
| `limit`                                                                                                                                           | *Optional[float]*                                                                                                                                 | :heavy_minus_sign:                                                                                                                                | Credit limit for the API key to be created                                                                                                        | 100                                                                                                                                               |
| `expires_at`                                                                                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                              | :heavy_minus_sign:                                                                                                                                | Optional expiration time for the API key to be created                                                                                            |                                                                                                                                                   |
| `key_label`                                                                                                                                       | *Optional[str]*                                                                                                                                   | :heavy_minus_sign:                                                                                                                                | Optional custom label for the API key. Defaults to the app name if not provided.                                                                  | My Custom Key                                                                                                                                     |
| `usage_limit_type`                                                                                                                                | [Optional[operations.UsageLimitType]](../../operations/usagelimittype.md)                                                                         | :heavy_minus_sign:                                                                                                                                | Optional credit limit reset interval. When set, the credit limit resets on this interval.                                                         | monthly                                                                                                                                           |
| `retries`                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                  | :heavy_minus_sign:                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                               |                                                                                                                                                   |

### Response

**[operations.CreateAuthKeysCodeResponse](../../operations/createauthkeyscoderesponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |