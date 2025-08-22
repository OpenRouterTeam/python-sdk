#!/bin/bash

# Install the speakeasy CLI
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | sh

# Setup samples directory
rmdir samples || true
mkdir samples


uv sync --dev

# Generate starter usage sample with speakeasy
speakeasy generate usage -s .speakeasy/out.openapi.yaml -l python -o samples/root.py