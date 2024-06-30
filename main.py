import os
import sys
import ast
import argparse
import anthropic
import pathspec
import chardet
from typing import List, Set


def read_gitignore(folder_path: str) -> pathspec.PathSpec:
    """
    指定されたフォルダ内の.gitignoreファイルを読み込み、PathSpecオブジェクトを返します。
    .gitディレクトリとnode_modulesを常に除外するパターンも追加します。

    :param folder_path: .gitignoreファイルを探すフォルダのパス
    :return: PathSpecオブジェクト
    """
    gitignore_path = os.path.join(folder_path, ".gitignore")
    patterns = [".git/", "node_modules/"]  # .gitディレクトリとnode_modulesを常に除外
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            patterns.extend(f.read().splitlines())
    return pathspec.PathSpec.from_lines("gitwildmatch", patterns)


def is_ignored(path: str, gitignore_spec: pathspec.PathSpec, base_path: str) -> bool:
    """
    指定されたパスが無視すべきかどうかを判断します。

    :param path: チェックするパス
    :param gitignore_spec: PathSpecオブジェクト
    :param base_path: プロジェクトのベースパス
    :return: パスが無視すべき場合はTrue、そうでない場合はFalse
    """
    rel_path = os.path.relpath(path, base_path)
    return gitignore_spec.match_file(rel_path)


def get_file_tree(folder_path: str, gitignore_spec: pathspec.PathSpec) -> str:
    """
    指定されたフォルダのファイル構造をツリー形式で返します。
    .gitディレクトリとnode_modulesは除外されます。

    :param folder_path: ツリーを生成するフォルダのパス
    :param gitignore_spec: PathSpecオブジェクト
    :return: ツリー形式のファイル構造を表す文字列
    """
    tree = []
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [
            d
            for d in dirs
            if not is_ignored(os.path.join(root, d), gitignore_spec, folder_path)
        ]
        level = root.replace(folder_path, "").count(os.sep)
        indent = "  " * level
        tree.append(f"{indent}{os.path.basename(root)}/")
        for file in files:
            if not is_ignored(os.path.join(root, file), gitignore_spec, folder_path):
                tree.append(f"{indent}  {file}")
    return "\n".join(tree)


def is_text_file(file_path: str, sample_size: int = 1024) -> bool:
    """
    ファイルがテキストファイルかどうかを判断します。

    :param file_path: チェックするファイルのパス
    :param sample_size: 読み込むサンプルサイズ（バイト）
    :return: テキストファイルの場合はTrue、そうでない場合はFalse
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

        # テキストとして解読できるかチェック
        sample.decode(result["encoding"])
        return True
    except (UnicodeDecodeError, IOError):
        return False


def is_binary_file(file_path: str) -> bool:
    """
    ファイルがバイナリファイルかどうかを判断します。

    :param file_path: チェックするファイルのパス
    :return: バイナリファイルの場合はTrue、そうでない場合はFalse
    """
    return not is_text_file(file_path)


def get_functions(file_path: str) -> List[str]:
    """
    指定されたPythonファイル内の関数名のリストを返します。

    :param file_path: 分析するPythonファイルのパス
    :return: ファイル内の関数名のリスト
    """
    with open(file_path, "r") as f:
        content = f.read()

    functions = []
    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
    except:
        pass  # ファイルがPythonでない場合や解析エラーの場合は無視
    return functions


def get_file_description(
    client: anthropic.Client, file_path: str, functions: List[str], prompt_template: str
) -> str:
    # return "test"
    """
    指定されたファイルの内容を分析し、AIを使用して説明を生成します。

    :param client: Anthropic APIクライアント
    :param file_path: 分析するファイルのパス
    :param functions: ファイル内の関数名のリスト
    :param prompt_template: 説明生成に使用するプロンプトのテンプレート
    :return: 生成された説明文
    """
    with open(file_path, "r") as f:
        content = f.read()

    prompt = prompt_template.format(functions=", ".join(functions), content=content)

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text


def main(
    folder_path: str,
    output_file: str,
    excluded_extensions: List[str],
    prompt_template: str,
    dry_run: bool,
):
    gitignore_spec = read_gitignore(folder_path)
    if not dry_run:
        client = anthropic.Client(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    target_files = []
    ignored_files = []
    excluded_files = []
    non_text_files = []
    empty_files = []

    print("ファイルをスキャン中...", file=sys.stderr)
    for root, dirs, files in os.walk(folder_path, topdown=True):
        dirs[:] = [
            d
            for d in dirs
            if not is_ignored(os.path.join(root, d), gitignore_spec, folder_path)
        ]
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1][1:].lower()

            if is_ignored(file_path, gitignore_spec, folder_path):
                ignored_files.append(file_path)
                continue

            if file_extension in excluded_extensions:
                excluded_files.append(file_path)
                continue

            if not is_text_file(file_path):
                non_text_files.append(file_path)
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as test_file:
                    content = test_file.read()
                    if not content.strip():
                        empty_files.append(file_path)
                        continue

                target_files.append(file_path)
            except Exception as e:
                print(f"ファイル {file_path} の処理中にエラーが発生しました: {str(e)}", file=sys.stderr)

    print(f"\n処理対象となるファイル数: {len(target_files)}", file=sys.stderr)
    print(f"除外されたファイル数:")
    print(f"  .gitignoreにより無視: {len(ignored_files)}")
    print(f"  除外された拡張子: {len(excluded_files)}")
    print(f"  テキストファイルではない: {len(non_text_files)}")
    print(f"  空のファイル: {len(empty_files)}")

    if dry_run:
        print("\n対象ファイルのリスト:")
        for file in target_files:
            print(file)

        print("\n除外されたファイルの詳細:")
        print("\n.gitignoreにより無視されたファイル:")
        for file in ignored_files:
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
    else:
        with open(output_file, "w", encoding="utf-8") as f:
            print("ファイル構造を生成中...", file=sys.stderr)
            file_tree = get_file_tree(folder_path, gitignore_spec)
            f.write(file_tree)
            f.write("\n\n")

            print("ファイルの説明を生成中...", file=sys.stderr)
            for file_path in target_files:
                try:
                    functions = get_functions(file_path)
                    description = get_file_description(
                        client, file_path, functions, prompt_template
                    )
                    print(f"  処理完了: {file_path}", file=sys.stderr)
                    f.write(f"\n{file_path}:\n{description}\n")
                except Exception as e:
                    print(f"  エラー発生: {file_path} - {str(e)}", file=sys.stderr)

        print(f"\n処理が完了しました。結果は {output_file} に保存されています。", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="指定されたフォルダ内のファイルの説明を生成します。")
    parser.add_argument("folder_path", help="分析するフォルダのパス")
    parser.add_argument("--output", default="output.txt", help="出力ファイルの名前")
    parser.add_argument("--exclude", nargs="*", default=[], help="除外する拡張子のリスト")
    parser.add_argument(
        "--prompt",
        default="""
Human: ファイルの内容を分析し、以下の形式で説明を提供してください：

1. ファイルの全体的な説明
2. PythonまたはTypeScriptファイルの場合、インポートされているモジュールのリスト
3. 以下の各関数の簡潔な説明（1-2文）：
{functions}

ファイルの内容：

{content}

Assistant: ファイルの内容を分析し、要求された形式で説明を提供いたします。

1. ファイルの全体的な説明:
[ファイルの全体的な説明をここに記述]

2. インポートされているモジュール:
[インポートされているモジュールのリストをここに記述]

3. 関数の説明:
[各関数の簡潔な説明をここに記述]
""",
        help="説明生成に使用するプロンプトのテンプレート",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="LLM処理を実行せずに対象ファイルのリストを出力"
    )

    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise ValueError("ANTHROPIC_API_KEYが設定されていません。環境変数を設定してください。")

    main(args.folder_path, args.output, args.exclude, args.prompt, args.dry_run)
