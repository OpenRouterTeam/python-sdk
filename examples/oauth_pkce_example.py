"""
Example of using OAuth PKCE helper functions

This example demonstrates how to:
1. Generate a SHA-256 code challenge and verifier
2. Create an authorization URL for OAuth flow
"""

from openrouter import OpenRouter
from openrouter.utils import (
    oauth_create_sha256_code_challenge,
    oauth_create_authorization_url,
    CreateSHA256CodeChallengeRequest,
    CreateAuthorizationUrlRequestWithPKCE,
)


def main():
    # Step 1: Generate a code challenge and verifier
    # You can optionally provide your own code_verifier, or let it generate one
    result = oauth_create_sha256_code_challenge()

    print("Code Challenge:", result.code_challenge)
    print("Code Verifier:", result.code_verifier)
    print()

    # Or provide your own code verifier (must be 43-128 chars, [A-Za-z0-9-._~])
    custom_result = oauth_create_sha256_code_challenge(
        CreateSHA256CodeChallengeRequest(
            code_verifier="my-custom-verifier-that-is-at-least-43-characters-long-abcdefghij"
        )
    )
    print("Custom Code Challenge:", custom_result.code_challenge)
    print("Custom Code Verifier:", custom_result.code_verifier)
    print()

    # Step 2: Create an authorization URL
    client = OpenRouter(api_key="your-api-key")

    # Create authorization URL with PKCE
    auth_url = oauth_create_authorization_url(
        client,
        CreateAuthorizationUrlRequestWithPKCE(
            callback_url="https://your-app.com/callback",
            code_challenge=result.code_challenge,
            code_challenge_method="S256",
            limit=10.0,  # Optional credit limit
        )
    )

    print("Authorization URL:", auth_url)
    print()

    # Step 3: User would visit the authorization URL and authorize the app
    # Step 4: After authorization, the callback URL receives an authorization code
    # Step 5: Exchange the code for an API key using the SDK's exchange method
    # code = "authorization-code-from-callback"
    # api_key_response = client.o_auth.exchange_auth_code_for_api_key(
    #     code=code,
    #     code_verifier=result.code_verifier,
    #     code_challenge_method="S256",
    # )
    # print("API Key:", api_key_response.key)


if __name__ == "__main__":
    main()
