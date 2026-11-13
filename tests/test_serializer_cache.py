import json

import httpx

from openrouter import OpenRouter
from openrouter._hooks import serializer_cache
from openrouter.utils import serializers

COMPLETION = {
    "id": "gen-test",
    "object": "chat.completion",
    "created": 1760000000,
    "model": "openai/gpt-4o-mini",
    "system_fingerprint": None,
    "choices": [
        {
            "index": 0,
            "finish_reason": "stop",
            "message": {"role": "assistant", "content": "ok"},
        }
    ],
    "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2},
}


def _client() -> OpenRouter:
    transport = httpx.MockTransport(
        lambda request: httpx.Response(200, json=COMPLETION)
    )
    return OpenRouter(api_key="test-key", client=httpx.Client(transport=transport))


def _send(client: OpenRouter):
    return client.chat.send(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": "hi"}],
    )


def test_sdk_init_installs_serializer_cache():
    _client()

    assert serializers.create_model is serializer_cache._create_model


def test_repeated_requests_reuse_serializer_models(monkeypatch):
    built = []
    uncached_create_model = serializer_cache._uncached_create_model

    def counting_create_model(*args, **kwargs):
        built.append(args[0] if args else kwargs.get("__model_name"))
        return uncached_create_model(*args, **kwargs)

    client = _client()
    serializer_cache._cached_wrapper_model.cache_clear()
    monkeypatch.setattr(serializer_cache, "_uncached_create_model", counting_create_model)

    first = _send(client)
    built_by_first_request = len(built)
    second = _send(client)

    assert built_by_first_request > 0
    assert len(built) == built_by_first_request
    assert first.choices[0].message.content == "ok"
    assert second.model_dump() == first.model_dump()


def test_cached_models_serialize_like_uncached_ones():
    _client()

    value = {"a": [1, 2]}
    typ = dict[str, list[int]]

    assert json.loads(serializers.marshal_json(value, typ)) == value
    assert serializers.unmarshal(value, typ) == value
    assert serializers.unmarshal(value, typ) == value
