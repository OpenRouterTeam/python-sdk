from openrouter import OpenRouter


def _public_methods(obj):
    return {name for name in dir(obj) if not name.startswith("_") and callable(getattr(obj, name))}


def test_responses_namespace_is_ga_and_beta_alias_remains_available():
    client = OpenRouter(api_key="test-key")

    assert client.responses is not None
    assert client.beta.responses is not None
    assert _public_methods(client.responses) == _public_methods(client.beta.responses)
    assert client.analytics is not None
