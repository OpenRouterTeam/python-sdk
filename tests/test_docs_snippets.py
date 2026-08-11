import ast
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SNIPPET = re.compile(r"```python\n(.*?)```", re.S)


def _snippets():
    """Every documented snippet that actually uses the SDK.

    Blocks under docs/components/ and docs/operations/ are type signatures rather
    than programs, so only blocks that import from `openrouter` are collected.
    """
    files = [ROOT / "README.md", ROOT / "README-PYPI.md", ROOT / "USAGE.md"]
    files += sorted(ROOT.glob("docs/**/*.mdx"))

    found = []
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in SNIPPET.finditer(text):
            code = match.group(1)
            if "from openrouter" in code or "import openrouter" in code:
                line = text[: match.start()].count("\n") + 1
                found.append(
                    pytest.param(code, id=f"{path.relative_to(ROOT).as_posix()}:{line}")
                )
    return found


@pytest.mark.parametrize("code", _snippets())
def test_documented_snippet_is_valid_python(code):
    # The README's Resource Management block is generated between Speakeasy
    # section markers, so a regeneration can silently reintroduce the empty
    # `with` bodies this guards against.
    ast.parse(code)


def test_snippet_collection_is_not_empty():
    assert len(_snippets()) > 100
