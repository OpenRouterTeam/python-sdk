from openrouter import OpenRouter


def test_responses_namespace_is_ga_and_beta_alias_remains_available():
    client = OpenRouter(api_key="test-key")

    assert client.responses is not None
    assert client.beta.responses is not None
    assert type(client.responses) is type(client.beta.responses)
    assert client.beta.analytics is not None
