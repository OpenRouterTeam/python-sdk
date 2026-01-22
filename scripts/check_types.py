#!/usr/bin/env python3
"""
Check if model types are stale.

This script is intended to be run as a postinstall hook to warn users
when their generated types are outdated (similar to update-browserslist-db).

It compares the MODEL_HASH in the generated types file with a freshly
computed hash from the OpenRouter API.

Exit codes:
- 0: Types are up to date OR check was skipped (CI, disabled, errors)
- Does NOT fail on stale types to avoid breaking installs
"""

import hashlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

API_URL = "https://openrouter.ai/api/v1/models"
TIMEOUT_SECONDS = 5


def compute_hash(model_ids: list[str]) -> str:
    """Compute SHA-256 hash of sorted model IDs (first 16 chars)."""
    sorted_ids = sorted(model_ids)
    content = "\n".join(sorted_ids)
    hash_obj = hashlib.sha256(content.encode())
    return hash_obj.hexdigest()[:16]


def extract_hash(content: str) -> str | None:
    """Extract MODEL_HASH from types file content."""
    match = re.search(r"MODEL_HASH: str = '([a-f0-9]+)'", content)
    return match.group(1) if match else None


def fetch_models() -> list[str]:
    """Fetch model IDs from OpenRouter API."""
    request = urllib.request.Request(API_URL)
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        data = json.loads(response.read().decode())
        return [model["id"] for model in data["data"]]


def main() -> None:
    # Skip in CI environments
    if os.environ.get("CI"):
        return

    # Skip if explicitly disabled
    if os.environ.get("OPENROUTER_SKIP_TYPE_CHECK"):
        return

    try:
        # Find the types file
        script_dir = Path(__file__).parent
        types_file = script_dir.parent / "src" / "openrouter" / "types" / "models.py"

        # Read existing hash
        try:
            content = types_file.read_text()
            existing_hash = extract_hash(content)
        except FileNotFoundError:
            # Types file doesn't exist - expected for fresh installs
            return

        if not existing_hash:
            # No hash found - unusual, but don't warn
            return

        # Fetch current models and compute hash
        model_ids = fetch_models()
        current_hash = compute_hash(model_ids)

        # Compare hashes
        if existing_hash != current_hash:
            print(
                "\n\033[33m"  # Yellow color
                "OpenRouter model types are outdated.\n"
                "Run: npx @openrouter/cli types\n"
                "\033[0m",  # Reset color
                file=sys.stderr,
            )

    except Exception:
        # Silently ignore errors - don't break installs
        # Network errors, timeouts, etc. are expected in some environments
        pass


if __name__ == "__main__":
    main()
