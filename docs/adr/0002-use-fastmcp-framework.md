# 2. FastMCP フレームワークの採用

Date: 2025-12-16

## Status

Accepted

## Context

Python で MCP サーバーを実装する際、ツールの定義方法を選択する必要があった。

公式 MCP SDK では手動でツールスキーマを定義する必要がある:

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

FastMCP を採用し、デコレーターベースのツール定義に移行する。

```python
@mcp.tool()
def greet(name: str) -> str:
    """ユーザーに挨拶する。

    Args:
        name: 挨拶するユーザーの名前。
    """
    return f"Hello, {name}!"
```

## Consequences

- コード量が約 50% 削減
- 関数定義がそのままツール定義になり、説明は docstring から自動生成される
- スキーマは型ヒントから自動生成される
- FastMCP への依存が追加される
