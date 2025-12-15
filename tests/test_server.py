"""Tests for sample_mcp.server."""

from sample_mcp.server import add, greet


def test_greet() -> None:
    """Test greet function."""
    assert greet("World") == "Hello, World!"


def test_add() -> None:
    """Test add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
