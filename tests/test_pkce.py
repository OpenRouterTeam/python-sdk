import base64
import hashlib

import pytest

from openrouter import OpenRouter
from openrouter.pkce import (
    CreateAuthorizationUrlRequestBase,
    CreateAuthorizationUrlRequestWithPKCE,
    CreateSHA256CodeChallengeRequest,
    oauth_create_authorization_url,
    oauth_create_sha256_code_challenge,
)


def test_generated_verifier_is_a_valid_challenge_pair():
    res = oauth_create_sha256_code_challenge()

    assert len(res.code_verifier) == 43
    expected = base64.urlsafe_b64encode(
        hashlib.sha256(res.code_verifier.encode()).digest()
    ).rstrip(b"=")
    assert res.code_challenge == expected.decode()
    assert "=" not in res.code_challenge


def test_supplied_verifier_is_validated_per_rfc7636():
    ok = "a" * 43
    assert oauth_create_sha256_code_challenge(
        CreateSHA256CodeChallengeRequest(code_verifier=ok)
    ).code_verifier == ok

    for bad in ["a" * 42, "a" * 129, "a" * 42 + "!"]:
        with pytest.raises(ValueError):
            oauth_create_sha256_code_challenge(
                CreateSHA256CodeChallengeRequest(code_verifier=bad)
            )


def test_authorization_url_points_at_the_site_root_not_the_api_base():
    # https://openrouter.ai/api/v1/auth is a 404; the auth page is on the origin.
    url = oauth_create_authorization_url(
        OpenRouter(api_key="x"),
        CreateAuthorizationUrlRequestBase(callback_url="https://app.example/cb"),
    )

    assert url.startswith("https://openrouter.ai/auth?")
    assert "/api/v1/" not in url
    assert "callback_url=https%3A%2F%2Fapp.example%2Fcb" in url


def test_authorization_url_honors_custom_server_url():
    url = oauth_create_authorization_url(
        OpenRouter(api_key="x", server_url="https://eu.openrouter.ai/api/v1"),
        CreateAuthorizationUrlRequestBase(callback_url="https://app.example/cb"),
    )

    assert url.startswith("https://eu.openrouter.ai/auth?")


def test_authorization_url_carries_pkce_and_limit():
    url = oauth_create_authorization_url(
        OpenRouter(api_key="x"),
        CreateAuthorizationUrlRequestWithPKCE(
            callback_url="https://app.example/cb",
            code_challenge="challenge",
            code_challenge_method="S256",
            limit=10.0,
        ),
    )

    assert "code_challenge=challenge" in url
    assert "code_challenge_method=S256" in url
    assert "limit=10.0" in url


def test_parse_result_callback_url_renders_as_a_url():
    # str() on a ParseResult yields its repr, which would corrupt the query param.
    from urllib.parse import urlparse

    url = oauth_create_authorization_url(
        OpenRouter(api_key="x"),
        CreateAuthorizationUrlRequestBase(
            callback_url=urlparse("https://app.example/cb")
        ),
    )

    assert "callback_url=https%3A%2F%2Fapp.example%2Fcb" in url
    assert "ParseResult" not in url
