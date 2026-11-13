import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Iterator, List, Tuple

import pytest

from openrouter import OpenRouter, errors
from openrouter.operations import DeleteFileRequest
from openrouter.utils.url import generate_url


class _RecordingHandler(BaseHTTPRequestHandler):
    requests: List[Tuple[str, str]] = []

    def _respond(self) -> None:
        type(self).requests.append((self.command, self.path))
        body = json.dumps({"error": {"code": 404, "message": "not found"}}).encode()
        self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    do_GET = do_DELETE = do_POST = do_PATCH = _respond

    def log_message(self, *args, **kwargs) -> None:  # pylint: disable=arguments-differ
        pass


@pytest.fixture(name="mock_server")
def fixture_mock_server() -> Iterator[str]:
    _RecordingHandler.requests = []
    server = ThreadingHTTPServer(("127.0.0.1", 0), _RecordingHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}/api/v1"
    finally:
        server.shutdown()
        server.server_close()


def _sent(mock_server: str, call) -> Tuple[str, str]:
    with OpenRouter(api_key="sk-or-v1-fake", server_url=mock_server) as client:
        with pytest.raises(errors.OpenRouterError):
            call(client)
    assert len(_RecordingHandler.requests) == 1
    return _RecordingHandler.requests[0]


def test_traversal_in_file_id_stays_on_files_download_route(mock_server: str):
    sent = _sent(mock_server, lambda c: c.files.download(file_id="../keys?x="))
    assert sent == ("GET", "/api/v1/files/..%2Fkeys%3Fx%3D/content")


def test_traversal_in_file_id_stays_on_files_delete_route(mock_server: str):
    sent = _sent(mock_server, lambda c: c.files.delete(file_id="../keys/abc"))
    assert sent == ("DELETE", "/api/v1/files/..%2Fkeys%2Fabc")


def test_normal_file_id_is_unchanged(mock_server: str):
    sent = _sent(mock_server, lambda c: c.files.download(file_id="file-abc_123.x~y"))
    assert sent == ("GET", "/api/v1/files/file-abc_123.x~y/content")


def test_spaces_unicode_and_fragment_are_percent_encoded(mock_server: str):
    sent = _sent(mock_server, lambda c: c.files.delete(file_id="my file é#frag"))
    assert sent == ("DELETE", "/api/v1/files/my%20file%20%C3%A9%23frag")


@pytest.mark.parametrize("file_id", [".", ".."])
def test_dot_segment_ids_are_rejected_before_sending(mock_server: str, file_id: str):
    with OpenRouter(api_key="sk-or-v1-fake", server_url=mock_server) as client:
        with pytest.raises(ValueError):
            client.files.delete(file_id=file_id)
    assert not _RecordingHandler.requests


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("abc", "/files/abc"),
        ("../keys", "/files/..%2Fkeys"),
        ("%2e%2e", "/files/%252e%252e"),
        ("a?b#c", "/files/a%3Fb%23c"),
    ],
)
def test_generate_url_percent_encodes_path_params(value: str, expected: str):
    url = generate_url(
        "http://127.0.0.1/api/v1/", "/files/{file_id}", DeleteFileRequest(file_id=value)
    )
    assert url == "http://127.0.0.1/api/v1" + expected
