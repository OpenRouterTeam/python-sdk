# ChatCompletionToolFunction

Function definition for tool calling


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | Function name (a-z, A-Z, 0-9, underscores, dashes, max 64 chars) |
| `description`                                                    | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Function description for the model                               |
| `parameters`                                                     | [Optional[models.Parameters]](../models/parameters.md)           | :heavy_minus_sign:                                               | Function parameters as JSON Schema object                        |
| `strict`                                                         | *OptionalNullable[bool]*                                         | :heavy_minus_sign:                                               | Enable strict schema adherence                                   |