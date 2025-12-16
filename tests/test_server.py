"""Tests for sample_mcp.server."""

from sample_mcp.tools import greet


class TestTools:
    """Tests for MCP tools."""

    def test_greet(self) -> None:
        """Test greet function."""
        assert greet("World") == "Hello, World!"
        assert greet("Alice") == "Hello, Alice!"
        assert greet("") == "Hello, !"


class TestMCPIntegration:
    """Integration tests for MCP server."""

    def test_mcp_server_has_tools(self) -> None:
        """Test that MCP server has registered tools."""
        from sample_mcp.server import mcp

        tool_names = [t.name for t in mcp._tool_manager._tools.values()]
        assert "greet" in tool_names
