# CreateEmbeddingsData

A single embedding object


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `embedding`                                                    | [operations.Embedding](../operations/embedding.md)             | :heavy_check_mark:                                             | Embedding vector as an array of floats or a base64 string      | [<br/>0.0023064255,<br/>-0.009327292,<br/>0.015797347<br/>]    |
| `index`                                                        | *Optional[int]*                                                | :heavy_minus_sign:                                             | Index of the embedding in the input list                       | 0                                                              |
| `object`                                                       | [operations.ObjectEmbedding](../operations/objectembedding.md) | :heavy_check_mark:                                             | N/A                                                            |                                                                |