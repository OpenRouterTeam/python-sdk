# Chat
(*chat*)

## Overview

### Available Operations

* [complete](#complete) - Create a chat completion

## complete

Creates a model response for the given chat conversation. Supports both streaming and non-streaming modes.

### Example Usage

<!-- UsageSnippet language="python" operationID="createChatCompletion" method="post" path="/chat/completions" -->
```python
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

    with res as event_stream:
        for event in event_stream:
            # handle event
            print(event, flush=True)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `messages`                                                                                        | List[[models.ChatCompletionMessageParam](../../models/chatcompletionmessageparam.md)]             | :heavy_check_mark:                                                                                | List of messages for the conversation                                                             | [<br/>{<br/>"role": "user",<br/>"content": "Hello, how are you?"<br/>}<br/>]                      |
| `model`                                                                                           | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Model to use for completion                                                                       |                                                                                                   |
| `frequency_penalty`                                                                               | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Frequency penalty (-2.0 to 2.0)                                                                   |                                                                                                   |
| `logit_bias`                                                                                      | Dict[str, *float*]                                                                                | :heavy_minus_sign:                                                                                | Token logit bias adjustments                                                                      |                                                                                                   |
| `logprobs`                                                                                        | *OptionalNullable[bool]*                                                                          | :heavy_minus_sign:                                                                                | Return log probabilities                                                                          |                                                                                                   |
| `top_logprobs`                                                                                    | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Number of top log probabilities to return (0-20)                                                  |                                                                                                   |
| `max_completion_tokens`                                                                           | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Maximum tokens in completion                                                                      |                                                                                                   |
| `max_tokens`                                                                                      | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Maximum tokens (deprecated, use max_completion_tokens)                                            |                                                                                                   |
| `metadata`                                                                                        | Dict[str, *str*]                                                                                  | :heavy_minus_sign:                                                                                | Key-value pairs for additional object information (max 16 pairs, 64 char keys, 512 char values)   |                                                                                                   |
| `presence_penalty`                                                                                | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Presence penalty (-2.0 to 2.0)                                                                    |                                                                                                   |
| `reasoning`                                                                                       | [OptionalNullable[models.Reasoning]](../../models/reasoning.md)                                   | :heavy_minus_sign:                                                                                | Reasoning configuration                                                                           |                                                                                                   |
| `response_format`                                                                                 | [Optional[models.ResponseFormat]](../../models/responseformat.md)                                 | :heavy_minus_sign:                                                                                | Response format configuration                                                                     |                                                                                                   |
| `seed`                                                                                            | *OptionalNullable[int]*                                                                           | :heavy_minus_sign:                                                                                | Random seed for deterministic outputs                                                             |                                                                                                   |
| `stop`                                                                                            | [OptionalNullable[models.Stop]](../../models/stop.md)                                             | :heavy_minus_sign:                                                                                | Stop sequences (up to 4)                                                                          |                                                                                                   |
| `stream`                                                                                          | *OptionalNullable[bool]*                                                                          | :heavy_minus_sign:                                                                                | Enable streaming response                                                                         |                                                                                                   |
| `stream_options`                                                                                  | [OptionalNullable[models.StreamOptions]](../../models/streamoptions.md)                           | :heavy_minus_sign:                                                                                | N/A                                                                                               |                                                                                                   |
| `temperature`                                                                                     | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Sampling temperature (0-2)                                                                        |                                                                                                   |
| `tool_choice`                                                                                     | [Optional[models.ChatCompletionToolChoiceOption]](../../models/chatcompletiontoolchoiceoption.md) | :heavy_minus_sign:                                                                                | Tool choice configuration                                                                         |                                                                                                   |
| `tools`                                                                                           | List[[models.ChatCompletionTool](../../models/chatcompletiontool.md)]                             | :heavy_minus_sign:                                                                                | Available tools for function calling                                                              |                                                                                                   |
| `top_p`                                                                                           | *OptionalNullable[float]*                                                                         | :heavy_minus_sign:                                                                                | Nucleus sampling parameter (0-1)                                                                  |                                                                                                   |
| `user`                                                                                            | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | Unique user identifier                                                                            |                                                                                                   |
| `fallback_models`                                                                                 | List[*str*]                                                                                       | :heavy_minus_sign:                                                                                | Order of models to fallback to for this request                                                   |                                                                                                   |
| `reasoning_effort`                                                                                | [OptionalNullable[models.ReasoningEffort]](../../models/reasoningeffort.md)                       | :heavy_minus_sign:                                                                                | Reasoning effort                                                                                  |                                                                                                   |
| `provider`                                                                                        | [OptionalNullable[models.Provider]](../../models/provider.md)                                     | :heavy_minus_sign:                                                                                | When multiple model providers are available, optionally indicate your routing preference.         |                                                                                                   |
| `plugins`                                                                                         | List[[models.Plugin](../../models/plugin.md)]                                                     | :heavy_minus_sign:                                                                                | Plugins you want to enable for this request, including their settings.                            |                                                                                                   |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |                                                                                                   |

### Response

**[models.CreateChatCompletionResponse](../../models/createchatcompletionresponse.md)**

### Errors

| Error Type                    | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.ChatCompletionError    | 400, 401, 429                 | application/json              |
| errors.ChatCompletionError    | 500                           | application/json              |
| errors.OpenRouterDefaultError | 4XX, 5XX                      | \*/\*                         |