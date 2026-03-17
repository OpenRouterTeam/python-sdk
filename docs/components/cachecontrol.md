# CacheControl

Enable automatic prompt caching. When set, the system automatically applies cache breakpoints to the last cacheable block in the request. Currently supported for Anthropic Claude models.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `type`                                                                                   | [components.ChatGenerationParamsType](../components/chatgenerationparamstype.md)         | :heavy_check_mark:                                                                       | N/A                                                                                      |
| `ttl`                                                                                    | [Optional[components.ChatGenerationParamsTTL]](../components/chatgenerationparamsttl.md) | :heavy_minus_sign:                                                                       | N/A                                                                                      |