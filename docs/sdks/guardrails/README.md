# Guardrails
(*guardrails*)

## Overview

Guardrails endpoints

### Available Operations

* [list](#list) - List guardrails
* [create](#create) - Create a guardrail
* [get](#get) - Get a guardrail
* [update](#update) - Update a guardrail
* [delete](#delete) - Delete a guardrail
* [list_key_assignments](#list_key_assignments) - List all key assignments
* [list_member_assignments](#list_member_assignments) - List all member assignments
* [list_guardrail_key_assignments](#list_guardrail_key_assignments) - List key assignments for a guardrail
* [bulk_assign_keys](#bulk_assign_keys) - Bulk assign keys to a guardrail
* [list_guardrail_member_assignments](#list_guardrail_member_assignments) - List member assignments for a guardrail
* [bulk_assign_members](#bulk_assign_members) - Bulk assign members to a guardrail
* [bulk_unassign_keys](#bulk_unassign_keys) - Bulk unassign keys from a guardrail
* [bulk_unassign_members](#bulk_unassign_members) - Bulk unassign members from a guardrail

## list

List all guardrails for the authenticated user. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGuardrails" method="get" path="/guardrails" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `offset`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Number of records to skip for pagination                            | 0                                                                   |
| `limit`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Maximum number of records to return (max 100)                       | 50                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListGuardrailsResponse](../../operations/listguardrailsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## create

Create a new guardrail for the authenticated user. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="createGuardrail" method="post" path="/guardrails" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.create(name="My New Guardrail")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `name`                                                                                                                      | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | Name for the new guardrail                                                                                                  | My New Guardrail                                                                                                            |
| `description`                                                                                                               | *OptionalNullable[str]*                                                                                                     | :heavy_minus_sign:                                                                                                          | Description of the guardrail                                                                                                | A guardrail for limiting API usage                                                                                          |
| `limit_usd`                                                                                                                 | *OptionalNullable[float]*                                                                                                   | :heavy_minus_sign:                                                                                                          | Spending limit in USD                                                                                                       | 50                                                                                                                          |
| `reset_interval`                                                                                                            | [OptionalNullable[operations.CreateGuardrailResetIntervalRequest]](../../operations/createguardrailresetintervalrequest.md) | :heavy_minus_sign:                                                                                                          | Interval at which the limit resets (daily, weekly, monthly)                                                                 | monthly                                                                                                                     |
| `allowed_providers`                                                                                                         | List[*str*]                                                                                                                 | :heavy_minus_sign:                                                                                                          | List of allowed provider IDs                                                                                                | [<br/>"openai",<br/>"anthropic",<br/>"deepseek"<br/>]                                                                       |
| `allowed_models`                                                                                                            | List[*str*]                                                                                                                 | :heavy_minus_sign:                                                                                                          | Array of model identifiers (slug or canonical_slug accepted)                                                                | [<br/>"openai/gpt-5.2",<br/>"anthropic/claude-4.5-opus-20251124",<br/>"deepseek/deepseek-r1-0528:free"<br/>]                |
| `enforce_zdr`                                                                                                               | *OptionalNullable[bool]*                                                                                                    | :heavy_minus_sign:                                                                                                          | Whether to enforce zero data retention                                                                                      | false                                                                                                                       |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[operations.CreateGuardrailResponse](../../operations/createguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## get

Get a single guardrail by ID. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="getGuardrail" method="get" path="/guardrails/{id}" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.get(id="550e8400-e29b-41d4-a716-446655440000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the guardrail to retrieve                  | 550e8400-e29b-41d4-a716-446655440000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.GetGuardrailResponse](../../operations/getguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## update

Update an existing guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateGuardrail" method="patch" path="/guardrails/{id}" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.update(id="550e8400-e29b-41d4-a716-446655440000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                        | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | The unique identifier of the guardrail to update                                                                            | 550e8400-e29b-41d4-a716-446655440000                                                                                        |
| `name`                                                                                                                      | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | New name for the guardrail                                                                                                  | Updated Guardrail Name                                                                                                      |
| `description`                                                                                                               | *OptionalNullable[str]*                                                                                                     | :heavy_minus_sign:                                                                                                          | New description for the guardrail                                                                                           | Updated description                                                                                                         |
| `limit_usd`                                                                                                                 | *OptionalNullable[float]*                                                                                                   | :heavy_minus_sign:                                                                                                          | New spending limit in USD                                                                                                   | 75                                                                                                                          |
| `reset_interval`                                                                                                            | [OptionalNullable[operations.UpdateGuardrailResetIntervalRequest]](../../operations/updateguardrailresetintervalrequest.md) | :heavy_minus_sign:                                                                                                          | Interval at which the limit resets (daily, weekly, monthly)                                                                 | monthly                                                                                                                     |
| `allowed_providers`                                                                                                         | List[*str*]                                                                                                                 | :heavy_minus_sign:                                                                                                          | New list of allowed provider IDs                                                                                            | [<br/>"openai",<br/>"anthropic",<br/>"deepseek"<br/>]                                                                       |
| `allowed_models`                                                                                                            | List[*str*]                                                                                                                 | :heavy_minus_sign:                                                                                                          | Array of model identifiers (slug or canonical_slug accepted)                                                                | [<br/>"openai/gpt-5.2"<br/>]                                                                                                |
| `enforce_zdr`                                                                                                               | *OptionalNullable[bool]*                                                                                                    | :heavy_minus_sign:                                                                                                          | Whether to enforce zero data retention                                                                                      | true                                                                                                                        |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |                                                                                                                             |

### Response

**[operations.UpdateGuardrailResponse](../../operations/updateguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## delete

Delete an existing guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteGuardrail" method="delete" path="/guardrails/{id}" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.delete(id="550e8400-e29b-41d4-a716-446655440000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the guardrail to delete                    | 550e8400-e29b-41d4-a716-446655440000                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.DeleteGuardrailResponse](../../operations/deleteguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list_key_assignments

List all API key guardrail assignments for the authenticated user. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="listKeyAssignments" method="get" path="/guardrails/assignments/keys" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list_key_assignments()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `offset`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Number of records to skip for pagination                            | 0                                                                   |
| `limit`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Maximum number of records to return (max 100)                       | 50                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListKeyAssignmentsResponse](../../operations/listkeyassignmentsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list_member_assignments

List all organization member guardrail assignments for the authenticated user. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="listMemberAssignments" method="get" path="/guardrails/assignments/members" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list_member_assignments()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `offset`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Number of records to skip for pagination                            | 0                                                                   |
| `limit`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Maximum number of records to return (max 100)                       | 50                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListMemberAssignmentsResponse](../../operations/listmemberassignmentsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list_guardrail_key_assignments

List all API key assignments for a specific guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGuardrailKeyAssignments" method="get" path="/guardrails/{id}/assignments/keys" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list_guardrail_key_assignments(id="550e8400-e29b-41d4-a716-446655440000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the guardrail                              | 550e8400-e29b-41d4-a716-446655440000                                |
| `offset`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Number of records to skip for pagination                            | 0                                                                   |
| `limit`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Maximum number of records to return (max 100)                       | 50                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListGuardrailKeyAssignmentsResponse](../../operations/listguardrailkeyassignmentsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## bulk_assign_keys

Assign multiple API keys to a specific guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="bulkAssignKeysToGuardrail" method="post" path="/guardrails/{id}/assignments/keys" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.bulk_assign_keys(id="550e8400-e29b-41d4-a716-446655440000", key_hashes=[
        "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the guardrail                                 | 550e8400-e29b-41d4-a716-446655440000                                   |
| `key_hashes`                                                           | List[*str*]                                                            | :heavy_check_mark:                                                     | Array of API key hashes to assign to the guardrail                     | [<br/>"c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"<br/>] |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[operations.BulkAssignKeysToGuardrailResponse](../../operations/bulkassignkeystoguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## list_guardrail_member_assignments

List all organization member assignments for a specific guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="listGuardrailMemberAssignments" method="get" path="/guardrails/{id}/assignments/members" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.list_guardrail_member_assignments(id="550e8400-e29b-41d4-a716-446655440000")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the guardrail                              | 550e8400-e29b-41d4-a716-446655440000                                |
| `offset`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Number of records to skip for pagination                            | 0                                                                   |
| `limit`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Maximum number of records to return (max 100)                       | 50                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.ListGuardrailMemberAssignmentsResponse](../../operations/listguardrailmemberassignmentsresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## bulk_assign_members

Assign multiple organization members to a specific guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="bulkAssignMembersToGuardrail" method="post" path="/guardrails/{id}/assignments/members" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.bulk_assign_members(id="550e8400-e29b-41d4-a716-446655440000", member_user_ids=[
        "user_abc123",
        "user_def456",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the guardrail                              | 550e8400-e29b-41d4-a716-446655440000                                |
| `member_user_ids`                                                   | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of member user IDs to assign to the guardrail                 | [<br/>"user_abc123",<br/>"user_def456"<br/>]                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BulkAssignMembersToGuardrailResponse](../../operations/bulkassignmemberstoguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## bulk_unassign_keys

Unassign multiple API keys from a specific guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="bulkUnassignKeysFromGuardrail" method="post" path="/guardrails/{id}/assignments/keys/remove" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.bulk_unassign_keys(id="550e8400-e29b-41d4-a716-446655440000", key_hashes=[
        "c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | The unique identifier of the guardrail                                 | 550e8400-e29b-41d4-a716-446655440000                                   |
| `key_hashes`                                                           | List[*str*]                                                            | :heavy_check_mark:                                                     | Array of API key hashes to unassign from the guardrail                 | [<br/>"c56454edb818d6b14bc0d61c46025f1450b0f4012d12304ab40aacb519fcbc93"<br/>] |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |                                                                        |

### Response

**[operations.BulkUnassignKeysFromGuardrailResponse](../../operations/bulkunassignkeysfromguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |

## bulk_unassign_members

Unassign multiple organization members from a specific guardrail. [Provisioning key](/docs/guides/overview/auth/provisioning-api-keys) required.

### Example Usage

<!-- UsageSnippet language="python" operationID="bulkUnassignMembersFromGuardrail" method="post" path="/guardrails/{id}/assignments/members/remove" -->
```python
from openrouter import OpenRouter
import os


with OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY", ""),
) as open_router:

    res = open_router.guardrails.bulk_unassign_members(id="550e8400-e29b-41d4-a716-446655440000", member_user_ids=[
        "user_abc123",
        "user_def456",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The unique identifier of the guardrail                              | 550e8400-e29b-41d4-a716-446655440000                                |
| `member_user_ids`                                                   | List[*str*]                                                         | :heavy_check_mark:                                                  | Array of member user IDs to unassign from the guardrail             | [<br/>"user_abc123",<br/>"user_def456"<br/>]                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[operations.BulkUnassignMembersFromGuardrailResponse](../../operations/bulkunassignmembersfromguardrailresponse.md)**

### Errors

| Error Type                         | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.BadRequestResponseError     | 400                                | application/json                   |
| errors.UnauthorizedResponseError   | 401                                | application/json                   |
| errors.NotFoundResponseError       | 404                                | application/json                   |
| errors.InternalServerResponseError | 500                                | application/json                   |
| errors.OpenRouterDefaultError      | 4XX, 5XX                           | \*/\*                              |