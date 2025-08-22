# ChatCompletionTokenLogprob

Token log probability information


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `token`                                            | *str*                                              | :heavy_check_mark:                                 | The token                                          |
| `logprob`                                          | *float*                                            | :heavy_check_mark:                                 | Log probability of the token                       |
| `bytes_`                                           | List[*float*]                                      | :heavy_check_mark:                                 | UTF-8 bytes of the token                           |
| `top_logprobs`                                     | List[[models.TopLogprob](../models/toplogprob.md)] | :heavy_check_mark:                                 | Top alternative tokens with probabilities          |