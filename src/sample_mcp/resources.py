"""Resource implementations for Sample MCP server."""

from sample_mcp import __version__


def get_version() -> str:
    """Get the server version."""
    return __version__


def get_server_info() -> str:
    """Get server information."""
    return f"""Sample MCP Server
Version: {__version__}
Description: A hello-world MCP server built with FastMCP
Available tools: greet, add, multiply, get_current_time, reverse_string, count_words
"""
