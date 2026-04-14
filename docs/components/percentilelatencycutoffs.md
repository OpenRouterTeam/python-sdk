# PercentileLatencyCutoffs

Percentile-based latency cutoffs. All specified cutoffs must be met for an endpoint to be preferred.


## Fields

| Field                         | Type                          | Required                      | Description                   |
| ----------------------------- | ----------------------------- | ----------------------------- | ----------------------------- |
| `p50`                         | *Optional[float]*             | :heavy_minus_sign:            | Maximum p50 latency (seconds) |
| `p75`                         | *Optional[float]*             | :heavy_minus_sign:            | Maximum p75 latency (seconds) |
| `p90`                         | *Optional[float]*             | :heavy_minus_sign:            | Maximum p90 latency (seconds) |
| `p99`                         | *Optional[float]*             | :heavy_minus_sign:            | Maximum p99 latency (seconds) |