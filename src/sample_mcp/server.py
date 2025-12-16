"""Sample MCP server implementation.

This server demonstrates the MCP tools primitive:
- Tools: Functions that can be called by the LLM
"""

from fastmcp import FastMCP

from sample_mcp.tools import greet as _greet

mcp = FastMCP("Sample MCP")


@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name.

    Args:
        name: Name of the user to greet.

    Returns:
        A greeting message.
    """
    return _greet(name)


def main() -> None:
    """Entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
