# AGENTS.md

すべての AI コーディングエージェント（GitHub Copilot、Claude Code、Cursor、Cline など）向けの開発規約。

## コミット規約

Conventional Commits を採用:

| type       | 用途                                               |
| ---------- | -------------------------------------------------- |
| `feat`     | 新機能                                             |
| `fix`      | バグ修正                                           |
| `docs`     | ドキュメントのみ                                   |
| `style`    | コードの意味に影響しない変更（空白、フォーマット） |
| `refactor` | バグ修正でも新機能でもないコード変更               |
| `test`     | テストの追加・修正                                 |
| `chore`    | ビルドプロセスやツールの変更                       |

ブランチ名: `{type}/{description}` (例: `feat/add-tool`, `fix/error-handling`)

## 開発ワークフロー

PDD (Plan Driven Development) を採用。詳細は以下を参照:

- **ワークフローガイド**: VS Code Copilot Chat で `@pdd` エージェントを使用
- **ドキュメントルール**: [.pdd/AGENTS.md](.pdd/AGENTS.md)

## ドキュメント原則

### 記述スタイル

- 事実を簡潔に記述
- 抽象的な説明より具体例を優先
- 可読性のためのリストや表は推奨

### セキュリティルール

Git 追跡されるドキュメントには以下を記載しない:

- 秘密鍵、トークン、パスワード、API キー
- 個人を特定できる情報（名前、メール、ユーザー名）
- ローカル環境のパス（例: `/Users/username/`）

ローカル専用情報は `AGENTS.local.md` に記載（Git 除外）。

### 共通ルール

- 絵文字禁止
- 水平線（`---`）禁止

## アーキテクチャ決定記録

重要な設計判断は `docs/adr/` に adr-tools で記録。

## リリース

release-please による自動リリース。Conventional Commits から CHANGELOG とバージョンを自動生成。

## 技術スタックとコマンド

詳細は [.github/copilot-instructions.md](.github/copilot-instructions.md) を参照。
