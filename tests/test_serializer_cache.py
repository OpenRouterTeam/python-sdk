from typing import Annotated, List, Literal, Optional, Union

import httpx
import pydantic
import pytest

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


def _uncached(monkeypatch):
    monkeypatch.setattr(
        serializers, "create_model", serializer_cache._uncached_create_model
    )


def _outcome(fn):
    try:
        result = fn()
    except pydantic.ValidationError as error:
        return ("error", [(e["type"], e["loc"]) for e in error.errors()])
    return ("ok", type(result), result)


class _Aliased(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(populate_by_name=True)
    max_tokens: Optional[int] = pydantic.Field(default=None, alias="maxTokens")


CASES = [
    ("1", int | float),
    ("1", float | int),
    ("1", Union[int, float]),
    ("1", Union[float, int]),
    (True, Literal[1]),
    (True, Literal[True]),
    (1, Literal[True]),
    ({"a": [1, 2]}, dict[str, list[int]]),
    ({"a": ["x"]}, dict[str, list[int]]),
    ({"maxTokens": 3}, _Aliased),
    ({"max_tokens": 3}, _Aliased),
    ({"maxTokens": "x"}, _Aliased),
    (None, Optional[_Aliased]),
    ([1, "2"], List[int]),
]


def _all_outcomes():
    unmarshalled = [_outcome(lambda: serializers.unmarshal(v, t)) for v, t in CASES]
    marshalled = [
        _outcome(lambda: serializers.marshal_json(v, t)) for v, t in CASES
    ]
    return unmarshalled + marshalled


@pytest.mark.parametrize("order", [1, -1], ids=["forward", "reverse"])
def test_cached_models_behave_like_uncached_ones(monkeypatch, order):
    with monkeypatch.context() as m:
        _uncached(m)
        expected = _all_outcomes()

    _client()
    serializer_cache._cached_wrapper_model.cache_clear()
    # Warm the cache in the given order, then compare every case.
    for value, typ in CASES[::order]:
        _outcome(lambda: serializers.unmarshal(value, typ))
        _outcome(lambda: serializers.marshal_json(value, typ))

    assert _all_outcomes() == expected


def test_unhashable_types_fall_back_to_uncached_models(monkeypatch):
    built = []
    uncached_create_model = serializer_cache._uncached_create_model

    def counting_create_model(*args, **kwargs):
        built.append(args[0])
        return uncached_create_model(*args, **kwargs)

    _client()
    serializer_cache._cached_wrapper_model.cache_clear()
    monkeypatch.setattr(serializer_cache, "_uncached_create_model", counting_create_model)
    typ = Annotated[int, {"unhashable": []}]

    assert serializers.unmarshal("5", typ) == 5
    assert serializers.unmarshal("5", typ) == 5
    assert built == ["Unmarshaller", "Unmarshaller"]
    assert serializer_cache._cached_wrapper_model.cache_info().currsize == 0


def test_cache_size_is_bounded():
    _client()
    serializer_cache._cached_wrapper_model.cache_clear()

    for i in range(serializer_cache._CACHE_SIZE + 50):
        dynamic = pydantic.create_model(f"Dynamic{i}", x=(int, ...))
        serializers.unmarshal({"x": i}, dynamic)

    info = serializer_cache._cached_wrapper_model.cache_info()
    assert info.maxsize == serializer_cache._CACHE_SIZE
    assert info.currsize == serializer_cache._CACHE_SIZE
