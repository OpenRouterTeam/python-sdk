"""Custom exception types for the call_model API.

This module defines the exception hierarchy for call_model operations,
providing actionable error messages with context for debugging.
"""

from typing import Any, Dict, List, Optional


class CallModelError(Exception):
    """Base exception for all call_model errors.

    This exception includes optional error codes and context to help
    developers understand and resolve issues.

    Attributes:
        message: Human-readable error description
        code: Optional error code for programmatic handling
        context: Optional dictionary with additional error context
    """

    def __init__(
        self,
        message: str,
        code: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ):
        """Initialize the error with message, code, and context.

        Args:
            message: Human-readable error description
            code: Optional error code for programmatic handling
            context: Optional dictionary with additional error context
        """
        super().__init__(message)
        self.message = message
        self.code = code
        self.context = context or {}

    def __str__(self) -> str:
        """Return the error message."""
        return self.message


class ToolExecutionError(CallModelError):
    """Raised when tool execution fails.

    This exception includes the tool name, original error, and input context
    to help developers debug tool implementation issues.

    Example:
        >>> try:
        ...     result = await tool.execute(params, context)
        ... except Exception as e:
        ...     raise ToolExecutionError(
        ...         tool_name="weather_tool",
        ...         error=e,
        ...         context={"input": params, "tool_call_id": "call_123"}
        ...     )
    """

    def __init__(self, tool_name: str, error: Exception, context: Dict[str, Any]):
        """Initialize the tool execution error.

        Args:
            tool_name: Name of the tool that failed
            error: Original exception that was raised
            context: Context dictionary with input, tool_call_id, etc.
        """
        message = f"Tool '{tool_name}' failed: {error}"

        if "input" in context:
            message += f"\nInput: {context['input']}"

        message += "\nSuggestion: Check tool implementation and input validation"

        super().__init__(message=message, code="TOOL_EXECUTION_ERROR", context=context)
        self.tool_name = tool_name
        self.original_error = error


class ToolValidationError(CallModelError):
    """Raised when tool input validation fails.

    This exception includes the validation errors from Pydantic to help
    developers understand what inputs were invalid.

    Example:
        >>> raise ToolValidationError(
        ...     tool_name="weather_tool",
        ...     validation_errors=["Field 'location' is required"]
        ... )
    """

    def __init__(self, tool_name: str, validation_errors: List[str]):
        """Initialize the tool validation error.

        Args:
            tool_name: Name of the tool that failed validation
            validation_errors: List of validation error messages
        """
        message = f"Tool '{tool_name}' validation failed:\n"
        message += "\n".join(f"  - {err}" for err in validation_errors)
        message += "\nSuggestion: Ensure input matches the tool's Pydantic schema"

        super().__init__(message=message, code="TOOL_VALIDATION_ERROR")
        self.tool_name = tool_name
        self.validation_errors = validation_errors


class StreamInterruptedError(CallModelError):
    """Raised when stream is interrupted.

    This exception includes details about the last successful event
    to help developers understand where the stream failed.

    Example:
        >>> raise StreamInterruptedError(
        ...     last_event={"type": "content.delta", "delta": {...}}
        ... )
    """

    def __init__(self, last_event: Optional[Dict[str, Any]] = None):
        """Initialize the stream interrupted error.

        Args:
            last_event: Optional dictionary with the last successful event
        """
        message = "Stream was interrupted"

        if last_event:
            message += f"\nLast successful event: {last_event.get('type', 'unknown')}"

        message += "\nSuggestion: Check network connection and retry"

        super().__init__(message=message, code="STREAM_INTERRUPTED")
        self.last_event = last_event


class MaxToolRoundsExceededError(CallModelError):
    """Raised when tool execution rounds exceed limit.

    This exception helps developers identify infinite tool loops
    or adjust the max_tool_rounds parameter.

    Example:
        >>> raise MaxToolRoundsExceededError(rounds=10, max_rounds=5)
    """

    def __init__(self, rounds: int, max_rounds: int):
        """Initialize the max tool rounds exceeded error.

        Args:
            rounds: Number of rounds executed
            max_rounds: Maximum allowed rounds
        """
        message = f"Tool execution exceeded maximum rounds ({rounds}/{max_rounds})"
        message += "\nSuggestion: Increase max_tool_rounds or check for tool loops"

        super().__init__(message=message, code="MAX_ROUNDS_EXCEEDED")
        self.rounds = rounds
        self.max_rounds = max_rounds
