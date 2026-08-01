import json
import os
import subprocess
import sys
from pathlib import Path

SRC = str(Path(__file__).resolve().parents[1] / "src")

PROBE = """
import json, logging, sys
{setup}
root = logging.getLogger()
before = (root.level, len(root.handlers))

from openrouter import OpenRouter
OpenRouter(api_key="x")
OpenRouter(api_key="x")  # twice: handlers must not stack

sdk = logging.getLogger("openrouter")
print(json.dumps({{
    "root_before": before,
    "root_after": (root.level, len(root.handlers)),
    "sdk_level": sdk.level,
    "sdk_handlers": len(sdk.handlers),
}}))
"""


def _probe(setup="", **env):
    """Run a fresh interpreter: logging config is process-global."""
    out = subprocess.run(
        [sys.executable, "-c", PROBE.format(setup=setup)],
        capture_output=True,
        text=True,
        check=True,
        env={**os.environ, "PYTHONPATH": SRC, **env},
    ).stdout
    return json.loads(out.strip().splitlines()[-1])


def test_debug_mode_leaves_the_root_logger_alone():
    r = _probe(OPENROUTER_DEBUG="1")

    # basicConfig used to set root to DEBUG and attach a StreamHandler to it.
    assert r["root_after"] == r["root_before"]
    assert r["root_after"] == [30, 0]  # WARNING, no handlers

    # The SDK's own logger is what gets configured.
    assert r["sdk_level"] == 10  # DEBUG
    assert r["sdk_handlers"] == 1  # not 2 — repeated construction must not stack


def test_no_logging_is_touched_without_the_env_var():
    r = _probe()

    assert r["root_after"] == r["root_before"]
    assert r["sdk_level"] == 0  # NOTSET
    assert r["sdk_handlers"] == 0


def test_an_application_handler_is_not_duplicated():
    r = _probe(
        setup="logging.basicConfig(level=logging.INFO)",
        OPENROUTER_DEBUG="1",
    )

    # The app configured root itself; we must not add a competing handler,
    # which would print every record twice.
    assert r["sdk_handlers"] == 0
    assert r["sdk_level"] == 10
    assert r["root_after"] == r["root_before"]
