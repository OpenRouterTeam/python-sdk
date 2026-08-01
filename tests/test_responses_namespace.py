from openrouter import OpenRouter


def _public_operations(namespace):
    return {name for name in dir(namespace) if not name.startswith("_")}


def test_responses_namespace_is_ga_and_beta_alias_remains_available():
    client = OpenRouter(api_key="test-key")

    assert client.responses is not None
    assert client.beta.responses is not None
    assert client.beta.analytics is not None

    # The alias is generated as its own class (BetaResponses), so identity no
    # longer holds — what has to stay true is that it exposes the same surface.
    operations = _public_operations(client.responses)
    assert {"send", "send_async"} <= operations
    assert _public_operations(client.beta.responses) == operations

    # deprecated-beta-responses-alias.overlay.yaml adds the tag description that
    # becomes this docstring. Its own comments warn that the overlay can silently
    # match nothing after a monorepo sync and drop the notice, so assert on it.
    assert "deprecated" in (type(client.beta.responses).__doc__ or "").lower()
