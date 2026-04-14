# Architecture

Model architecture information


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `input_modalities`                                                 | List[[components.InputModality](../components/inputmodality.md)]   | :heavy_check_mark:                                                 | Supported input modalities                                         |                                                                    |
| `instruct_type`                                                    | [Nullable[components.InstructType]](../components/instructtype.md) | :heavy_check_mark:                                                 | Instruction format type                                            | chatml                                                             |
| `modality`                                                         | *Nullable[str]*                                                    | :heavy_check_mark:                                                 | Primary modality of the model                                      | text                                                               |
| `output_modalities`                                                | List[[components.OutputModality](../components/outputmodality.md)] | :heavy_check_mark:                                                 | Supported output modalities                                        |                                                                    |
| `tokenizer`                                                        | [Nullable[components.Tokenizer]](../components/tokenizer.md)       | :heavy_check_mark:                                                 | N/A                                                                | GPT                                                                |