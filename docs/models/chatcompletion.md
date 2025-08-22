# ChatCompletion

Chat completion response


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Unique completion identifier                                           |
| `choices`                                                              | List[[models.ChatCompletionChoice](../models/chatcompletionchoice.md)] | :heavy_check_mark:                                                     | List of completion choices                                             |
| `created`                                                              | *float*                                                                | :heavy_check_mark:                                                     | Unix timestamp of creation                                             |
| `model`                                                                | *str*                                                                  | :heavy_check_mark:                                                     | Model used for completion                                              |
| `object`                                                               | [models.ChatCompletionObject](../models/chatcompletionobject.md)       | :heavy_check_mark:                                                     | N/A                                                                    |
| `system_fingerprint`                                                   | *OptionalNullable[str]*                                                | :heavy_minus_sign:                                                     | System fingerprint                                                     |
| `usage`                                                                | [Optional[models.CompletionUsage]](../models/completionusage.md)       | :heavy_minus_sign:                                                     | Token usage statistics                                                 |