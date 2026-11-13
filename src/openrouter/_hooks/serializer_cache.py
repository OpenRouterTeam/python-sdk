"""Reuse the wrapper models that ``utils.serializers`` builds for each type.

``marshal_json`` and ``unmarshal`` call ``pydantic.create_model`` on every
call, so each request builds and compiles new model classes. This module
replaces ``serializers.create_model`` with a version that builds one model per
(name, type, config) and returns it on later calls. Calls in any other shape,
or with unhashable arguments, fall through to ``pydantic.create_model``.
"""

import functools
from typing import Any, Callable, Tuple, Type, get_args, get_origin

from pydantic import BaseModel, ConfigDict

from ..utils import serializers

_uncached_create_model: Callable[..., Type[BaseModel]] = serializers.create_model

# Bounded so dynamically created types can't grow the cache without limit.
_CACHE_SIZE = 1024


def _type_key(typ: Any) -> Any:
    # Equal annotations can still validate differently: `int | float ==
    # float | int` and `Literal[1] == Literal[True]`, but pydantic tries union
    # members in order and checks literal types. Keep order and leaf types.
    args = get_args(typ)
    if not args:
        return (type(typ), typ)
    return (get_origin(typ), tuple(_type_key(arg) for arg in args))


@functools.lru_cache(maxsize=_CACHE_SIZE)
def _cached_wrapper_model(
    name: str, type_key: Any, config_items: Tuple[Tuple[str, Any], ...], typ: Any
) -> Type[BaseModel]:
    del type_key
    return _uncached_create_model(
        name, body=(typ, ...), __config__=ConfigDict(**dict(config_items))  # type: ignore[typeddict-item]
    )


def _create_model(name: str, **kwargs: Any) -> Type[BaseModel]:
    body, config = kwargs.get("body"), kwargs.get("__config__")
    if (
        set(kwargs) != {"body", "__config__"}
        or not isinstance(body, tuple)
        or len(body) != 2
        or body[1] is not ...
        or not isinstance(config, dict)
    ):
        return _uncached_create_model(name, **kwargs)
    typ = body[0]
    try:
        return _cached_wrapper_model(
            name, _type_key(typ), tuple(sorted(config.items())), typ
        )
    except TypeError:
        return _uncached_create_model(name, **kwargs)


def install() -> None:
    setattr(serializers, "create_model", _create_model)
