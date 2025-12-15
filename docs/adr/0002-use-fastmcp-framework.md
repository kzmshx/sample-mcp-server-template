# 2. Use FastMCP framework

Date: 2025-12-16

## Status

Accepted

## Context

When implementing the MCP server in Python, we needed to choose how to define tools.

The official MCP SDK requires manual tool schema definitions:

```python
TOOLS = [
    Tool(
        name="greet",
        description="...",
        inputSchema={
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "..."}
            },
            "required": ["name"]
        }
    )
]
```

## Decision

Adopted FastMCP and migrated to decorator-based tool definitions.

```python
@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name.

    Args:
        name: Name of the user to greet.
    """
    return f"Hello, {name}!"
```

## Consequences

- Code reduced by approximately 50%
- Function definitions directly become tool definitions, with descriptions auto-generated from docstrings
- Schemas are auto-generated from type hints
- Added dependency on FastMCP
