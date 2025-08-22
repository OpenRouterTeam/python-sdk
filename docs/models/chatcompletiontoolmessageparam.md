# ChatCompletionToolMessageParam

Tool response message


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `role`                                                                                             | [models.ChatCompletionToolMessageParamRole](../models/chatcompletiontoolmessageparamrole.md)       | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `content`                                                                                          | [models.ChatCompletionToolMessageParamContent](../models/chatcompletiontoolmessageparamcontent.md) | :heavy_check_mark:                                                                                 | Tool response content                                                                              |
| `tool_call_id`                                                                                     | *str*                                                                                              | :heavy_check_mark:                                                                                 | ID of the tool call this message responds to                                                       |