"""Tests for sample_mcp.server."""

from sample_mcp.prompts import greeting_prompt, summarize_prompt
from sample_mcp.resources import get_server_info, get_version
from sample_mcp.tools import (
    add,
    count_words,
    get_current_time,
    greet,
    multiply,
    reverse_string,
)


class TestTools:
    """Tests for MCP tools."""

    def test_greet(self) -> None:
        """Test greet function."""
        assert greet("World") == "Hello, World!"
        assert greet("Alice") == "Hello, Alice!"
        assert greet("") == "Hello, !"

    def test_add(self) -> None:
        """Test add function."""
        assert add(1, 2) == 3
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
        assert add(-5, -3) == -8

    def test_multiply(self) -> None:
        """Test multiply function."""
        assert multiply(2, 3) == 6.0
        assert multiply(0, 100) == 0.0
        assert multiply(-2, 3) == -6.0
        assert multiply(1.5, 2) == 3.0

    def test_get_current_time(self) -> None:
        """Test get_current_time function."""
        result = get_current_time()
        assert isinstance(result, str)
        assert "T" in result
        assert "+" in result or "Z" in result or result.endswith("+00:00")

    def test_reverse_string(self) -> None:
        """Test reverse_string function."""
        assert reverse_string("hello") == "olleh"
        assert reverse_string("") == ""
        assert reverse_string("a") == "a"
        assert reverse_string("12345") == "54321"

    def test_count_words(self) -> None:
        """Test count_words function."""
        result = count_words("hello world")
        assert result["total_words"] == 2
        assert result["unique_words"] == 2
        assert result["characters"] == 11

        result = count_words("the the the")
        assert result["total_words"] == 3
        assert result["unique_words"] == 1

        result = count_words("")
        assert result["total_words"] == 0
        assert result["unique_words"] == 0
        assert result["characters"] == 0


class TestResources:
    """Tests for MCP resources."""

    def test_get_version(self) -> None:
        """Test get_version resource."""
        version = get_version()
        assert isinstance(version, str)
        assert version == "0.1.0"

    def test_get_server_info(self) -> None:
        """Test get_server_info resource."""
        info = get_server_info()
        assert "Sample MCP Server" in info
        assert "0.1.0" in info
        assert "FastMCP" in info


class TestPrompts:
    """Tests for MCP prompts."""

    def test_greeting_prompt(self) -> None:
        """Test greeting_prompt function."""
        result = greeting_prompt("Alice")
        assert "Alice" in result
        assert "greeting" in result.lower()

    def test_summarize_prompt(self) -> None:
        """Test summarize_prompt function."""
        result = summarize_prompt("Python programming")
        assert "Python programming" in result
        assert "summary" in result.lower()


class TestMCPIntegration:
    """Integration tests for MCP server."""

    def test_mcp_server_has_tools(self) -> None:
        """Test that MCP server has registered tools."""
        from sample_mcp.server import mcp

        tool_names = [t.name for t in mcp._tool_manager._tools.values()]
        assert "greet" in tool_names
        assert "add" in tool_names
        assert "multiply" in tool_names
        assert "get_current_time" in tool_names
        assert "reverse_string" in tool_names
        assert "count_words" in tool_names

    def test_mcp_server_has_resources(self) -> None:
        """Test that MCP server has registered resources."""
        from sample_mcp.server import mcp

        resource_uris = list(mcp._resource_manager._resources.keys())
        assert "config://version" in resource_uris
        assert "config://info" in resource_uris

    def test_mcp_server_has_prompts(self) -> None:
        """Test that MCP server has registered prompts."""
        from sample_mcp.server import mcp

        prompt_names = list(mcp._prompt_manager._prompts.keys())
        assert "greeting_prompt" in prompt_names
        assert "summarize_prompt" in prompt_names
