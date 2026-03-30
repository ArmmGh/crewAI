import contextvars
import os

from localagents.events.event_bus import localagents_event_bus
from localagents.events.types.env_events import (
    CCEnvEvent,
    CodexEnvEvent,
    CursorEnvEvent,
    DefaultEnvEvent,
)
from localagents.utilities.constants import CC_ENV_VAR, CODEX_ENV_VARS, CURSOR_ENV_VARS


_env_context_emitted: contextvars.ContextVar[bool] = contextvars.ContextVar(
    "_env_context_emitted", default=False
)


def _is_codex_env() -> bool:
    return any(os.environ.get(var) for var in CODEX_ENV_VARS)


def _is_cursor_env() -> bool:
    return any(os.environ.get(var) for var in CURSOR_ENV_VARS)


def get_env_context() -> None:
    if _env_context_emitted.get():
        return
    _env_context_emitted.set(True)

    if os.environ.get(CC_ENV_VAR):
        localagents_event_bus.emit(None, CCEnvEvent())
    elif _is_codex_env():
        localagents_event_bus.emit(None, CodexEnvEvent())
    elif _is_cursor_env():
        localagents_event_bus.emit(None, CursorEnvEvent())
    else:
        localagents_event_bus.emit(None, DefaultEnvEvent())
