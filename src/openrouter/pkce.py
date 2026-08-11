"""OAuth PKCE helpers.

Hand-written, not generated. Kept out of the generated tree and listed in
`.genignore` so a regeneration cannot delete it — that is exactly how the
previous version of these helpers was lost (added in 05f81a5, removed as
collateral damage by the regen in e6b0242, which left examples/ importing
symbols that no longer existed).

See https://openrouter.ai/docs/use-cases/oauth-pkce and RFC 7636.
"""

import base64
import hashlib
import re
import secrets
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Optional, Union
from urllib.parse import ParseResult, urlencode, urlsplit, urlunsplit

if TYPE_CHECKING:
    from openrouter.sdk import OpenRouter


@dataclass
class CreateSHA256CodeChallengeRequest:
    """Parameters for creating a SHA-256 code challenge.

    If `code_verifier` is omitted a random one is generated. If supplied it must
    be 43-128 characters of unreserved characters `[A-Za-z0-9-._~]` per RFC 7636.
    """

    code_verifier: Optional[str] = None


@dataclass
class CreateSHA256CodeChallengeResponse:
    """The generated code challenge and the verifier it was derived from."""

    code_challenge: str
    code_verifier: str


@dataclass
class CreateAuthorizationUrlRequestBase:
    """Authorization URL parameters without PKCE."""

    callback_url: Union[str, ParseResult]
    limit: Optional[float] = None


@dataclass
class CreateAuthorizationUrlRequestWithPKCE:
    """Authorization URL parameters with PKCE."""

    callback_url: Union[str, ParseResult]
    code_challenge_method: Literal["S256", "plain"]
    code_challenge: str
    limit: Optional[float] = None


CreateAuthorizationUrlRequest = Union[
    CreateAuthorizationUrlRequestWithPKCE,
    CreateAuthorizationUrlRequestBase,
]


def _b64url(data: bytes) -> str:
    """Base64url-encode without padding (RFC 4648 §5)."""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def _generate_code_verifier() -> str:
    """Generate a random code verifier: 32 octets base64url-encoded = 43 chars."""
    return _b64url(secrets.token_bytes(32))


def _validate_code_verifier(code_verifier: str) -> None:
    """Raise ValueError if `code_verifier` does not satisfy RFC 7636 §4.1."""
    if len(code_verifier) < 43:
        raise ValueError("Code verifier must be at least 43 characters")
    if len(code_verifier) > 128:
        raise ValueError("Code verifier must be at most 128 characters")
    if not re.match(r"^[A-Za-z0-9\-._~]+$", code_verifier):
        raise ValueError(
            "Code verifier must only contain unreserved characters: [A-Za-z0-9-._~]"
        )


def _as_url(value: Union[str, ParseResult]) -> str:
    """Render a URL. `str()` on a ParseResult yields its repr, not the URL."""
    return value.geturl() if isinstance(value, ParseResult) else value


def _get_site_origin(client: "OpenRouter") -> str:
    """Derive the site origin from the configured API server URL.

    The authorization page lives on the site root (`https://openrouter.ai/auth`),
    not under the API base path — `https://openrouter.ai/api/v1/auth` is a 404.
    Deriving from the configured server URL keeps regional hosts such as
    `eu.openrouter.ai` and custom base URLs working.
    """
    server_url, _ = client.sdk_configuration.get_server_details()
    if not server_url:
        raise ValueError("No server URL configured")

    parts = urlsplit(server_url)
    if not parts.scheme or not parts.netloc:
        raise ValueError(f"Cannot derive an authorization URL from {server_url!r}")

    return urlunsplit((parts.scheme, parts.netloc, "", "", ""))


def oauth_create_sha256_code_challenge(
    params: Optional[CreateSHA256CodeChallengeRequest] = None,
) -> CreateSHA256CodeChallengeResponse:
    """Generate a SHA-256 code challenge and its code verifier for PKCE.

    Args:
        params: Optional parameters. A random verifier is generated when omitted.

    Returns:
        The code challenge and the verifier it was derived from. Keep the
        verifier; it is required to exchange the auth code for an API key.

    Raises:
        ValueError: If a supplied code verifier is invalid.
    """
    if params is None:
        params = CreateSHA256CodeChallengeRequest()

    code_verifier = params.code_verifier
    if code_verifier is None:
        code_verifier = _generate_code_verifier()
    else:
        _validate_code_verifier(code_verifier)

    digest = hashlib.sha256(code_verifier.encode("utf-8")).digest()

    return CreateSHA256CodeChallengeResponse(
        code_challenge=_b64url(digest),
        code_verifier=code_verifier,
    )


def oauth_create_authorization_url(
    client: "OpenRouter",
    params: CreateAuthorizationUrlRequest,
) -> str:
    """Build the URL to redirect users to in order to authorize your app.

    Args:
        client: An OpenRouter client; its server URL determines the host.
        params: Callback URL, optional credit limit, and optional PKCE challenge.

    Returns:
        The authorization URL.

    Raises:
        ValueError: If the client has no usable server URL configured.
    """
    query = {"callback_url": _as_url(params.callback_url)}

    if isinstance(params, CreateAuthorizationUrlRequestWithPKCE):
        query["code_challenge"] = params.code_challenge
        query["code_challenge_method"] = params.code_challenge_method

    if params.limit is not None:
        query["limit"] = str(params.limit)

    return f"{_get_site_origin(client)}/auth?{urlencode(query)}"
