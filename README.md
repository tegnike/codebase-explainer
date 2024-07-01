# codebase-explainer

AIを活用してプロジェクトのコードベースを分析し、ファイル構造とファイルの説明を生成するPythonスクリプトです。

## 概要

このスクリプトは、指定されたフォルダ内のファイルを解析し、以下の機能を提供します：

1. プロジェクトのファイル構造をMarkdownのツリー形式で表示
2. テキストファイルの内容をAI（Claude）を使用して分析し、各ファイルの説明を生成
3. .gitignoreに基づいてファイルを除外
4. .projectignoreファイルを使用して追加のファイル除外を管理
5. バイナリファイルや空のファイルを自動的に除外
6. 特定の拡張子を持つファイルを除外するオプション
7. 実行時間の計測と表示

## 使い方

1. 必要なライブラリをインストールします：
   ```
   pip install -r requirements.txt
   ```

2. 環境変数に `ANTHROPIC_API_KEY` を設定します：
   ```
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

3. まず、dry-runモードでスクリプトを実行して.projectignoreファイルを作成します：
   ```
   python main.py /path/to/your/project --dry-run
   ```

4. 必要に応じて.projectignoreファイルを編集します。

5. 本実行を行います：
   ```
   python main.py /path/to/your/project
   ```

### オプション

- `--exclude`: 除外する拡張子のリストを指定（例: `--exclude jpg png`）
- `--prompt`: カスタムプロンプトテンプレートを指定
- `--dry-run`: .projectignoreファイルの作成と対象ファイルのリスト出力のみを行う

### 例

1. dry-runの実行：
   ```
   python main.py /path/to/your/project --dry-run
   ```

2. 特定の拡張子を除外して本実行：
   ```
   python main.py /path/to/your/project --exclude jpg png
   ```

## 出力形式

スクリプトは以下の形式でMarkdownファイルを生成します：

1. プロジェクト構造（# Project Structure）
   - .gitignoreで除外されたファイルは表示されません
   - .projectignoreで除外されたファイルはツリー構造には表示されますが、AIによるファイル説明は実行されません
2. ファイルの説明（# File Descriptions）
   - 各ファイルに対して：
     - ファイルの説明（### File Description）
     - インポートされているモジュール（### Imported Modules）
     - 定義されている関数（### Functions）

## 参考

[sample.md](sample.md) は [tegnike/aituber-kit(v1.24.0)](https://github.com/tegnike/aituber-kit) の実行結果です。

- 対象ファイル数: 95
- 出力行数: 1,575
- 実行時間: 494.41秒
- API費用: $0.69

## 注意事項

- このスクリプトはAnthropicのClaudeモデル（claude-3-sonnet-20240229）を使用します。適切なAPI使用料金が発生する可能性があります。
- 大規模なプロジェクトの場合、処理に時間がかかる可能性があります。
- テキストファイルのエンコーディングによっては、正しく読み取れない場合があります。
- スクリプトの実行時間が表示されます。
- 必ず最初にdry-runを実行して.projectignoreファイルを作成してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 宣伝

AIキャラクターと対話したり、Youtube配信できるWebアプリを開発中です（[tegnike/aituber-kit](https://github.com/tegnike/aituber-kit)）
