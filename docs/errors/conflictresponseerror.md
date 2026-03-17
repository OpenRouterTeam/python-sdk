# ConflictResponseError

Conflict - Resource conflict or concurrent modification


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `error`                                                                            | [components.ConflictResponseErrorData](../components/conflictresponseerrordata.md) | :heavy_check_mark:                                                                 | Error data for ConflictResponse                                                    | {<br/>"code": 409,<br/>"message": "Resource conflict. Please try again later."<br/>} |
| `user_id`                                                                          | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                |                                                                                    |