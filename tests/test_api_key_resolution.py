import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from openrouter import OpenRouter


@pytest.fixture(name="server")
def _server():
    """A stub API that records the Authorization header it was sent."""
    received = []

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 - name fixed by BaseHTTPRequestHandler
            received.append(self.headers.get("authorization"))
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"data": 0}')

        def log_message(self, *args):
            pass

    httpd = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    try:
        yield f"http://127.0.0.1:{httpd.server_address[1]}", received
    finally:
        httpd.shutdown()


def _authorization(url, received, **kwargs):
    try:
        OpenRouter(server_url=url, **kwargs).models.count()
    except Exception:  # the stub body does not satisfy the response schema
        pass
    assert received, "no request reached the server"
    return received.pop()


def test_env_var_is_used_when_no_api_key_is_passed(server, monkeypatch):
    url, received = server
    monkeypatch.setenv("OPENROUTER_API_KEY", "from-env")

    assert _authorization(url, received) == "Bearer from-env"


def test_explicit_api_key_wins_over_the_env_var(server, monkeypatch):
    url, received = server
    monkeypatch.setenv("OPENROUTER_API_KEY", "from-env")

    assert _authorization(url, received, api_key="explicit") == "Bearer explicit"


def test_blank_api_key_falls_back_to_the_env_var(server, monkeypatch):
    # The documented pattern api_key=os.getenv("OPENROUTER_API_KEY", "") produces
    # "" when the variable is unset. It used to short-circuit the fallback and
    # fail in httpx with LocalProtocolError: Illegal header value b'Bearer '.
    url, received = server
    monkeypatch.setenv("OPENROUTER_API_KEY", "from-env")

    assert _authorization(url, received, api_key="") == "Bearer from-env"
    assert _authorization(url, received, api_key="   ") == "Bearer from-env"


def test_no_credentials_anywhere_sends_no_authorization_header(server, monkeypatch):
    url, received = server
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)

    assert _authorization(url, received) is None
    assert _authorization(url, received, api_key="") is None


def test_callable_api_key_is_still_resolved_per_request(server, monkeypatch):
    url, received = server
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    keys = iter(["first", "second"])

    client = OpenRouter(server_url=url, api_key=lambda: next(keys))
    for expected in ["Bearer first", "Bearer second"]:
        try:
            client.models.count()
        except Exception:
            pass
        assert received.pop() == expected
