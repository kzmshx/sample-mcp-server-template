# AGENTS.md

各種 AI コーディングエージェント向けの共通プロンプト。
GitHub Copilot、Claude Code、Cursor、Cline など。

## コミット規約 / ブランチ命名

| type       | 用途                                                   |
| ---------- | ----------------------------------------------------- |
| `feat`     | 新機能                                                 |
| `fix`      | バグ修正                                               |
| `docs`     | ドキュメントのみ                                        |
| `style`    | コードの意味に影響しない変更（空白、フォーマット）            |
| `refactor` | バグ修正でも新機能でもないコード変更                       |
| `test`     | テストの追加・修正                                       |
| `chore`    | ビルドプロセスやツールの変更                              |

ブランチ名: `{type}/{description}` (例: `feat/add-tool`, `fix/error-handling`)

## 開発ワークフロー

1. ブランチを作成 (`{type}/{description}`)
2. `.pdd/{branch}/PLAN.md` を作成
3. 実装前に PLAN.md をレビュー・精査
4. 実装
5. マイルストーンごとに `NOTES_{YYYYMMDD_HHMMSS}.md` を作成
6. PR を作成してマージ

## PR レビュー対応

| 操作         | コマンド                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------- |
| CI 確認     | `gh pr checks {n}`                                                                            |
| コメント取得 | `gh api repos/{owner}/{repo}/pulls/{n}/comments`                                               |
| 返信        | `gh api repos/{owner}/{repo}/pulls/{n}/comments/{comment_id}/replies -X POST -f body="..."`    |

修正後はコミットハッシュを添えて返信する。

## ドキュメント構成

### .pdd/{branch}/

ブランチごとの作業ドキュメント。`.gitignore` で除外。

構成:

- `PLAN.md`: 機能仕様と実装タスク
- `NOTES_{YYYYMMDD_HHMMSS}.md`: 作業ログ（発見事項、問題、解決策）。マイルストーンごとに作成

### docs/adr/

`adr` CLI (adr-tools) で管理。Git 追跡対象。

- 作成: `adr new <title>`
- 一覧: `adr list`
- 置換: `adr new -s <number> <title>`

## ドキュメントルール

### 共通ルール

- 絵文字禁止
- 水平線 (`---`) 禁止

### 共通スタイル

- 事実を簡潔に記述
- 不要な装飾や冗長な説明を避ける（可読性のためのリストや表は可）
- コードや設定は具体例を示す

### セキュリティルール（重要）

`docs/` 配下のドキュメントは Git 追跡されるため、以下は禁止:

- 秘密鍵、トークン、パスワード
- API キー、認証情報
- 個人を特定できる情報（名前、メール、ユーザー名）
- ローカル環境のパス (例: `/Users/username/`)
- プロジェクト ID やリソース名は OK (例: `my-project-id`)
- 具体的な設定値は `.env.example` などのテンプレートファイルを参照
- ローカル環境の情報は `AGENTS.local.md` に記載

### .pdd/{branch}/PLAN.md ルール

- h1 見出しは `# PLAN`
- h2, h3, h4 は使用可（過度なネストは避ける）

### .pdd/{branch}/NOTES_{YYYYMMDD_HHMMSS}.md ルール

- ファイル名のタイムスタンプは `date +%Y%m%d_%H%M%S` の出力をそのまま使用（変更不可）
- h1 見出しはファイル名と一致 (例: `# NOTES_20251129_094523`)
- h2 見出しのみ使用し、その直下に簡潔なポイントを記載（h3 以下は不可）
- 各セクション内に参照リンクを含める

## 技術スタック

- Python 3.11+
- FastMCP による MCP サーバー実装
- uv によるパッケージ管理
- ruff によるリント・フォーマット
- mypy による型チェック
- pytest によるテスト
