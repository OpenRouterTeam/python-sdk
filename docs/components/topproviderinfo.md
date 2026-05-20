# TopProviderInfo

Information about the top provider for this model


## Fields

| Field                                           | Type                                            | Required                                        | Description                                     | Example                                         |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| `context_length`                                | *OptionalNullable[int]*                         | :heavy_minus_sign:                              | Context length from the top provider            | 8192                                            |
| `is_moderated`                                  | *bool*                                          | :heavy_check_mark:                              | Whether the top provider moderates content      | true                                            |
| `max_completion_tokens`                         | *OptionalNullable[int]*                         | :heavy_minus_sign:                              | Maximum completion tokens from the top provider | 4096                                            |