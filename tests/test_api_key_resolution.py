import httpx
import pytest

from openrouter import OpenRouter


def _authorization_header(**kwargs):
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.headers.get("authorization"))
        return httpx.Response(200, json={"data": {"count": 0}})

    client = httpx.Client(transport=httpx.MockTransport(handler))
    try:
        OpenRouter(client=client, **kwargs).models.count()
    except Exception:  # pylint: disable=broad-except
        pass  # response shape is irrelevant; only the request header matters
    assert seen, "no request was sent"
    return seen[0]


@pytest.mark.parametrize("api_key", ["", "   "])
def test_blank_api_key_falls_back_to_env_var(monkeypatch, api_key):
    monkeypatch.setenv("OPENROUTER_API_KEY", "from-env")
    assert _authorization_header(api_key=api_key) == "Bearer from-env"


def test_blank_api_key_without_env_var_sends_no_authorization(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert _authorization_header(api_key="") is None


@pytest.mark.parametrize("env_value", ["", "   "])
def test_blank_api_key_and_blank_env_var_sends_no_authorization(
    monkeypatch, env_value
):
    monkeypatch.setenv("OPENROUTER_API_KEY", env_value)
    assert _authorization_header(api_key="") is None


def test_blank_callable_api_key_falls_back_to_env_var(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "from-env")
    assert _authorization_header(api_key=lambda: "") == "Bearer from-env"


def test_explicit_api_key_wins_over_env_var(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "from-env")
    assert _authorization_header(api_key="explicit") == "Bearer explicit"
