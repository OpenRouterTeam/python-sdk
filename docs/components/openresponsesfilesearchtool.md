# OpenResponsesFileSearchTool

File search tool configuration


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `type`                                                                 | [components.TypeFileSearch](../components/typefilesearch.md)           | :heavy_check_mark:                                                     | N/A                                                                    |
| `vector_store_ids`                                                     | List[*str*]                                                            | :heavy_check_mark:                                                     | N/A                                                                    |
| `filters`                                                              | [OptionalNullable[components.Filters]](../components/filters.md)       | :heavy_minus_sign:                                                     | N/A                                                                    |
| `max_num_results`                                                      | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | N/A                                                                    |
| `ranking_options`                                                      | [Optional[components.RankingOptions]](../components/rankingoptions.md) | :heavy_minus_sign:                                                     | N/A                                                                    |