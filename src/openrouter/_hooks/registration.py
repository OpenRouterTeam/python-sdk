import os

import httpx

from openrouter import components
from openrouter.sdkconfiguration import SDKConfiguration

from .types import BeforeRequestContext, BeforeRequestHook, Hooks, SDKInitHook


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


class BlankAPIKeyIsUnsetHook(SDKInitHook, BeforeRequestHook):
    """Treat a blank `api_key` (e.g. from `os.getenv("OPENROUTER_API_KEY", "")`)
    as not supplied, so the `OPENROUTER_API_KEY` env-var fallback still applies
    instead of sending an empty `Bearer ` token.

    The env var is read per request and a callable `api_key` is resolved per
    request, so either can still yield a blank token after init; a blank
    bearer token is replaced with `OPENROUTER_API_KEY` when that is set, and
    otherwise the `Authorization` header is dropped.
    """

    def sdk_init(self, config: SDKConfiguration) -> SDKConfiguration:
        security = config.security
        if isinstance(security, components.Security) and not (
            security.api_key or ""
        ).strip():
            config.security = None
        return config

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        auth = request.headers.get("authorization")
        if auth is not None:
            scheme, _, token = auth.strip().partition(" ")
            if not auth.strip() or (scheme.lower() == "bearer" and not token.strip()):
                env_key = (os.getenv("OPENROUTER_API_KEY") or "").strip()
                if env_key:
                    request.headers["authorization"] = f"Bearer {env_key}"
                else:
                    del request.headers["authorization"]
        return request


def init_hooks(hooks: Hooks):
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    blank_api_key_hook = BlankAPIKeyIsUnsetHook()
    hooks.register_sdk_init_hook(blank_api_key_hook)
    hooks.register_before_request_hook(blank_api_key_hook)
