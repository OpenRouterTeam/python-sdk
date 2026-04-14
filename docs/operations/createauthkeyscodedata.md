# CreateAuthKeysCodeData

Auth code data


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `app_id`                                                 | *int*                                                    | :heavy_check_mark:                                       | The application ID associated with this auth code        | 12345                                                    |
| `created_at`                                             | *str*                                                    | :heavy_check_mark:                                       | ISO 8601 timestamp of when the auth code was created     | 2025-08-24T10:30:00Z                                     |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | The authorization code ID to use in the exchange request | auth_code_xyz789                                         |