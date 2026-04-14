# PercentileThroughputCutoffs

Percentile-based throughput cutoffs. All specified cutoffs must be met for an endpoint to be preferred.


## Fields

| Field                               | Type                                | Required                            | Description                         |
| ----------------------------------- | ----------------------------------- | ----------------------------------- | ----------------------------------- |
| `p50`                               | *Optional[float]*                   | :heavy_minus_sign:                  | Minimum p50 throughput (tokens/sec) |
| `p75`                               | *Optional[float]*                   | :heavy_minus_sign:                  | Minimum p75 throughput (tokens/sec) |
| `p90`                               | *Optional[float]*                   | :heavy_minus_sign:                  | Minimum p90 throughput (tokens/sec) |
| `p99`                               | *Optional[float]*                   | :heavy_minus_sign:                  | Minimum p99 throughput (tokens/sec) |