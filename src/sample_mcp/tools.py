"""Tool implementations for Sample MCP server."""

from datetime import datetime, timezone


def greet(name: str) -> str:
    """Greet a user by name.

    Args:
        name: Name of the user to greet.

    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of the two numbers.
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of the two numbers.
    """
    return a * b


def get_current_time() -> str:
    """Get the current UTC time.

    Returns:
        Current time in ISO 8601 format.
    """
    return datetime.now(timezone.utc).isoformat()


def reverse_string(text: str) -> str:
    """Reverse a string.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.
    """
    return text[::-1]


def count_words(text: str) -> dict[str, int]:
    """Count words in a text.

    Args:
        text: The text to analyze.

    Returns:
        Dictionary with word count statistics.
    """
    words = text.split()
    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "characters": len(text),
    }
