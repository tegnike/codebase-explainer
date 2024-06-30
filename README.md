# codebase-explainer

AIを活用してプロジェクトのコードベースを分析し、ファイル構造とファイルの説明を生成するPythonスクリプトです。

## 概要

このスクリプトは、指定されたフォルダ内のファイルを解析し、以下の機能を提供します：

1. プロジェクトのファイル構造をツリー形式で表示
2. テキストファイルの内容をAI（Claude）を使用して分析し、各ファイルの説明を生成
3. .gitignoreに基づいてファイルを除外
4. バイナリファイルや空のファイルを自動的に除外
5. 特定の拡張子を持つファイルを除外するオプション

## 使い方

1. 必要なライブラリをインストールします：
   ```
   pip install -r requirements.txt
   ```

2. 環境変数に `ANTHROPIC_API_KEY` を設定します：
   ```
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

3. スクリプトを実行します：
   ```
   python main.py /path/to/your/project --output analysis.txt
   ```

### オプション

- `--output`: 出力ファイルの名前を指定（デフォルト: output.txt）
- `--exclude`: 除外する拡張子のリストを指定（例: `--exclude jpg png`）
- `--prompt`: カスタムプロンプトテンプレートを指定
- `--dry-run`: LLM処理を実行せずに対象ファイルのリストを出力

### 例

1. プロジェクトの分析を実行：
   ```
   python main.py /path/to/your/project --output analysis.txt
   ```

2. 特定の拡張子を除外してドライラン：
   ```
   python main.py /path/to/your/project --exclude jpg png --dry-run
   ```

## 注意事項

- このスクリプトはAnthropicのClaudeモデルを使用します。適切なAPI使用料金が発生する可能性があります。
- 大規模なプロジェクトの場合、処理に時間がかかる可能性があります。
- テキストファイルのエンコーディングによっては、正しく読み取れない場合があります。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。
