# Run SDK examples with uv

This guide explains how to create and activate a Python virtual environment on macOS, install necessary dependencies, and run the `.py` scripts.

## Steps to Set Up and Run the Script

### Prerequisites

- [Install uv](https://docs.astral.sh/uv/getting-started/installation/#pypi)


### Configure auth

- Rename .env.template to .env and populate the .env file with your client ID and secret

```bash
OPENROUTER_API_KEY=""
```

### Run the script with the .env values

```bash
 cd examples/
 uv run --env-file=.env script.py
```
