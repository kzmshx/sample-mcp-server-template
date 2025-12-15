"""Sample MCP server implementation."""

from fastmcp import FastMCP

mcp = FastMCP("Sample MCP")


@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name.

    Args:
        name: Name of the user to greet.

    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of the two numbers.
    """
    return a + b


@mcp.resource("config://version")
def get_version() -> str:
    """Get the server version."""
    from sample_mcp import __version__

    return __version__


def main() -> None:
    """Entry point for the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
