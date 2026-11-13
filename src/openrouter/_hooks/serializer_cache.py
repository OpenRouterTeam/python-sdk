"""Reuse the wrapper models that ``utils.serializers`` builds for each type.

``marshal_json`` and ``unmarshal`` call ``pydantic.create_model`` on every
call, so each request builds and compiles new model classes. This module
replaces ``serializers.create_model`` with a version that builds one model per
(name, type, config) and returns it on later calls. Calls in any other shape,
or with unhashable arguments, fall through to ``pydantic.create_model``.
"""

import functools
from typing import Any, Callable, Tuple, Type

from pydantic import BaseModel, ConfigDict

from ..utils import serializers

_uncached_create_model: Callable[..., Type[BaseModel]] = serializers.create_model


@functools.lru_cache(maxsize=None)
def _cached_wrapper_model(
    name: str, typ: Any, config_items: Tuple[Tuple[str, Any], ...]
) -> Type[BaseModel]:
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
    try:
        return _cached_wrapper_model(name, body[0], tuple(sorted(config.items())))
    except TypeError:
        return _uncached_create_model(name, **kwargs)


def install() -> None:
    setattr(serializers, "create_model", _create_model)
