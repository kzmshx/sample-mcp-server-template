"""Sample MCP server implementation.

This server demonstrates the three main MCP primitives:
- Tools: Functions that can be called by the LLM
- Resources: Data that can be read by the LLM
- Prompts: Reusable prompt templates
"""

from fastmcp import FastMCP

from sample_mcp.prompts import greeting_prompt as _greeting_prompt
from sample_mcp.prompts import summarize_prompt as _summarize_prompt
from sample_mcp.resources import get_server_info as _get_server_info
from sample_mcp.resources import get_version as _get_version
from sample_mcp.tools import add as _add
from sample_mcp.tools import count_words as _count_words
from sample_mcp.tools import get_current_time as _get_current_time
from sample_mcp.tools import greet as _greet
from sample_mcp.tools import multiply as _multiply
from sample_mcp.tools import reverse_string as _reverse_string

mcp = FastMCP("Sample MCP")


# =============================================================================
# Tools
# =============================================================================


@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name.

    Args:
        name: Name of the user to greet.

    Returns:
        A greeting message.
    """
    return _greet(name)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of the two numbers.
    """
    return _add(a, b)


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of the two numbers.
    """
    return _multiply(a, b)


@mcp.tool()
def get_current_time() -> str:
    """Get the current UTC time.

    Returns:
        Current time in ISO 8601 format.
    """
    return _get_current_time()


@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse a string.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.
    """
    return _reverse_string(text)


@mcp.tool()
def count_words(text: str) -> dict[str, int]:
    """Count words in a text.

    Args:
        text: The text to analyze.

    Returns:
        Dictionary with word count statistics.
    """
    return _count_words(text)


# =============================================================================
# Resources
# =============================================================================


@mcp.resource("config://version")
def get_version() -> str:
    """Get the server version."""
    return _get_version()


@mcp.resource("config://info")
def get_server_info() -> str:
    """Get server information."""
    return _get_server_info()


# =============================================================================
# Prompts
# =============================================================================


@mcp.prompt()
def greeting_prompt(name: str) -> str:
    """Generate a greeting prompt.

    Args:
        name: Name of the person to greet.

    Returns:
        A prompt for generating a personalized greeting.
    """
    return _greeting_prompt(name)


@mcp.prompt()
def summarize_prompt(topic: str) -> str:
    """Generate a summarization prompt.

    Args:
        topic: The topic to summarize.

    Returns:
        A prompt for summarizing the topic.
    """
    return _summarize_prompt(topic)


# =============================================================================
# Entry Point
# =============================================================================


def main() -> None:
    """Entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
