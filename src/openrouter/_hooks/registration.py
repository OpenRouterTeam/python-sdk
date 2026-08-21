from openrouter import components
from openrouter.sdkconfiguration import SDKConfiguration

from .types import Hooks, SDKInitHook


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


class BlankAPIKeyIsUnsetHook(SDKInitHook):
    """Treat a blank `api_key` as "not supplied".

    `get_security_from_env` only falls back to `OPENROUTER_API_KEY` when no
    security was supplied at all, so `OpenRouter(api_key="")` short-circuits the
    fallback. The documented pattern `api_key=os.getenv("OPENROUTER_API_KEY", "")`
    hits that path whenever the variable is unset, and the resulting empty bearer
    token fails inside httpx with `LocalProtocolError: Illegal header value
    b'Bearer '` — before any request is sent, and with nothing to suggest the
    problem is a missing credential.

    Normalising the blank value to `None` here restores the fallback, and leaves
    a client with genuinely no credentials sending no `Authorization` header at
    all, which is the clearer failure.

    A callable `api_key` is left alone: it is resolved per-request, and calling
    it here to inspect the result would defeat that.
    """

    def sdk_init(self, config: SDKConfiguration) -> SDKConfiguration:
        security = config.security
        if isinstance(security, components.Security):
            if security.api_key is None or not security.api_key.strip():
                config.security = None
        return config


def init_hooks(hooks: Hooks):
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    hooks.register_sdk_init_hook(BlankAPIKeyIsUnsetHook())
