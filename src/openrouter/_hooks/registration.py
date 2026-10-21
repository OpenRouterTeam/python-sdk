from openrouter import components
from openrouter.sdkconfiguration import SDKConfiguration

from .types import Hooks, SDKInitHook


# This file is only ever generated once on the first generation and then is free to be modified.
# Any hooks you wish to add should be registered in the init_hooks function. Feel free to define them
# in this file or in separate files in the hooks folder.


class BlankAPIKeyIsUnsetHook(SDKInitHook):
    """Treat a blank `api_key` (e.g. from `os.getenv("OPENROUTER_API_KEY", "")`)
    as not supplied, so the `OPENROUTER_API_KEY` env-var fallback still applies
    instead of sending an empty `Bearer ` token.

    Callable `api_key`s are resolved per request and are left untouched.
    """

    def sdk_init(self, config: SDKConfiguration) -> SDKConfiguration:
        security = config.security
        if isinstance(security, components.Security) and not (
            security.api_key or ""
        ).strip():
            config.security = None
        return config


def init_hooks(hooks: Hooks):
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    hooks.register_sdk_init_hook(BlankAPIKeyIsUnsetHook())
