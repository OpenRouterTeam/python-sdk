"""Type definitions for the call_model API.

This module defines the core types, enums, and type aliases used throughout
the call_model implementation. All types follow Python typing conventions
with comprehensive docstrings.
"""

from enum import Enum
from typing import Any, Dict, List, Optional, TypedDict


# Type aliases for clarity and maintainability
ToolCallId = str
"""Unique identifier for a tool call."""

EventType = str
"""Type of SSE event (e.g., 'content.delta', 'tool.call')."""

StreamEvent = Dict[str, Any]
"""Raw SSE event dictionary from the API."""


class ToolType(str, Enum):
    """Enumeration of supported tool types.

    Currently only function tools are supported. This enum allows for
    future extension to other tool types.

    Attributes:
        FUNCTION: Standard function-based tool
    """

    FUNCTION = "function"


class ToolContext(TypedDict, total=False):
    """Context passed to tool execute methods.

    This context provides tools with information about the current
    conversation state, enabling context-aware tool execution.

    Attributes:
        number_of_turns: 1-indexed turn number (first turn = 1)
        message_history: List of all messages in the conversation
        model: Primary model being used (if single model)
        models: List of models (if using model routing)
        previous_tool_results: Results from previous tool executions
        request_id: Unique identifier for this request

    Example:
        >>> context = ToolContext(
        ...     number_of_turns=2,
        ...     message_history=[...],
        ...     model="gpt-4",
        ...     previous_tool_results=[...]
        ... )
    """

    number_of_turns: int
    message_history: List[Dict[str, Any]]
    model: Optional[str]
    models: Optional[List[str]]
    previous_tool_results: Optional[List[Dict[str, Any]]]
    request_id: Optional[str]


class ResponseState(str, Enum):
    """State of the ResponseWrapper.

    Tracks the lifecycle of a response from initialization through
    completion or error.

    Attributes:
        INITIALIZED: Response created but not yet consumed
        STREAMING: Currently consuming the stream
        COMPLETED: Stream fully consumed successfully
        ERROR: An error occurred during consumption
    """

    INITIALIZED = "initialized"
    STREAMING = "streaming"
    COMPLETED = "completed"
    ERROR = "error"


class CachedData(TypedDict, total=False):
    """Cached response data for reuse across consumption methods.

    This structure stores parsed data from the response to avoid
    redundant parsing when multiple consumption methods are called.

    Attributes:
        message: Complete message object with all content
        text: Extracted text content only
        tool_calls: Parsed tool call objects
        raw_response: Raw API response dictionary

    Example:
        >>> cache: CachedData = {
        ...     "message": {"role": "assistant", "content": [...]},
        ...     "text": "The weather is sunny",
        ...     "tool_calls": [...]
        ... }
    """

    message: Optional[Dict[str, Any]]
    text: Optional[str]
    tool_calls: Optional[List[Dict[str, Any]]]
    raw_response: Optional[Dict[str, Any]]
