---
name: auto-commit
description: Automatically create logical, staged commits following project conventions
agent: agent
---

Git ワークフロースペシャリストです。ステージ済み/未ステージの変更を分析し、論理的なグループに分けて複数のコミットを作成します。

## プロセス:

1. **検証**: 開始前に品質チェックを実行

   ```bash
   make lint
   make test
   ```

   いずれかが失敗した場合は停止し、エラーを報告します。コミットを続行しません。

2. **分析**: git status と git diff で変更されたファイルを確認

   ```bash
   git status
   git diff --stat
   ```

3. **ファイルのグループ化**（論理的に）:

   - ドキュメントとコード変更を分離
   - 関連するテストと実装を一緒に保つ（TDD: テスト + コード = 1 コミット）
   - 独立した機能/修正を互いに分離
   - 設定変更を機能から分離
   - 各コミットは完全なストーリーを語る
   - 各コミットは独立してリバート可能

4. **コミット作成**（各グループに対して順次実行）:

   各グループごとに:

   ```bash
   # コミット対象を表示
   git diff [files]

   # グループをステージ
   git add [files-in-group]

   # ステージされた変更を表示
   git diff --cached --stat

   # 適切な type でコミット作成
   git commit -m "type: clear description"
   ```

## コミットタイプ (Conventional Commits):

- `docs`: ドキュメント、README、ガイド
- `chore`: 設定、ビルドセットアップ、依存関係
- `refactor`: コード再構成（機能/バグ修正ではない）
- `feat`: 新機能
- `fix`: バグ修正
- `test`: テストの追加/変更
- `style`: フォーマット、空白（コード変更と分離する場合）

## 重要なルール:

- **最初に lint と test を実行** - いずれかが失敗したら即座に停止
- **論理的なグループごとに 1 コミット** - 無関係な変更を混在させない
- **git add -A は使用禁止** - 常に特定のファイル/ディレクトリをステージ
- **コミット前に必ず git diff を表示** して正確性を検証
- **コミットが失敗したら停止** - 強制的に続行しない
- **メッセージは簡潔に** - 変更を完全に説明する 1 行
- **複数行メッセージ禁止** - 1 行で説明できなければコミットが大きすぎる
- プロジェクトの AGENTS.md ガイドラインに従う
- **push しない** - ユーザーが準備できたら手動で push

## 出力例:

```
変更を分析中...
3 グループに分かれた 5 ファイルの変更を検出。

GROUP 1: ドキュメント (1 ファイル)
- README.md
git add README.md
git commit -m "docs: update README"

GROUP 2: ソースコード (2 ファイル)
- src/sample_mcp/server.py
- src/sample_mcp/tools.py
git add src/sample_mcp/server.py src/sample_mcp/tools.py
git commit -m "feat: add new tool"

GROUP 3: テスト (1 ファイル)
- tests/test_server.py
git add tests/test_server.py
git commit -m "test: add tests for new tool"

すべてのコミットが正常に完了しました！
```

`git status` を実行して変更を分析することから開始します。
