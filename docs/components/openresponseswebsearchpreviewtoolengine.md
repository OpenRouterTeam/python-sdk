# OpenResponsesWebSearchPreviewToolEngine

Which search engine to use. "auto" (default) uses native if the provider supports it, otherwise Exa. "native" forces the provider's built-in search (parameters like max_results, search_context_size, and domain filters are not forwarded to the provider). "exa" forces the Exa search API.


## Values

| Name     | Value    |
| -------- | -------- |
| `AUTO`   | auto     |
| `NATIVE` | native   |
| `EXA`    | exa      |