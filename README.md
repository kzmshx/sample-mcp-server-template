# Sample MCP Server Template

FastMCP を使用した MCP サーバー開発のテンプレートリポジトリ。

## 特徴

- FastMCP によるシンプルなツール定義
- uv によるモダンなパッケージ管理
- release-please による自動リリース
- ADR (Architecture Decision Records) による設計判断の記録
- GitHub Actions による CI/CD
- GitHub Copilot / Claude Code 向けのエージェント設定
- PDD (Plan Driven Development) ワークフロー

## セットアップ

```bash
# リポジトリをテンプレートから作成
gh repo create my-mcp-server --template kzmshx/sample-mcp-server-template

# クローン
git clone https://github.com/your-username/my-mcp-server
cd my-mcp-server

# 依存関係のインストール
uv sync
```

## 開発

```bash
# 開発モードで起動
make dev

# MCP Inspector で確認
make inspect

# リント
make lint

# 自動修正
make fix

# テスト
make test

# 型チェック
make typecheck
```

## ディレクトリ構成

```
.
├── .github/
│   ├── agents/                  # カスタムエージェント
│   │   └── pdd.agent.md
│   ├── prompts/                 # プロンプトテンプレート
│   │   └── auto-commit.prompt.md
│   ├── copilot-instructions.md  # Copilot Agent 向け設定
│   └── workflows/               # GitHub Actions
├── .pdd/                        # 作業ドキュメント（Git除外）
│   └── {branch}/
│       ├── PLAN.md
│       └── NOTES_*.md
├── docs/
│   └── adr/                     # Architecture Decision Records
├── src/
│   └── sample_mcp/              # ソースコード
├── tests/                       # テスト
├── AGENTS.md                    # AI エージェント向け共通プロンプト
├── pyproject.toml               # プロジェクト設定
└── Makefile                     # 開発コマンド
```

## 利用可能なツール

### `greet`

挨拶メッセージを返すサンプルツール。

**パラメータ**:

- `name` (string): 挨拶する相手の名前

**使用例**:

```
greet("World")  # "Hello, World!"
```

## ツールの追加方法

1. `src/sample_mcp/tools.py` に実装を追加:

```python
def my_tool(param: str) -> str:
    """ツールの説明。

    Args:
        param: パラメータの説明。

    Returns:
        戻り値の説明。
    """
    return f"Result: {param}"
```

2. `src/sample_mcp/server.py` に登録:

```python
from sample_mcp.tools import my_tool as _my_tool

@mcp.tool()
def my_tool(param: str) -> str:
    """ツールの説明。

    Args:
        param: パラメータの説明。

    Returns:
        戻り値の説明。
    """
    return _my_tool(param)
```

- 型ヒントから JSON Schema が自動生成される
- docstring から説明が自動抽出される

## リリース

main ブランチへのマージ時に release-please が自動で:

1. Conventional Commits からリリース PR を作成
2. CHANGELOG.md を更新
3. バージョンをバンプ

## 開発に貢献

このプロジェクトへの貢献に興味がある方は、開発者向けドキュメントを参照してください：

- [AGENTS.md](AGENTS.md): 開発哲学とワークフロー
- [docs/adr/](docs/adr/): アーキテクチャ決定記録

## ライセンス

MIT
