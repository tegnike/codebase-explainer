import os
import sys
import ast
import time
import argparse
import anthropic
import pathspec
import chardet
from typing import List, Set
from datetime import datetime


def read_gitignore(folder_path: str) -> pathspec.PathSpec:
    """
    指定されたフォルダ内の.gitignoreファイルを読み込み、PathSpecオブジェクトを返す。

    .gitディレクトリとnode_modulesを常に除外するパターンも追加する。

    Args:
        folder_path (str): .gitignoreファイルを探すフォルダのパス

    Returns:
        pathspec.PathSpec: 生成されたPathSpecオブジェクト
    """
    gitignore_path = os.path.join(folder_path, ".gitignore")
    patterns = [".git/", "node_modules/"]  # .gitディレクトリとnode_modulesを常に除外
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            patterns.extend(f.read().splitlines())
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)


def read_projectignore(output_dir: str) -> pathspec.PathSpec:
    """
    指定されたディレクトリ内の.projectignoreファイルを読み込み、PathSpecオブジェクトを返す。

    Args:
        output_dir (str): .projectignoreファイルを探すディレクトリのパス

    Returns:
        pathspec.PathSpec: 生成されたPathSpecオブジェクト
    """
    projectignore_path = os.path.join(output_dir, ".projectignore")
    if not os.path.exists(projectignore_path):
        raise FileNotFoundError(f".projectignoreファイルが見つかりません: {projectignore_path}")

    with open(projectignore_path, "r") as f:
        patterns = f.read().splitlines()
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)


def is_ignored(
    path: str,
    gitignore_spec: pathspec.PathSpec,
    projectignore_spec: pathspec.PathSpec,
    base_path: str,
) -> bool:
    """
    指定されたパスが無視すべきかどうかを判断する。

    Args:
        path (str): チェックするパス
        gitignore_spec (pathspec.PathSpec): GitignoreのPathSpecオブジェクト
        projectignore_spec (pathspec.PathSpec): ProjectignoreのPathSpecオブジェクト
        base_path (str): プロジェクトのベースパス

    Returns:
        bool: パスが無視すべき場合はTrue、そうでない場合はFalse
    """
    rel_path = os.path.relpath(path, base_path)
    return gitignore_spec.match_file(rel_path) or projectignore_spec.match_file(
        rel_path
    )


def is_ignored_by_gitignore(
    path: str, gitignore_spec: pathspec.PathSpec, base_path: str
) -> bool:
    """
    指定されたパスが.gitignoreによって無視すべきかどうかを判断する。

    Args:
        path (str): チェックするパス
        gitignore_spec (pathspec.PathSpec): GitignoreのPathSpecオブジェクト
        base_path (str): プロジェクトのベースパス

    Returns:
        bool: パスが無視すべき場合はTrue、そうでない場合はFalse
    """
    rel_path = os.path.relpath(path, base_path)
    return gitignore_spec.match_file(rel_path)


def is_ignored_by_projectignore(
    path: str, projectignore_spec: pathspec.PathSpec, base_path: str
) -> bool:
    """
    指定されたパスが.projectignoreによって無視すべきかどうかを判断する。

    Args:
        path (str): チェックするパス
        projectignore_spec (pathspec.PathSpec): ProjectignoreのPathSpecオブジェクト
        base_path (str): プロジェクトのベースパス

    Returns:
        bool: パスが無視すべき場合はTrue、そうでない場合はFalse
    """
    rel_path = os.path.relpath(path, base_path)
    return projectignore_spec.match_file(rel_path)


def get_file_tree(
    folder_path: str,
    gitignore_spec: pathspec.PathSpec,
    projectignore_spec: pathspec.PathSpec,
) -> str:
    """
    指定されたフォルダのファイル構造をMarkdownのツリー形式で返す。
    .gitignoreで無視されたファイルは除外し、.projectignoreで無視されたファイルは含める。

    Args:
        folder_path (str): ツリーを生成するフォルダのパス
        gitignore_spec (pathspec.PathSpec): GitignoreのPathSpecオブジェクト
        projectignore_spec (pathspec.PathSpec): ProjectignoreのPathSpecオブジェクト

    Returns:
        str: Markdown形式のファイル構造を表す文字列
    """
    tree = []
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [
            d
            for d in dirs
            if not is_ignored_by_gitignore(
                os.path.join(root, d), gitignore_spec, folder_path
            )
        ]
        level = root.replace(folder_path, "").count(os.sep)
        indent = "  " * level
        tree.append(f"{indent}- {os.path.basename(root)}/")
        for file in files:
            file_path = os.path.join(root, file)
            if not is_ignored_by_gitignore(file_path, gitignore_spec, folder_path):
                if is_ignored_by_projectignore(
                    file_path, projectignore_spec, folder_path
                ):
                    tree.append(f"{indent}  - {file}")
                else:
                    tree.append(f"{indent}  - {file}")
    return "\n".join(tree)


def is_text_file(file_path: str, sample_size: int = 1024) -> bool:
    """
    ファイルがテキストファイルかどうかを判断する。

    Args:
        file_path (str): チェックするファイルのパス
        sample_size (int, optional): 読み込むサンプルサイズ（バイト）。デフォルトは1024。

    Returns:
        bool: テキストファイルの場合はTrue、そうでない場合はFalse
    """
    try:
        with open(file_path, "rb") as f:
            sample = f.read(sample_size)

        if not sample:  # 空のファイルの場合
            return True

        # NULL バイトがあればバイナリファイルと判断
        if b"\x00" in sample:
            return False

        # エンコーディングを推測
        result = chardet.detect(sample)
        if result["encoding"] is None:
            return False

        return True
    except (UnicodeDecodeError, IOError):
        return False


def get_file_description(
    client: anthropic.Client,
    file_path: str,
    folder_path: str,
    prompt_template: str,
) -> str:
    """
    指定されたファイルの内容を分析し、説明を生成する。

    Args:
        client (anthropic.Client): Anthropic APIクライアント
        file_path (str): 分析するファイルのパス
        folder_path (str): プロジェクトのベースパス
        prompt_template (str): 説明生成に使用するプロンプトのテンプレート

    Returns:
        str: 生成されたMarkdown形式の説明
    """
    with open(file_path, "r") as f:
        content = f.read()

    prompt = prompt_template.format(content=content)

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    description = response.content[0].text

    # 絶対パスを相対パスに変換
    relative_path = os.path.relpath(file_path, folder_path)

    markdown_description = f"""
## {relative_path}

{description.strip()}
"""
    return markdown_description


def create_projectignore(output_dir: str) -> None:
    """
    指定されたディレクトリに.projectignoreファイルを作成する。

    Args:
        output_dir (str): .projectignoreファイルを作成するディレクトリのパス
    """
    projectignore_path = os.path.join(output_dir, ".projectignore")
    if not os.path.exists(projectignore_path):
        with open(projectignore_path, "w") as f:
            f.write("# Add patterns to ignore here, one per line\n")
        print(f".projectignoreファイルが作成されました: {projectignore_path}", file=sys.stderr)
    else:
        print(f".projectignoreファイルは既に存在します: {projectignore_path}", file=sys.stderr)


def main(
    folder_path: str,
    excluded_extensions: List[str],
    prompt_template: str,
    dry_run: bool,
):
    """
    メイン関数。指定されたフォルダ内のファイルを分析し、説明を生成する。

    Args:
        folder_path (str): 分析するフォルダのパス
        excluded_extensions (List[str]): 除外する拡張子のリスト
        prompt_template (str): 説明生成に使用するプロンプトのテンプレート
        dry_run (bool): .projectignoreファイルの作成と対象ファイルのリスト出力のみを行うかどうか
    """
    start_time = time.time()

    # 出力ディレクトリの設定
    output_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.path.basename(folder_path)
    )
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "summary.md")

    gitignore_spec = read_gitignore(folder_path)

    if dry_run:
        create_projectignore(output_dir)
        try:
            projectignore_spec = read_projectignore(output_dir)
        except FileNotFoundError:
            projectignore_spec = pathspec.PathSpec.from_lines("gitwildmatch", [])
    else:
        try:
            projectignore_spec = read_projectignore(output_dir)
        except FileNotFoundError:
            print("エラー: .projectignoreファイルが見つかりません。", file=sys.stderr)
            print("最初にdry-runオプションを実行して.projectignoreファイルを作成してください。", file=sys.stderr)
            return

        client = anthropic.Client(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    target_files = []
    ignored_by_gitignore = []
    ignored_by_projectignore = []
    excluded_files = []
    non_text_files = []
    empty_files = []
    ignored_by_projectignore = []

    print("ファイルをスキャン中...", file=sys.stderr)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        rel_root = os.path.relpath(root, folder_path)

        # ディレクトリのチェック
        dirs[:] = [
            d
            for d in dirs
            if not is_ignored_by_gitignore(
                os.path.join(root, d), gitignore_spec, folder_path
            )
        ]
        for d in dirs[:]:
            if is_ignored_by_projectignore(
                os.path.join(root, d), projectignore_spec, folder_path
            ):
                ignored_by_projectignore.append(os.path.join(rel_root, d))
                dirs.remove(d)

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, folder_path)
            file_extension = os.path.splitext(file)[1][1:].lower()

            if is_ignored_by_gitignore(file_path, gitignore_spec, folder_path):
                ignored_by_gitignore.append(relative_path)
                continue

            if is_ignored_by_projectignore(file_path, projectignore_spec, folder_path):
                ignored_by_projectignore.append(relative_path)
                continue

            if file_extension in excluded_extensions:
                excluded_files.append(relative_path)
                continue

            if not is_text_file(file_path):
                non_text_files.append(relative_path)
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as test_file:
                    content = test_file.read()
                    if not content.strip():
                        empty_files.append(relative_path)
                        continue

                target_files.append(file_path)  # 絶対パスで保存
            except Exception as e:
                print(
                    f"ファイル {relative_path} の処理中にエラーが発生しました: {str(e)}", file=sys.stderr
                )

    print(f"\n処理対象となるファイル数: {len(target_files)}", file=sys.stderr)
    print(f"除外されたファイル数:")
    print(f"  .gitignoreにより無視: {len(ignored_by_gitignore)}")
    print(f"  .projectignoreにより無視: {len(ignored_by_projectignore)}")
    print(f"  除外された拡張子: {len(excluded_files)}")
    print(f"  テキストファイルではない: {len(non_text_files)}")
    print(f"  空のファイル: {len(empty_files)}")

    if dry_run:
        print("\n対象ファイルのリスト:")
        for file in target_files:
            print(os.path.relpath(file, folder_path))

        print("\n除外されたファイルの詳細:")
        print("\n.projectignoreにより無視されたファイル・フォルダ:")
        for file in ignored_by_projectignore:
            print(f"  {file}")
        print("\n除外された拡張子のファイル:")
        for file in excluded_files:
            print(f"  {file}")
        print("\nテキストファイルではないファイル:")
        for file in non_text_files:
            print(f"  {file}")
        print("\n空のファイル:")
        for file in empty_files:
            print(f"  {file}")

        print("\ndry-runが完了しました。.projectignoreファイルを編集し、本実行を行ってください。", file=sys.stderr)
    else:
        with open(output_file, "w", encoding="utf-8") as f:
            print("ファイル構造を生成中...", file=sys.stderr)
            file_tree = get_file_tree(folder_path, gitignore_spec, projectignore_spec)
            f.write("# Project Structure\n\n")
            f.write(file_tree)
            f.write("\n\n# File Descriptions\n\n")

            print("ファイルの説明を生成中...", file=sys.stderr)
            for file_path in target_files:
                try:
                    relative_path = os.path.relpath(file_path, folder_path)
                    description = get_file_description(
                        client, file_path, folder_path, prompt_template
                    )
                    print(f"  処理完了: {relative_path}", file=sys.stderr)
                    f.write(f"{description}\n")
                except Exception as e:
                    relative_path = os.path.relpath(file_path, folder_path)
                    print(f"  エラー発生: {relative_path} - {str(e)}", file=sys.stderr)

        print(f"\n処理が完了しました。結果は {output_file} に保存されています。", file=sys.stderr)

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\n実行時間: {execution_time:.2f} 秒", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="指定されたフォルダ内のファイルの説明を生成します。")
    parser.add_argument("folder_path", help="分析するフォルダのパス")
    parser.add_argument("--exclude", nargs="*", default=[], help="除外する拡張子のリスト")
    parser.add_argument(
        "--prompt",
        default="""
あなたは、プログラミングファイルの内容を分析し、その構造と機能を簡潔に説明するAIアシスタントです。以下の指示に従って、与えられたファイルの内容を分析し、Markdown形式で説明を提供してください。

まず、分析対象のファイル内容を以下に示します：

<file_content>
{content}
</file_content>

このファイルの内容を注意深く分析し、以下の手順で説明を作成してください：

1. ファイル全体の概要を把握します。
2. インポートされているモジュールを特定します。
3. 定義されている関数を見つけ、各関数の目的を理解します。

分析が完了したら、以下の形式でMarkdown形式の説明を提供してください：

<answer>
### File Description
ファイルの全体的な説明を2〜5文程度で記述してください。ファイルの主な目的、機能、および重要な特徴を含めてください。

### Imported Modules
- モジュール1
- モジュール2
（以下、インポートされているすべてのモジュールをリストアップしてください）

### Functions
- 関数名1: 簡潔な説明（1-2文）
- 関数名2: 簡潔な説明（1-2文）
（以下、ファイル内のすべての関数について同様に記述してください）
</answer>

注意事項：
- 説明は日本語で提供してください。
- ファイルの内容を正確に反映させ、重要な情報を漏らさないようにしてください。
- 専門用語や技術的な概念については、可能な限り分かりやすく説明してください。
- 関数の説明は簡潔でありながら、その主な目的や機能が伝わるようにしてください。
- コメントや文字列内の日本語はそのまま使用し、適切に説明に組み込んでください。

以上の指示に従って、与えられたファイルの内容を分析し、Markdown形式の説明を提供してください。
""",
        help="説明生成に使用するプロンプトのテンプレート",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help=".projectignoreファイルの作成と対象ファイルのリスト出力のみを行う"
    )

    args = parser.parse_args()

    if not args.dry_run and not os.environ.get("ANTHROPIC_API_KEY"):
        raise ValueError("ANTHROPIC_API_KEYが設定されていません。環境変数を設定してください。")

    main(args.folder_path, args.exclude, args.prompt, args.dry_run)
