# Project Structure

- nike-ChatVRM/
  - tailwind.config.js
  - LICENSE
  - output_sorted.json
  - Dockerfile
  - next.config.js
  - electron.mjs
  - input_sorted.json
  - test.py
  - README.md
  - .gitignore
  - package-lock.json
  - package.json
  - .env
  - watch.json
  - tsconfig.json
  - docker-compose.yml
  - postcss.config.js
  - .eslintrc.json
  - locales/
    - ja/
      - translation.json
    - zh/
      - translation.json
    - ko/
      - translation.json
    - en/
      - translation.json
  - docs/
    - vrm_licence_en.md
    - vrm_licence_zh.md
    - summary.md
    - logo_licence_ko.md
    - README_ko.md
    - logo_licence_zh.md
    - logo_licence_en.md
    - README_en.md
    - README_zh.md
    - logo_licence.md
    - vrm_licence.md
    - vrm_licence_ko.md
  - .next/
  - public/
    - ogp.png
    - bg-c.png
    - github-mark-white.svg
    - AvatarSample_B.vrm
    - AvatarSample_B_old.vrm
    - idle_loop.vrma
  - scripts/
    - analyze_issue.py
  - .github/
    - workflows/
      - issue-analyzer.yml
      - nextjs.yml
  - .git/
  - src/
    - features/
      - emoteController/
        - expressionController.ts
        - emoteConstants.ts
        - autoLookAt.ts
        - autoBlink.ts
        - emoteController.ts
      - lipSync/
        - lipSyncAnalyzeResult.ts
        - lipSync.ts
      - messages/
        - speakCharacter.ts
        - messages.ts
        - synthesizeStyleBertVITS2.ts
        - synthesizeVoiceGoogle.ts
        - synthesizeVoice.ts
      - chat/
        - localLLMChat.ts
        - anthropicChat.ts
        - openAiChat.ts
        - googleChat.ts
        - groqChat.ts
        - difyChat.ts
        - aiChatFactory.ts
      - constants/
        - systemPromptConstants.ts
        - koeiroParam.ts
      - vrmViewer/
        - viewerContext.ts
        - model.ts
        - viewer.ts
      - youtube/
        - conversationContinuityFunctions.ts
        - youtubeComments.ts
      - googletts/
        - googletts.ts
      - koeiromap/
        - koeiromap.ts
    - utils/
      - reduceTalkStyle.ts
      - englishToJapanese.json
      - wait.ts
      - buildUrl.ts
    - styles/
      - globals.css
    - components/
      - settings.tsx
      - chatLog.tsx
      - messageInput.tsx
      - link.tsx
      - speakers.json
      - meta.tsx
      - textButton.tsx
      - assistantText.tsx
      - codeLog.tsx
      - menu.tsx
      - messageInputContainer.tsx
      - iconButton.tsx
      - githubLink.tsx
      - introduction.tsx
      - vrmViewer.tsx
    - lib/
      - i18n.js
      - VRMAnimation/
        - VRMAnimation.ts
        - VRMAnimationLoaderPluginOptions.ts
        - VRMAnimationLoaderPlugin.ts
        - loadVRMAnimation.ts
        - VRMCVRMAnimation.ts
        - utils/
          - linearstep.ts
          - saturate.ts
          - arrayChunk.ts
      - VRMLookAtSmootherLoaderPlugin/
        - VRMLookAtSmoother.ts
        - VRMLookAtSmootherLoaderPlugin.ts
    - pages/
      - index.tsx
      - _document.tsx
      - _app.tsx
      - api/
        - anthropic.ts
        - chat.ts
        - groq.ts
        - google.ts
        - tts.ts
        - stylebertvits2.ts

# File Descriptions


## tailwind.config.js

以下は要求された形式でのMarkdown形式の説明です：

### File Description
このファイルはTailwind CSSの設定ファイルです。カスタムテーマ、カラーパレット、フォントファミリー、およびプラグインの設定が含まれています。また、@charcoal-ui/themeと@charcoal-ui/tailwind-configモジュールを使用してベースの設定を行っています。

### Imported Modules
- @charcoal-ui/theme
- @charcoal-ui/tailwind-config

### Functions
- createTailwindConfig: Tailwind CSSの設定を生成するための関数。バージョンとテーマ設定を受け取ります。

### Configuration
- darkMode: ダークモードを有効化
- content: スタイルを適用するファイルのパスを指定
- presets: createTailwindConfigを使用してベース設定を生成
- theme.extend.colors: カスタムカラーパレットを定義
- theme.extend.fontFamily: カスタムフォントファミリーを定義
- plugins: @tailwindcss/line-clampプラグインを追加

このファイルには特定の関数定義は含まれていませんが、モジュールのエクスポートとTailwind CSSの設定オブジェクトの定義が主な内容となっています。


## Dockerfile

以下にMarkdown形式で、指定されたファイルの分析結果を提供します：

### File Description
このファイルはDockerfileで、Node.jsアプリケーションのコンテナ化を定義しています。Node.js 16をベースイメージとして使用し、アプリケーションの依存関係をインストールし、ソースコードをコピーしてビルドを行い、最後にアプリケーションを起動するための設定が含まれています。

### Imported Modules
このDockerfileには外部モジュールのインポートは含まれていません。

### Functions
Dockerfileには関数は含まれていませんが、主要なステップは以下の通りです：

- FROM: ベースイメージを指定（node:16）
- WORKDIR: 作業ディレクトリを設定（/app）
- COPY: ファイルをコンテナにコピー
- RUN: コマンドを実行（依存関係のインストールとビルド）
- EXPOSE: 公開するポートを指定（3000）
- CMD: コンテナ起動時に実行するコマンドを指定（npm start）


## next.config.js

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはNext.jsの設定ファイル（`next.config.js`）です。アプリケーションの様々な挙動を制御するための設定オプションが含まれています。環境変数`BASE_PATH`を使用してベースパスを設定し、フォント最適化を無効にするなどの設定が行われています。

### Imported Modules
- 明示的なモジュールのインポートはありません。

### Functions
このファイルには明示的な関数定義はありません。代わりに、Next.jsの設定オブジェクトが定義されています：

- `nextConfig`: Next.jsアプリケーションの設定オプションを含むオブジェクト。以下の設定が含まれています：
  - `reactStrictMode`: Reactの厳格モードを有効化
  - `assetPrefix`: アセットのプレフィックスを設定
  - `basePath`: アプリケーションのベースパスを設定
  - `trailingSlash`: URLの末尾にスラッシュを追加
  - `publicRuntimeConfig`: 公開ランタイム設定を定義
  - `optimizeFonts`: フォントの最適化を無効化

最後に、`module.exports`を使用して`nextConfig`オブジェクトをエクスポートしています。


## electron.mjs

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはElectronアプリケーションのメインプロセスを定義しています。アプリケーションウィンドウの作成、設定、そして開発モードと本番モードの区別を行っています。セキュリティ設定やウィンドウの外観カスタマイズも含まれています。

### Imported Modules
- electron (app, BrowserWindow, screen)
- path
- url (fileURLToPath)
- electron-is-dev
- wait-on

### Functions
- createWindow: メインウィンドウを作成し、設定を適用します。開発モードではローカルサーバーの準備を待ち、本番モードではHTMLファイルを直接ロードします。

### Key Features
- ウィンドウサイズはプライマリディスプレイのワークエリアに合わせて設定
- セキュリティ強化のための設定（nodeIntegration: false, contextIsolation: true）
- 開発モードと本番モードの区別（electron-is-devを使用）
- ウィンドウの透明化、影の除去などの外観カスタマイズ
- 開発者ツールの無効化（本番環境向け）
- 'ready-to-show'イベントを使用したウィンドウの遅延表示


## package.json

以下は要求された形式でのMarkdown形式の説明です：

### File Description
このファイルは、Node.jsプロジェクトの`package.json`ファイルです。プロジェクト名は"chat-vrm"で、バージョン0.1.0のプライベートプロジェクトです。開発、ビルド、デプロイメント用のスクリプトが定義されており、必要な依存関係とdevDependenciesが列挙されています。

### Imported Modules
このファイルは直接モジュールをインポートしていませんが、プロジェクトの依存関係を以下のように定義しています：

- 主要な依存関係:
  - next
  - react
  - react-dom
  - three
  - openai
  - @google/generative-ai
  - i18next
  - など

- 開発用依存関係:
  - typescript
  - tailwindcss
  - electron
  - @types/react
  - など

### Functions
`package.json`ファイルは関数を直接定義しませんが、以下のNPMスクリプトが定義されています：

- dev: 開発サーバーを起動
- build: プロジェクトをビルド
- start: ビルドしてから起動
- export: 静的ファイルをエクスポート
- lint: コードのリント
- electron: Electronアプリケーションを起動
- desktop: 開発サーバーとElectronアプリを同時に起動

これらのスクリプトはプロジェクトの開発、ビルド、デプロイメントプロセスを自動化するために使用されます。


## watch.json

この内容に基づいて、Markdown形式の説明を以下に提供します：

### File Description
このファイルは、プロジェクトの設定を定義するJSONファイルです。主に、インストール時に含めるファイル、再起動時に監視するファイル、およびスロットル時間を指定しています。おそらく、開発環境や自動デプロイメントプロセスで使用される設定ファイルだと考えられます。

### Imported Modules
このJSONファイルには直接的なモジュールのインポートはありません。

### Functions
このJSONファイルには関数定義は含まれていません。代わりに、以下の主要な設定項目があります：

- install: インストールプロセスに含めるファイルを指定
- restart: 再起動をトリガーする監視対象ファイルを指定
- throttle: 操作の頻度を制限するためのスロットル時間を設定（ミリ秒単位）


## tsconfig.json

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはTypeScriptの設定ファイル（tsconfig.json）です。Next.jsプロジェクトで使用される典型的な設定が含まれており、TypeScriptのコンパイラオプションやプロジェクトの構造に関する設定が定義されています。

### Imported Modules
このファイルは設定ファイルであるため、モジュールのインポートは含まれていません。

### Functions
このファイルは設定ファイルであるため、関数の定義は含まれていません。

代わりに、主要な設定項目を以下に列挙します：

- compilerOptions: TypeScriptコンパイラの動作を制御する様々なオプションを設定
  - target: コンパイル後のJavaScriptのバージョンを指定（ES2015）
  - lib: 使用するライブラリファイルを指定
  - strict: 厳格な型チェックを有効化
  - jsx: JSXのコンパイル方法を指定
  - paths: モジュールのインポートパスのエイリアスを設定

- include: コンパイル対象のファイルパターンを指定
- exclude: コンパイル対象から除外するファイルパターンを指定

この設定ファイルは、Next.jsプロジェクトでTypeScriptを使用する際の標準的な設定を提供しており、開発環境の一貫性と型安全性を確保するために重要な役割を果たしています。


## docker-compose.yml

以下は、指定されたファイルの分析結果をMarkdown形式で説明したものです：

### File Description
このファイルはDocker Composeの設定ファイルです。バージョン3の構文を使用しており、`app`という名前のサービスを定義しています。このサービスはDockerコンテナとしてアプリケーションを実行するための設定を含んでいます。

### Imported Modules
このファイルは設定ファイルであるため、直接的なモジュールのインポートはありません。

### Functions
このファイルは設定ファイルであるため、関数の定義はありません。代わりに、以下のような主要な設定項目が含まれています：

- `build`: カレントディレクトリ（`.`）からDockerイメージをビルドするよう指定しています。
- `ports`: ホストの3000ポートをコンテナの3000ポートにマッピングしています。
- `volumes`: カレントディレクトリをコンテナ内の`/app`ディレクトリにマウントしています。
- `env_file`: `.env`ファイルから環境変数を読み込むよう指定しています。


## postcss.config.js

以下にMarkdown形式で、指定されたファイルの分析結果を提供します：

### File Description
このファイルは、PostCSSの設定ファイルです。TailwindCSSとAutoprefixerプラグインを使用するように設定されています。これは一般的にウェブ開発プロジェクトで使用され、CSSの処理とスタイリングを効率化します。

### Imported Modules
このファイルには直接的なモジュールのインポートはありません。

### Functions
このファイルには関数の定義はありません。

### Additional Notes
- このファイルは`module.exports`を使用してオブジェクトをエクスポートしています。
- `plugins`オブジェクト内で、TailwindCSSとAutoprefixerが設定されています。
- 空のオブジェクト（`{}`）は、これらのプラグインがデフォルト設定で使用されることを示しています。


## src/features/emoteController/expressionController.ts

以下にMarkdown形式で説明を提供します：

### File Description
このファイルは3DキャラクターのVRM（Virtual Reality Model）の表情を制御するためのExpressionControllerクラスを定義しています。感情表現、リップシンク、自動まばたき、自動視線制御などの機能を管理し、滑らかな表情の遷移を実現します。

### Imported Modules
- THREE from "three"
- VRM, VRMExpressionManager, VRMExpressionPresetName from "@pixiv/three-vrm"
- AutoLookAt from "./autoLookAt"
- AutoBlink from "./autoBlink"

### Functions
- constructor: VRMモデルとカメラオブジェクトを受け取り、ExpressionControllerを初期化します。
- playEmotion: 指定された表情プリセットを再生し、前の表情をリセットします。
- lipSync: リップシンク（口の動き）を設定します。
- update: 自動まばたきとリップシンクの更新を行います。

このクラスは、VRMモデルの表情を滑らかに制御し、自然な感情表現やリップシンクを実現するための重要な役割を果たしています。


## src/features/emoteController/emoteConstants.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、瞬きに関連する定数を定義しています。目を閉じている最大時間と開いている最大時間を秒単位で指定しています。これらの定数は、おそらく瞬きの検出や分析に使用されるものと思われます。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
このファイルには関数の定義はありません。

### Constants
- BLINK_CLOSE_MAX: 瞬きで目を閉じている最大時間（秒）を定義しています。値は0.12秒です。
- BLINK_OPEN_MAX: 瞬きで目を開いている最大時間（秒）を定義しています。値は5秒です。

これらの定数は `export` キーワードを使用して定義されており、他のファイルからインポートして使用できるようになっています。


## src/features/emoteController/autoLookAt.ts

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルはThree.jsとVRMを使用して、3Dキャラクターの目線制御を行うクラス`AutoLookAt`を定義しています。VRMモデルのLookAt機能を利用して、カメラに追加されたターゲットオブジェクトに対して目線を向けるように設定しています。

### Imported Modules
- THREE from "three"
- VRM from "@pixiv/three-vrm"

### Functions
- constructor(vrm: VRM, camera: THREE.Object3D): `AutoLookAt`クラスのコンストラクタ。VRMモデルとカメラオブジェクトを受け取り、目線のターゲットを設定します。

### Classes
- AutoLookAt: 目線を制御するクラス。VRMモデルの目線をカメラに追加されたターゲットオブジェクトに向けるように設定します。


## src/features/emoteController/autoBlink.ts

以下はファイルの分析結果です：

### File Description
このファイルは自動瞬きを制御するための`AutoBlink`クラスを定義しています。VRMモデルの表情管理を利用して、瞬きの開閉を制御し、自動瞬きの有効/無効を切り替える機能を提供しています。

### Imported Modules
- @pixiv/three-vrm (VRMExpressionManager)
- ./emoteConstants (BLINK_CLOSE_MAX, BLINK_OPEN_MAX)

### Functions
- constructor: AutoBlinkクラスのインスタンスを初期化します。
- setEnable: 自動瞬きの有効/無効を設定し、目が開くまでの時間を返します。
- update: 瞬きの状態を更新します。時間経過に応じて目の開閉を制御します。
- close: 目を閉じる処理を行います。
- open: 目を開く処理を行います。

このクラスは、VRMモデルの表情管理を使用して瞬きを制御し、自然な目の動きを実現するためのものです。自動瞬きの有効/無効切り替えや、目の開閉状態の管理、時間に基づいた瞬きの更新などの機能を提供しています。


## src/features/emoteController/emoteController.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、VRMモデルの感情表現を制御するための`EmoteController`クラスを定義しています。主にExpressionの操作を行い、VRMの表情や口の動きを制御するためのインターフェースを提供しています。

### Imported Modules
- three (as THREE)
- @pixiv/three-vrm (VRM, VRMExpressionPresetName)
- ./expressionController (ExpressionController)

### Functions
- constructor: VRMモデルとカメラオブジェクトを受け取り、ExpressionControllerを初期化します。
- playEmotion: 指定された表情プリセットを再生します。
- lipSync: リップシンク（口の動き）を制御します。指定された表情プリセットと値を使用します。
- update: ExpressionControllerの状態を更新します。アニメーションのフレーム間の時間差を引数として受け取ります。


## src/features/lipSync/lipSyncAnalyzeResult.ts

以下は、提供されたファイル内容の分析結果です：

### File Description
このファイルは、リップシンク（口の動きと音声の同期）分析の結果を表すインターフェースを定義しています。現在は音量のみを含む簡素な構造ですが、将来的に拡張される可能性があります。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
このファイルには関数の定義はありません。

### Interfaces
- LipSyncAnalyzeResult: リップシンク分析の結果を表すインターフェース。現在は音量（volume）のみを数値型で保持しています。


## src/features/lipSync/lipSync.ts

以下は要求された形式での分析結果です：

### File Description
このファイルはLipSyncクラスを定義しています。このクラスは音声データを解析し、リップシンク（口の動き）に関連する情報を提供します。AudioContextとAnalyserNodeを使用して音声データを処理し、音量を計算してリップシンクの結果を生成します。また、ArrayBufferやURLから音声を再生する機能も含まれています。

### Imported Modules
- LipSyncAnalyzeResult (from "./lipSyncAnalyzeResult")

### Functions
- constructor: AudioContextを受け取り、AnalyserNodeと時間領域データ用の配列を初期化します。
- update: 現在の音声データを解析し、音量を計算してLipSyncAnalyzeResultを返します。
- playFromArrayBuffer: ArrayBufferから音声を再生し、オプションで再生終了時のコールバックを設定します。
- playFromURL: 指定されたURLから音声データを取得し、再生します。再生終了時のコールバックもオプションで設定可能です。


## src/features/messages/speakCharacter.ts

以下に、ご要望の形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、テキスト音声合成（TTS）機能を提供するモジュールです。複数のTTSサービス（KoeiroMap、VOICEVOX、Google TTS、StyleBertVITS2、GSVI TTS）をサポートし、3Dキャラクターモデルと連携して音声を再生する機能を実装しています。また、英語から日本語への変換機能も含まれています。

### Imported Modules
- wait (from "@/utils/wait")
- synthesizeVoiceApi (from "./synthesizeVoice")
- synthesizeVoiceGoogleApi (from "./synthesizeVoiceGoogle")
- synthesizeStyleBertVITS2Api (from "./synthesizeStyleBertVITS2")
- Viewer (from "../vrmViewer/viewer")
- Screenplay, Talk (from "./messages")
- englishToJapanese (from '@/utils/englishToJapanese.json')

### Functions
- createSpeakCharacter: キャラクターの発話機能を作成する関数。
- convertEnglishToJapaneseReading: 英語テキストを日本語読みに変換する関数。
- getGoogleTtsType: Google TTSの種類を選択する関数。
- getGppgleTtsType: 言語に基づいてGoogle TTSの種類を返す関数。
- fetchAudio: KoeiroMap APIを使用して音声を取得する関数。
- fetchAudioVoiceVox: VOICEVOX APIを使用して音声を取得する関数。
- fetchAudioGoogle: Google TTS APIを使用して音声を取得する関数。
- fetchAudioStyleBertVITS2: StyleBertVITS2 APIを使用して音声を取得する関数。
- testVoice: VOICEVOXを使用してテスト音声を再生する関数。
- fetchAudioVoiceGSVIApi: GSVI TTS APIを使用して音声を取得する関数。


## src/features/messages/messages.ts

以下は要求された形式でのMarkdown形式の説明です：

### File Description
このファイルは、VRMモデルの表情と発話を制御するための関数や型定義を含んでいます。ChatGPTのメッセージ形式、感情表現、発話スタイルなどを定義し、テキストを解析して適切な感情表現と発話スタイルを決定する機能を提供しています。

### Imported Modules
- @pixiv/three-vrm
- ../constants/koeiroParam

### Functions
- splitSentence: テキストを文章単位で分割する関数。
- textsToScreenplay: テキストの配列をScreenplay形式に変換する関数。感情タグを解析し、適切な表情と発話スタイルを設定します。
- emotionToTalkStyle: 感情タイプを対応する発話スタイルに変換する関数。

### Types and Interfaces
- Message: ChatGPT APIのメッセージ形式を定義する型。
- TalkStyle: 発話スタイルを定義する型。
- Talk: 発話内容と話者の位置情報を含む型。
- EmotionType: VRMモデルの感情表現を定義する型。
- Screenplay: 感情表現と発話内容をセットにした型。

このファイルは、テキストベースのコミュニケーションをVRMモデルの動作と表情に変換するための重要な機能を提供しています。


## src/features/messages/synthesizeStyleBertVITS2.ts

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、StyleBertVITS2 APIを使用して音声合成を行うための非同期関数を含んでいます。関数は指定されたパラメータを使用してAPIリクエストを構築し、サーバーに送信します。結果として得られるオーディオデータをArrayBufferとして返します。

### Imported Modules
このファイルには明示的なインポート文はありませんが、以下の組み込みAPIを使用しています：
- fetch: ネットワークリクエストを行うためのWeb API

### Functions
- synthesizeStyleBertVITS2Api: StyleBertVITS2 APIを使用して音声合成を行う非同期関数。指定されたメッセージ、サーバーURL、モデルID、スタイル、言語を使用してAPIリクエストを構築し、結果のオーディオデータを返します。エラーハンドリングも含まれています。


## src/features/messages/synthesizeVoiceGoogle.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、Google Text-to-Speech (TTS) APIを使用して音声合成を行うための関数を定義しています。非同期関数として実装され、指定されたメッセージとTTSタイプを使用してサーバーサイドAPIにリクエストを送信し、生成された音声データを取得します。

### Imported Modules
このファイルには明示的なモジュールのインポートは含まれていません。

### Functions
- synthesizeVoiceGoogleApi: Google TTS APIを利用して音声を合成する非同期関数。メッセージとTTSタイプを受け取り、サーバーサイドAPIにリクエストを送信して音声データを取得します。


## src/features/messages/synthesizeVoice.ts

以下は、指定された形式でのファイルの分析結果です：

### File Description
このファイルは音声合成機能を提供するモジュールです。`synthesizeVoice`と`synthesizeVoiceApi`という2つの非同期関数を含み、メッセージ、話者の位置、話し方のスタイルに基づいて音声を生成します。`synthesizeVoiceApi`関数はAPIキーを使用し、無料版向けに感情表現を制限する機能も備えています。

### Imported Modules
- `@/utils/reduceTalkStyle`から`reduceTalkStyle`
- `../koeiromap/koeiromap`から`koeiromapV0`
- `../messages/messages`から`TalkStyle`

### Functions
- synthesizeVoice: メッセージ、話者の位置、スタイルを基に音声を合成する関数。koeiromapV0を使用して音声データを生成します。
- synthesizeVoiceApi: APIを使用して音声を合成する関数。感情表現を制限し、サーバーにリクエストを送信して音声データを取得します。


## src/features/chat/localLLMChat.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、ローカルLLM（Large Language Model）とのチャット応答をストリーミング形式で取得する機能を提供しています。axiosを使用してHTTPリクエストを行い、受信したデータをストリーム処理して、チャンク単位で解析し、ReadableStreamとして返します。

### Imported Modules
- axios
- Message (from '../messages/messages')

### Functions
- getLocalLLMChatResponseStream: ローカルLLMにメッセージを送信し、応答をストリーミング形式で取得します。受信したデータを解析し、ReadableStreamとして返します。この関数は非同期で動作し、ストリームデータを逐次的に処理します。


## src/features/chat/anthropicChat.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはAnthropicのチャットAPIとのインタラクションを管理するための関数を含んでいます。非ストリーミングとストリーミングの両方のレスポンス取得方法を提供し、APIキーやモデル指定などのパラメータを柔軟に扱えるようになっています。

### Imported Modules
- `Message` from "../messages/messages"

### Functions
- `getAnthropicChatResponse`: Anthropic APIに非ストリーミングリクエストを送信し、レスポンスを取得する関数。
- `getAnthropicChatResponseStream`: Anthropic APIにストリーミングリクエストを送信し、リアルタイムでレスポンスを取得するための関数。ReadableStreamを返し、チャンク単位でデータを処理する。


## src/features/chat/openAiChat.ts

以下は要求された形式での分析結果です：

### File Description
このファイルはOpenAI APIを使用してチャット応答を生成するための関数を提供しています。通常の応答生成と、ストリーミング形式での応答生成の2つの主要な機能を含んでいます。OpenAIクライアントの初期化、APIリクエストの送信、応答の処理を行っています。

### Imported Modules
- OpenAI (from "openai")
- Message (from "../messages/messages")
- ChatCompletionMessageParam (from "openai/resources")

### Functions
- getOpenAIChatResponse: OpenAI APIを使用して単一の応答を生成する非同期関数。メッセージ履歴、APIキー、モデル名を受け取り、生成された応答を返します。

- getOpenAIChatResponseStream: OpenAI APIを使用してストリーミング形式で応答を生成する非同期関数。メッセージ履歴、APIキー、モデル名を受け取り、応答のストリームを返します。ReadableStreamを使用して、チャンク単位で応答を処理します。


## src/features/chat/googleChat.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはGoogle ChatのAPIを利用してチャット応答を取得するための関数を提供しています。通常の応答と、ストリーミング応答の2つの方法をサポートしています。また、メッセージの前処理を行う補助関数も含まれています。

### Imported Modules
- @google/generative-ai
- ../messages/messages

### Functions
- getGoogleChatResponse: Google ChatのAPIを使用して単一の応答を取得する非同期関数です。
- getGoogleChatResponseStream: Google ChatのAPIを使用してストリーミング形式で応答を取得する非同期関数です。
- processMessages: 入力メッセージを処理し、システムメッセージと会話履歴を適切な形式に変換する関数です。

各関数は、メッセージ履歴、APIキー、モデル名を入力として受け取り、Google Generative AIを使用して応答を生成します。ストリーミング版はReadableStreamを返し、リアルタイムでの応答の取得を可能にします。


## src/features/chat/groqChat.ts

以下は、提供されたファイルの分析結果です：

### File Description
このファイルは、Groq APIとの対話を処理するための関数を含んでいます。通常のレスポンスと、ストリーミングレスポンスの両方を扱う機能を提供しています。主にチャットボットやAI対話システムで使用されることを想定しています。

### Imported Modules
- Message (from "../messages/messages")

### Functions
- getGroqChatResponse: Groq APIに非ストリーミングのリクエストを送信し、レスポンスを取得します。
- getGroqChatResponseStream: Groq APIにストリーミングリクエストを送信し、レスポンスをReadableStreamとして返します。このストリームは受信したデータをリアルタイムで処理し、整形して返します。


## src/features/chat/difyChat.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、Dify APIを使用してチャットレスポンスのストリームを取得する機能を提供しています。APIキーを使用して認証し、メッセージをストリーミングモードで送信し、レスポンスを逐次的に処理します。また、会話IDの管理も行っています。

### Imported Modules
- Message（"../messages/messages"から）

### Functions
- getDifyChatResponseStream: Dify APIにリクエストを送信し、チャットレスポンスのストリームを取得します。APIキー、URL、メッセージ配列、会話ID、および会話IDを設定するコールバック関数を引数として受け取り、ReadableStreamを返します。この関数は非同期で動作し、ストリーミングレスポンスを処理して、メッセージの内容とコンバセーションIDを逐次的に提供します。


## src/features/chat/aiChatFactory.ts

以下はMarkdown形式の説明です：

### File Description
このファイルは、複数のAIサービス（OpenAI、Anthropic、Google、ローカルLLM、Groq、Dify）とのチャットインターフェースを提供するモジュールです。各サービスに対応するストリーム取得関数をインポートし、統一されたインターフェースを通じてこれらのサービスにアクセスする機能を提供しています。

### Imported Modules
- Message（@/features/messages/messages から）
- getOpenAIChatResponseStream（./openAiChat から）
- getAnthropicChatResponseStream（./anthropicChat から）
- getGoogleChatResponseStream（./googleChat から）
- getLocalLLMChatResponseStream（./localLLMChat から）
- getGroqChatResponseStream（./groqChat から）
- getDifyChatResponseStream（./difyChat から）

### Functions
- getAIChatResponseStream: 指定されたAIサービスに基づいて適切なチャットレスポンスストリームを取得する。サービス名、メッセージ配列、設定オブジェクトを受け取り、対応するストリーム取得関数を呼び出す。

### Types and Interfaces
- AIService: サポートされているAIサービスの名前を定義する型
- AIServiceConfig: 各AIサービスの設定情報を含むインターフェース


## src/features/constants/systemPromptConstants.ts

以下にファイルの内容を分析した結果をMarkdown形式で提供します：

### File Description
このファイルは、AI会話システムのためのシステムプロンプトを定義しています。プロンプトは、AIが人間らしく振る舞い、感情を込めて会話することを指示しています。また、会話の形式や例を提供し、AIの応答方法を具体的に説明しています。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
このファイルには関数の定義はありません。

### Constants
- SYSTEM_PROMPT: AIシステムに対する指示を含む文字列定数。この定数は、AIが会話中にどのように振る舞うべきか、感情をどのように表現するか、そして会話の形式や例を提供しています。

### Key Features
1. 5つの感情タイプ（neutral, happy, angry, sad, relaxed）の定義
2. 会話文の書式指定（[感情]{会話文}）
3. AIの発言例の提供
4. 返答に関する具体的な指示（1つの適切な会話文のみ返答、ですます調や敬語を使わない）

このファイルは、自然な会話を模倣するAIシステムの基本的な動作を規定するために使用されると考えられます。


## src/features/constants/koeiroParam.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、音声合成パラメータを定義するTypeScriptモジュールです。`KoeiroParam`型を定義し、デフォルトパラメータと4つのプリセットパラメータを設定しています。各パラメータは話者のX座標とY座標を表しています。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
このファイルには関数の定義はありません。代わりに、以下の定数が定義されています：

- `DEFAULT_PARAM`: デフォルトの話者パラメータを定義
- `PRESET_A`: プリセットAの話者パラメータを定義
- `PRESET_B`: プリセットBの話者パラメータを定義
- `PRESET_C`: プリセットCの話者パラメータを定義
- `PRESET_D`: プリセットDの話者パラメータを定義

各定数は`KoeiroParam`型のオブジェクトで、`speakerX`と`speakerY`プロパティを持ちます。


## src/features/vrmViewer/viewerContext.ts

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、React アプリケーションで使用される Viewer コンポーネントのコンテキストを設定しています。`Viewer` クラスのインスタンスを作成し、それを React の Context API を使用してアプリケーション全体で利用可能にしています。

### Imported Modules
- createContext (from react)
- Viewer (from "./viewer")

### Functions
このファイルには独立した関数定義はありませんが、以下の重要な操作が行われています：

- Viewer インスタンスの作成: 新しい `Viewer` オブジェクトを作成します。
- ViewerContext の作成: `createContext` を使用して、`viewer` オブジェクトを含む新しいコンテキストを作成します。


## src/features/vrmViewer/model.ts

以下に、要求された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは3Dキャラクターを管理するModelクラスを定義しています。VRMモデルの読み込み、アニメーションの適用、リップシンク、感情表現などの機能を提供し、3Dキャラクターの総合的な制御を行います。

### Imported Modules
- THREE from "three"
- VRM, VRMLoaderPlugin, VRMUtils from "@pixiv/three-vrm"
- GLTFLoader from "three/examples/jsm/loaders/GLTFLoader"
- VRMAnimation from "../../lib/VRMAnimation/VRMAnimation"
- VRMLookAtSmootherLoaderPlugin from "@/lib/VRMLookAtSmootherLoaderPlugin/VRMLookAtSmootherLoaderPlugin"
- LipSync from "../lipSync/lipSync"
- EmoteController from "../emoteController/emoteController"
- Screenplay from "../messages/messages"

### Functions
- constructor: Modelクラスのインスタンスを初期化し、LipSyncオブジェクトを作成します。
- loadVRM: 指定されたURLからVRMモデルを非同期で読み込み、初期化します。
- unLoadVrm: 現在のVRMモデルをアンロードし、メモリを解放します。
- loadAnimation: VRMアニメーションを読み込み、再生を開始します。
- speak: 音声バッファを再生し、指定された表情でリップシンクを行います。
- update: モデルの状態を更新し、リップシンク、感情表現、アニメーションを進行させます。


## src/features/vrmViewer/viewer.ts

以下はMarkdown形式での分析結果です：

### File Description
このファイルは、Three.jsを使用した3Dビューワーを実装するためのViewerクラスを定義しています。VRMモデルのロード、アニメーション、カメラ制御、レンダリングなどの機能を提供し、Reactアプリケーションで使用することを想定しています。

### Imported Modules
- THREE from "three"
- Model from "./model"
- loadVRMAnimation from "@/lib/VRMAnimation/loadVRMAnimation"
- buildUrl from "@/utils/buildUrl"
- OrbitControls from "three/examples/jsm/controls/OrbitControls"

### Functions
- constructor: Viewerクラスのインスタンスを初期化し、シーン、ライト、クロックを設定します。
- loadVrm: 指定されたURLからVRMモデルをロードし、シーンに追加します。
- unloadVRM: 現在ロードされているVRMモデルをシーンから削除します。
- setup: Reactで管理されているCanvasを設定し、レンダラー、カメラ、コントロールを初期化します。
- resize: キャンバスのサイズをその親要素に合わせてリサイズします。
- resetCamera: VRMモデルのヘッドノードを基準にカメラ位置を調整します。
- update: アニメーションフレームごとにモデルの更新とシーンのレンダリングを行います。

このクラスは、3Dモデルのインタラクティブな表示と操作を可能にし、WebGLを使用してブラウザ上で高度な3Dグラフィックスを実現します。


## src/features/youtube/conversationContinuityFunctions.ts

以下はMarkdown形式での分析結果です：

### File Description
このファイルは、AI対話システムのための様々な機能を提供するユーティリティ関数群を含んでいます。OpenAIとAnthropicのAIサービスを利用して、会話の継続、新しい話題の生成、最適なコメントの選択などの機能を実装しています。

### Imported Modules
- Message from "@/features/messages/messages"
- getOpenAIChatResponse from "@/features/chat/openAiChat"
- getAnthropicChatResponse from "@/features/chat/anthropicChat"

### Functions
- fetchAIResponse: 指定されたAIサービスとモデルを使用してレスポンスを取得します。
- getLastMessages: 指定された数の最新メッセージを取得し、文字列として返します。
- getModifiedSystemMessage: システムメッセージを受け取り、修正したメッセージを返します。
- getBestComment: ユーザーのコメントとYoutubeのコメントから最適なコメントを選択します。
- getMessagesForSleep: 休憩用のメッセージを生成します。
- getAnotherTopic: 最新の会話から関連する新しい話題を生成します。
- getMessagesForNewTopic: 新しい話題に基づいてメッセージを生成します。
- checkIfResponseContinuationIsRequired: 会話の続きが必要かどうかを判断します。
- getMessagesForContinuation: 会話を継続するためのメッセージを生成します。


## src/features/youtube/youtubeComments.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、YouTubeのライブチャットからコメントを取得し、AIを使用して会話を継続するための機能を提供しています。主な機能には、ライブチャットIDの取得、コメントの取得と処理、AIによる応答の生成が含まれます。また、コメントがない場合の対応や会話の継続性を維持するためのロジックも実装されています。

### Imported Modules
- Message (from "@/features/messages/messages")
- getBestComment, getMessagesForSleep, getAnotherTopic, getMessagesForNewTopic, checkIfResponseContinuationIsRequired, getMessagesForContinuation (from "@/features/youtube/conversationContinuityFunctions")

### Functions
- getLiveChatId: YouTubeのライブストリームIDからライブチャットIDを取得します。
- retrieveLiveComments: 指定されたライブチャットIDを使用して、YouTubeのライブコメントを取得します。
- fetchAndProcessComments: ライブコメントを取得し、AIを使用して処理します。会話の継続性を維持し、必要に応じて新しいトピックを生成したりスリープモードに移行したりします。


## src/features/googletts/googletts.ts

以下はリクエストされた形式でのMarkdown形式の説明です：

### File Description
このファイルはGoogle Cloud Text-to-Speech APIを使用して、テキストを音声に変換する機能を提供しています。非同期関数`googleTts`を定義し、指定されたメッセージとTTSタイプに基づいて音声を生成します。

### Imported Modules
- @google-cloud/text-to-speech

### Functions
- googleTts: Google Cloud Text-to-Speech APIを使用してテキストを音声に変換する非同期関数。指定されたメッセージとTTSタイプを受け取り、生成された音声データを返します。この関数は英語（米国）の女性の声を使用し、LINEAR16形式でオーディオを生成します。


## src/features/koeiromap/koeiromap.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、声の合成に関連する2つの関数を含んでいます。これらの関数は、メッセージテキスト、話者の位置、話し方のスタイルなどのパラメータを受け取り、APIリクエストを行って音声データを生成します。一つはkoeiromapV0 APIを、もう一つはkoeiromapFreeV1 APIを使用しています。

### Imported Modules
- TalkStyle (from "../messages/messages")

### Functions
- koeiromapV0: メッセージ、話者の位置、スタイルを入力として受け取り、koeiromapV0 APIを使用して音声を生成します。生成された音声データを返します。

- koeiromapFreeV1: メッセージ、話者の位置、スタイル、APIキーを入力として受け取り、koeiromapFreeV1 APIを使用して音声を生成します。生成された音声データを返します。このバージョンでは、より多くのスタイルオプションと出力フォーマットの指定が可能です。


## src/utils/reduceTalkStyle.ts

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、koeiromap Free v1の制限に対応した声色パラメータを処理するためのTypeScriptコードを含んでいます。ReducedTalkStyleという型定義と、reduceTalkStyleという関数が定義されています。これらは、入力された声色パラメータを制限された選択肢に変換するために使用されます。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
- reduceTalkStyle: 入力された声色パラメータを "talk"、"happy"、"sad" のいずれかに制限します。該当しない場合は "talk" を返します。

### Types
- ReducedTalkStyle: "talk"、"happy"、"sad" のいずれかの値を持つ文字列型を定義しています。


## src/utils/wait.ts

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、JavaScriptまたはTypeScriptで使用される単一の非同期関数 `wait` を定義しています。この関数は、指定されたミリ秒数だけ実行を一時停止するためのユーティリティ関数です。

### Imported Modules
このファイルでは外部モジュールのインポートは行われていません。

### Functions
- wait: 指定されたミリ秒数だけプログラムの実行を一時停止する非同期関数。Promiseを返し、setTimeout を使用して遅延を実現します。


## src/utils/buildUrl.ts

以下は要求された形式でのMarkdown形式の説明です：

### File Description
このファイルは、Next.jsアプリケーションでGitHub Pagesに公開する際のアセット読み込みを支援する機能を提供しています。環境変数に基づいてURLにリポジトリ名を追加することで、適切なパスを生成します。

### Imported Modules
- next/config

### Functions
- buildUrl: 与えられたパスに対して、環境設定に基づいてリポジトリ名を前置したURLを生成します。GitHub Pagesでのアセット読み込みを正しく行うために使用されます。


## src/styles/globals.css

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはTailwind CSSを使用したCSSスタイルシートです。基本的なTailwindの設定を含み、カスタムコンポーネントとユーティリティクラスを定義しています。また、bodyタグのグローバルスタイリングや、カスタムの入力範囲スライダーのスタイリング、スクロールバーを非表示にするユーティリティクラスも含まれています。

### Imported Modules
- @tailwind base
- @tailwind components
- @tailwind utilities

### Custom Styles
- body: 背景画像の配置と表示方法を設定

### Components (@layer components)
- .input-range: カスタムの入力範囲スライダーのスタイリングを定義
  - WebkitとStandard CSSの両方に対応
  - スライダーのつまみ（thumb）のカスタマイズを含む

### Utilities (@layer utilities)
- .scroll-hidden: スクロールバーを非表示にするユーティリティクラスを定義
  - 異なるブラウザに対応するための複数のプロパティを使用


## src/components/settings.tsx

以下は、提供されたコードの分析結果です：

### File Description
このファイルは、React コンポーネントである `Settings` を定義しています。このコンポーネントは、チャットアプリケーションの設定画面を表示し、ユーザーが様々な設定（AI サービス、言語、音声合成エンジン、キャラクター設定など）を変更できるようにします。

### Imported Modules
- React, useEffect
- IconButton, TextButton, Link
- Message
- GitHubLink
- KoeiroParam, PRESET_A, PRESET_B, PRESET_C, PRESET_D
- i18n, useTranslation
- speakers.json

### Functions
- Settings: メインのコンポーネント関数。多数のプロップを受け取り、設定画面の UI を生成します。
- useEffect: コンポーネントのマウント時に localStorage から言語設定を読み込みます。

このコンポーネントは非常に大きく、多くの設定オプションを含んでいます。主な機能は以下の通りです：

1. 言語設定
2. キャラクター名と表示設定
3. VRM と背景画像の設定
4. 外部接続モードの切り替え
5. AI サービスの選択と設定（OpenAI, Anthropic, Google, Groq, LocalLLM, Dify）
6. YouTube モードの設定
7. キャラクター設定プロンプトの編集
8. 音声合成エンジンの選択と設定
9. チャット履歴の管理

各設定項目は、対応するステート変数と更新関数を使用して管理されています。また、i18next を使用して多言語対応を実現しています。


## src/components/chatLog.tsx

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはReactコンポーネントを定義しており、チャットログを表示するための`ChatLog`コンポーネントと、個々のチャットメッセージを表示する`Chat`コンポーネントが含まれています。スクロール機能や、ユーザーとキャラクターの発言を区別して表示する機能が実装されています。

### Imported Modules
- useEffect (from 'react')
- useRef (from 'react')
- Message (from '@/features/messages/messages')

### Functions
- ChatLog: メッセージの配列とキャラクター名を受け取り、チャットログ全体を表示するコンポーネント。自動スクロール機能を実装。
- Chat: 個々のチャットメッセージを表示するコンポーネント。役割（ユーザーまたはキャラクター）に応じて異なるスタイルを適用。
- useEffect (in ChatLog): コンポーネントのマウント時と`messages`の更新時にスクロール位置を調整するためのeffect hook。


## src/components/messageInput.tsx

以下は要求された形式でのファイル分析結果です：

### File Description
このファイルはReactコンポーネント `MessageInput` を定義しています。このコンポーネントはチャットインターフェースの入力部分を実装しており、テキスト入力、マイクボタン、送信ボタンを含んでいます。ユーザーの入力や処理状態に応じて動的に変化する機能を持っています。

### Imported Modules
- IconButton (from "./iconButton")
- useTranslation (from 'react-i18next')
- useState, useEffect (from 'react')

### Functions
- MessageInput: メインのコンポーネント関数。ユーザーメッセージ入力、マイク録音、チャット処理状態を管理し、対応するUIを表示します。
- handleKeyPress: テキストエリアでのキー入力を処理する関数。Enterキーでのメッセージ送信やShift+Enterでの改行を管理します。

このコンポーネントは、ユーザー入力の管理、多言語対応、動的なUI更新（ローディングドットのアニメーションなど）、そしてレスポンシブなテキストエリアの実装を特徴としています。


## src/components/link.tsx

以下は、提供されたファイルの内容に基づいたMarkdown形式の説明です：

### File Description
このファイルは、Reactコンポーネントとして`Link`を定義しています。このコンポーネントは、外部リンクを生成するためのシンプルな再利用可能なコンポーネントです。セキュリティと適切なスタイリングを考慮して設計されています。

### Imported Modules
このファイルでは明示的なインポート文は見られません。ただし、Reactの JSX 構文を使用しているため、暗黙的にReactがインポートされていると考えられます。

### Functions
- Link: URLとラベルを受け取り、スタイル付きの外部リンクを生成するReactコンポーネント。セキュリティ属性とホバー効果を含む。


## src/components/speakers.json

以下にMarkdown形式での分析結果を示します：

### File Description
このファイルは、音声合成システムまたは対話システムで使用される話者（キャラクター）のリストを JSON 形式で定義しています。各話者には名前と ID が割り当てられており、一部の話者には複数の話し方（モード）が設定されています。

### Imported Modules
このファイルは純粋なデータ定義であり、特定のモジュールのインポートは含まれていません。

### Functions
このファイルには関数定義は含まれていません。代わりに、以下のような構造を持つデータリストが定義されています：

- 各要素は `{"speaker": "話者名", "id": 数値ID}` の形式
- 一部の話者は複数のバリエーション（例：普通、あまあま、ツンツンなど）を持つ
- ID は 0 から始まる連続しない整数値で割り当てられている

このデータ構造は、音声合成システムや対話システムで話者を選択したり、特定の話し方を指定したりする際に使用される可能性が高いです。


## src/components/meta.tsx

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、Reactコンポーネントとして`Meta`を定義しています。`Meta`コンポーネントは、ウェブページのメタデータ（タイトル、説明、OGPタグ、Twitterカード情報など）を設定するためのものです。Next.jsの`Head`コンポーネントを使用して、HTMLの`<head>`セクションにこれらのメタタグを挿入します。

### Imported Modules
- `buildUrl` from "@/utils/buildUrl"
- `Head` from "next/head"

### Functions
- `Meta`: ウェブページのメタデータを設定するReactコンポーネント。タイトル、説明、画像URL、OGPタグ、Twitterカード情報を含むHeadコンポーネントを返します。

注意: `buildUrl`関数はインポートされていますが、このコード内では使用されていません。


## src/components/textButton.tsx

以下は、提供されたファイルの内容を分析し、Markdown形式で説明したものです：

### File Description
このファイルはReactコンポーネントの`TextButton`を定義しています。このコンポーネントは、カスタマイズ可能なスタイルを持つボタンを作成します。プロパティとしてHTMLボタン要素の属性を受け取り、それらを拡張してスタイリングを適用します。

### Imported Modules
- react (ButtonHTMLAttributes)

### Functions
- TextButton: カスタマイズ可能なスタイルを持つボタンコンポーネントを作成します。HTMLボタン要素の属性を受け取り、追加のクラス名とスタイルを適用します。

この関数コンポーネントは、渡されたpropsを展開し、独自のクラス名を追加してボタンをレンダリングします。ボタンのスタイルには、パディング、テキスト色、背景色、ホバー効果、アクティブ状態、無効状態、そして角丸などが含まれています。


## src/components/assistantText.tsx

以下はファイルの分析結果です：

### File Description
このファイルは、React コンポーネントの `AssistantText` を定義しています。このコンポーネントは、アシスタントのメッセージを表示するためのUI要素を作成します。キャラクター名の表示オプションがあり、メッセージ内の特定のパターンを除去する機能も含まれています。

### Imported Modules
このファイルには明示的なインポート文が含まれていませんが、以下のモジュールの使用が暗示されています：
- React (JSX構文の使用から推測)

### Functions
- AssistantText: アシスタントのテキストメッセージを表示するためのReactコンポーネント。メッセージ、キャラクター名、キャラクター名の表示有無を引数として受け取り、スタイリングされたUIを返します。この関数は、メッセージ内の特定のパターン（角括弧で囲まれたアルファベット）を除去する機能も持っています。


## src/components/codeLog.tsx

以下に、ご要望の形式でMarkdown形式の説明を提供します：

### File Description
このファイルはReactコンポーネントを含み、チャットログを表示するためのコードを提供しています。`CodeLog`コンポーネントはメッセージのリストを受け取り、それらを適切にスタイリングして表示します。また、`Chat`コンポーネントは個々のメッセージの表示を担当し、メッセージの種類（コード、出力、実行中、アシスタント、その他）に応じて適切なスタイルを適用します。

### Imported Modules
- useEffect (from 'react')
- useRef (from 'react')
- Message (from '@/features/messages/messages')
- React (from 'react')

### Functions
- CodeLog: メッセージのリストを受け取り、全体のチャットログを表示するコンポーネント。自動スクロール機能も実装しています。
- Chat: 個々のメッセージを表示するコンポーネント。メッセージの種類に応じて背景色やテキスト色を変更し、適切なスタイリングを行います。


## src/components/menu.tsx

以下はファイルの分析結果です：

### File Description
このファイルは、React コンポーネントである `Menu` を定義しています。このコンポーネントは、AI サービスの設定、チャットログの表示、システムプロンプトの管理、音声設定など、多くの機能を制御するインターフェースを提供します。また、VRM ファイルの読み込みや背景画像の設定など、視覚的な要素の管理も行っています。

### Imported Modules
- React と関連フック（useCallback, useContext, useRef, useState）
- カスタムコンポーネント（IconButton, ChatLog, CodeLog, Settings, AssistantText）
- コンテキスト（ViewerContext）
- 型定義（Message, KoeiroParam）
- ユーティリティ関数（testVoice）
- i18next（useTranslation）

### Functions
- Menu: メインのコンポーネント関数。多数のプロップを受け取り、設定やチャットログの表示を管理します。
- handleChangeAIService: AI サービスの変更を処理します。
- handleChangeSystemPrompt: システムプロンプトの変更を処理します。
- handleOpenAiKeyChange: OpenAI キーの変更を処理します。
- handleAnthropicKeyChange: Anthropic キーの変更を処理します。
- handleGoogleKeyChange: Google キーの変更を処理します。
- handleGroqKeyChange: Groq キーの変更を処理します。
- handleChangeLocalLlmUrl: ローカル LLM URL の変更を処理します。
- handleDifyKeyChange: Dify キーの変更を処理します。
- handleDifyUrlChange: Dify URL の変更を処理します。
- handleDifyConversationIdChange: Dify 会話 ID の変更を処理します。
- handleChangeKoeiromapKey: Koeiromap キーの変更を処理します。
- handleVoicevoxSpeakerChange: VOICEVOX スピーカーの変更を処理します。
- handleChangeGoogleTtsType: Google TTS タイプの変更を処理します。
- handleChangeStyleBertVits2ServerUrl: StyleBertVits2 サーバー URL の変更を処理します。
- handleChangeStyleBertVits2ModelId: StyleBertVits2 モデル ID の変更を処理します。
- handleChangeStyleBertVits2Style: StyleBertVits2 スタイルの変更を処理します。
- handleYoutubeApiKeyChange: YouTube API キーの変更を処理します。
- handleYoutubeLiveIdChange: YouTube ライブ ID の変更を処理します。
- handleChangeKoeiroParam: Koeiro パラメータの変更を処理します。
- handleWebSocketMode: WebSocket モードの変更を処理します。
- handleConversationContinuityMode: 会話の継続性モードの変更を処理します。
- handleClickOpenVrmFile: VRM ファイルを開くクリックイベントを処理します。
- handleClickOpenBgFile: 背景ファイルを開くクリックイベントを処理します。
- handleClickTestVoice: 音声テストのクリックイベントを処理します。
- handleChangeVrmFile: VRM ファイルの変更を処理します。
- handleChangeBgFile: 背景ファイルの変更を処理します。
- handleChangeGSVITtsServerUrl: GSVI TTS サーバー URL の変更を処理します。
- handleChangeGSVITtsModelId: GSVI TTS モデル ID


## src/components/messageInputContainer.tsx

以下は要求された形式でのファイル内容の分析です：

### File Description
このファイルは、React コンポーネントの `MessageInputContainer` を定義しています。このコンポーネントはテキスト入力と音声入力機能を提供し、ユーザーのメッセージを処理します。音声認識機能を含み、ユーザーの発言を自動的にテキストに変換し、チャット処理を開始します。

### Imported Modules
- MessageInput (from "@/components/messageInput")
- useState, useEffect, useCallback (from "react")

### Functions
- MessageInputContainer: メインのコンポーネント関数。テキスト入力、音声入力、およびメッセージ送信機能を管理します。
- handleRecognitionResult: 音声認識の結果を処理し、テキストを更新します。
- handleRecognitionEnd: 音声認識の終了を処理します。
- handleClickMicButton: マイクボタンのクリックイベントを処理し、音声認識を開始または停止します。
- handleClickSendButton: 送信ボタンのクリックイベントを処理し、メッセージを送信します。

このコンポーネントは、ユーザーインターフェースの状態管理、音声認識の設定と制御、およびユーザー入力の処理を行います。また、外部から提供される props を通じて、チャット処理の状態や言語設定を管理します。


## src/components/iconButton.tsx

以下はリクエストされた形式での分析結果です：

### File Description
このファイルはReactコンポーネントの`IconButton`を定義しています。このコンポーネントはアイコンを含むボタンを作成し、プロセス中の状態や追加のラベルテキストをサポートします。ボタンのスタイリングにはTailwind CSSクラスが使用されています。

### Imported Modules
- KnownIconType from "@charcoal-ui/icons"
- ButtonHTMLAttributes from "react"

### Functions
- IconButton: アイコン付きのボタンを生成するReactコンポーネント。アイコン、処理中の状態、オプションのラベルを受け取り、スタイリングされたボタンを返します。

### Types
- Props: IconButtonコンポーネントのプロパティを定義するタイプ。HTMLButtonElementの属性に加えて、iconName、isProcessing、labelを含みます。

### Components
- pixiv-icon: アイコンを表示するためのカスタムコンポーネント。処理中の状態に応じて異なるアイコンを表示します。

この分析では、ファイル内で定義されている主要な要素を簡潔に説明しています。特に重要なのは`IconButton`コンポーネントの機能と、それが受け取るプロパティの構造です。


## src/components/githubLink.tsx

以下は要求された形式でのMarkdown形式の説明です：

### File Description
このファイルはReactコンポーネント `GitHubLink` を定義しています。このコンポーネントは、GitHubリポジトリへのリンクを含む、スタイリングされたボタンを表示します。ボタンには GitHub のロゴと "Fork me" というテキストが含まれており、ページの右上に固定位置で表示されるようになっています。

### Imported Modules
- Image (from 'next/image')
- buildUrl (from "@/utils/buildUrl")

### Functions
- GitHubLink: GitHubリポジトリへのリンクを含むボタンをレンダリングするReactコンポーネント関数。ボタンはGitHubロゴと"Fork me"テキストを含み、クリックするとGitHubリポジトリが新しいタブで開きます。


## src/components/introduction.tsx

以下にMarkdown形式での説明を提供します：

### File Description
このファイルはReactコンポーネントの`Introduction`を定義しています。アプリケーションの紹介、技術説明、ソースコードリンクなどを含む導入画面を表示します。また、言語選択機能と「次回から表示しない」オプションも提供しています。

### Imported Modules
- react: useState, useCallback
- ./link: Link
- ./iconButton: IconButton
- i18next: i18n
- react-i18next: useTranslation, Trans

### Functions
- Introduction: メインのコンポーネント関数。導入画面のUIを構築し、言語設定や表示制御を行います。
- handleDontShowIntroductionChange: 「次回から表示しない」チェックボックスの変更を処理します。
- updateLanguage: 選択された言語に基づいて言語設定を更新します。
- getVoiceLanguageCode: 選択された言語コードに対応する音声言語コードを返します。

このコンポーネントは、アプリケーションの概要説明、使用技術の紹介、ソースコードへのリンクなどを含む詳細な導入画面を提供し、多言語対応と表示制御機能を備えています。


## src/components/vrmViewer.tsx

以下にMarkdown形式での説明を提供します：

### File Description
このファイルは、React コンポーネントの `VrmViewer` を定義しています。VRMファイルを表示するためのキャンバスを設定し、ドラッグ＆ドロップによるVRMファイルの動的な読み込みを可能にします。また、初期VRMモデルの読み込みも行います。

### Imported Modules
- react: `useContext`, `useCallback`
- ../features/vrmViewer/viewerContext: `ViewerContext`
- @/utils/buildUrl: `buildUrl`

### Functions
- VrmViewer: メインのコンポーネント関数。キャンバスの設定、VRMファイルの読み込み、ドラッグ＆ドロップイベントの処理を行います。
- canvasRef: キャンバス要素への参照を扱うコールバック関数。キャンバスの初期設定、VRMファイルの読み込み、ドラッグ＆ドロップイベントリスナーの追加を行います。

このコンポーネントは、フルスクリーンのキャンバス要素をレンダリングし、VRMビューアーの機能を提供します。ユーザーはドラッグ＆ドロップでVRMファイルを動的に変更できます。


## src/lib/i18n.js

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはi18nextライブラリを使用して多言語対応を設定するためのものです。英語、日本語、中国語、韓国語の翻訳リソースを設定し、デフォルト言語を日本語に設定しています。React アプリケーションで国際化を実装するための基本的な設定ファイルです。

### Imported Modules
- i18n from "i18next"
- initReactI18next from "react-i18next"

### Functions
このファイルには明示的に定義された関数はありませんが、以下の主要な操作が行われています：

- i18n.use(): i18nにReact用の初期化機能を追加します。
- i18n.init(): 多言語リソース、デフォルト言語、フォールバック言語、補間オプションなどの設定を行います。

最後に、設定されたi18nオブジェクトがエクスポートされ、アプリケーションの他の部分で使用できるようになっています。


## src/lib/VRMAnimation/VRMAnimation.ts

以下はMarkdown形式での説明です：

### File Description
このファイルはVRMアニメーションを扱うクラス `VRMAnimation` を定義しています。VRMモデルのヒューマノイド、表情、視線のアニメーションを管理し、THREE.jsのAnimationClipを生成する機能を提供します。

### Imported Modules
- three
- @pixiv/three-vrm

### Functions
- constructor: `VRMAnimation` クラスのインスタンスを初期化します。各種トラックとプロパティを設定します。
- createAnimationClip: VRMモデルに対応するTHREE.jsのAnimationClipを生成します。
- createHumanoidTracks: ヒューマノイドの回転と移動のキーフレームトラックを生成します。
- createExpressionTracks: 表情のキーフレームトラックを生成します。
- createLookAtTrack: 視線のキーフレームトラックを生成します。
- createHumanoidTracks: VRMモデルのヒューマノイドボーンに対応するアニメーショントラックを生成します。
- createExpressionTracks: VRMモデルの表情に対応するアニメーショントラックを生成します。
- createLookAtTrack: 視線制御のためのアニメーショントラックを生成します。


## src/lib/VRMAnimation/VRMAnimationLoaderPluginOptions.ts

以下は、提供されたファイル内容の分析結果です：

### File Description
このファイルは、TypeScriptで書かれたインターフェース定義を含んでいます。`VRMAnimationLoaderPluginOptions`というインターフェースが定義されていますが、現時点では中身が空です。このインターフェースは、VRMアニメーションローダープラグインのオプションを定義するためのものと推測されます。

### Imported Modules
このファイルには外部モジュールのインポートは含まれていません。

### Functions
このファイルには関数定義は含まれていません。

注: このファイルは非常に短く、主にインターフェース定義のみを含んでいます。将来的にこのインターフェースに具体的なプロパティやメソッドが追加される可能性があります。


## src/lib/VRMAnimation/VRMAnimationLoaderPlugin.ts

以下は、提供されたファイルの分析結果です：

### File Description
このファイルは、VRMアニメーションのローダープラグインを実装しています。GLTFファイルからVRMアニメーションデータを抽出し、Three.jsと互換性のあるフォーマットに変換します。主にVRMCVRMAnimationの解析と、ボーン、表情、視線のアニメーションデータの処理を行っています。

### Imported Modules
- three
- three/examples/jsm/loaders/GLTFLoader
- ./VRMAnimationLoaderPluginOptions
- @gltf-transform/core
- ./VRMCVRMAnimation
- @pixiv/three-vrm
- ./VRMAnimation
- ./utils/arrayChunk

### Functions
- constructor: VRMAnimationLoaderPluginのインスタンスを初期化します。
- afterRoot: GLTFファイルの読み込み後に呼び出され、VRMアニメーションデータを抽出・処理します。
- _createNodeMap: VRMCVRMAnimationからノードマップを作成します。
- _createBoneWorldMatrixMap: ボーンのワールド行列マップを作成します。
- _parseAnimation: アニメーションクリップを解析し、VRMAnimation形式に変換します。

このプラグインは、GLTFファイルからVRMアニメーションデータを抽出し、Three.jsで使用可能な形式に変換する重要な役割を果たしています。ヒューマノイド、表情、視線のアニメーションデータを処理し、VRMキャラクターのアニメーション再生を可能にします。


## src/lib/VRMAnimation/loadVRMAnimation.ts

以下はリクエストされた形式での分析結果です：

### File Description
このファイルは、VRMアニメーションをロードするための機能を提供しています。GLTFLoaderを使用してVRMアニメーションファイルを非同期的に読み込み、VRMAnimationLoaderPluginを利用してVRMアニメーションデータを解析します。

### Imported Modules
- GLTFLoader (from 'three/examples/jsm/loaders/GLTFLoader')
- VRMAnimation (from './VRMAnimation')
- VRMAnimationLoaderPlugin (from './VRMAnimationLoaderPlugin')

### Functions
- loadVRMAnimation: 指定されたURLからVRMアニメーションを非同期的にロードし、最初のVRMAnimationオブジェクトを返します。アニメーションが見つからない場合はnullを返します。

### Other Elements
- loader: GLTFLoaderのインスタンスで、VRMAnimationLoaderPluginが登録されています。これにより、VRMアニメーションの特殊な解析が可能になります。


## src/lib/VRMAnimation/VRMCVRMAnimation.ts

以下は要求された形式での分析結果です：

### File Description
このファイルは、VRMCVRMAnimationインターフェースを定義しています。VRMフォーマットのアニメーションデータ構造を表現し、humanoid、expressions、lookAtなどの主要な要素を含んでいます。@pixiv/three-vrmライブラリからの型定義を利用しています。

### Imported Modules
- @pixiv/three-vrm

### Functions
このファイルには関数定義は含まれていません。代わりに、以下のインターフェースが定義されています：

- VRMCVRMAnimation: VRMアニメーションデータの構造を定義するインターフェース。specVersion、humanoid、expressions、lookAtプロパティを持ちます。

注：このファイルは主にTypeScriptのインターフェース定義を含んでおり、実行可能な関数は含まれていません。


## src/lib/VRMAnimation/utils/linearstep.ts

以下は要求された形式でのMarkdown形式の説明です：

### File Description
このファイルは、線形補間（リニアステップ）関数を実装しています。`linearstep`関数は、指定された範囲内で値を0から1の間に正規化し、その結果を飽和（クランプ）させます。この関数は、アニメーションや視覚効果などで滑らかな遷移を作成する際に役立ちます。

### Imported Modules
- `saturate` from './saturate'

### Functions
- `linearstep`: 3つの数値パラメータ（a, b, t）を受け取り、tをaとbの間で正規化し、その結果を0から1の範囲に飽和させます。この関数は、値の滑らかな補間に使用されます。


## src/lib/VRMAnimation/utils/saturate.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、数値を0から1の範囲に制限する`saturate`関数を定義しています。この関数はTypeScriptで書かれており、エクスポートされているため、他のモジュールで使用できるようになっています。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
- saturate: 入力された数値を0以上1以下の範囲に制限します。Math.min()とMath.max()を使用して、値を適切な範囲内に収めます。


## src/lib/VRMAnimation/utils/arrayChunk.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルは、配列を指定されたサイズのチャンクに分割する関数`arrayChunk`を定義しています。TypeScriptで書かれており、ジェネリック型を使用して様々な型の配列に対応できるようになっています。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Functions
- arrayChunk: 与えられた配列を指定されたサイズのチャンクに分割する関数。元の配列の要素を順番に新しい部分配列に分配し、結果として2次元配列を返します。引数として配列と分割サイズを受け取り、TypeScriptのジェネリクスを使用して型安全性を確保しています。


## src/lib/VRMLookAtSmootherLoaderPlugin/VRMLookAtSmoother.ts

以下はご提供いただいたファイルの分析結果です：

### File Description
このファイルは、VRMモデルの視線制御を拡張した`VRMLookAtSmoother`クラスを定義しています。このクラスは、ユーザーの方向への視線追従、頭の回転、眼球のサッケード運動などの機能を追加し、よりリアルな視線制御を実現します。

### Imported Modules
- @pixiv/three-vrm
- three

### Functions
- VRMLookAtSmoother.constructor: VRMLookAtSmootherクラスのコンストラクタ。初期設定を行います。
- VRMLookAtSmoother.update: 毎フレーム呼び出され、視線の更新を行います。アニメーション、ユーザー向き、サッケードを考慮して視線を計算します。
- VRMLookAtSmoother.revertFirstPersonBoneQuat: レンダリング後に頭の回転を元に戻すメソッド。

### Constants
- SACCADE_MIN_INTERVAL: サッケードが発生するまでの最小間隔
- SACCADE_PROC: サッケードが発生する確率
- SACCADE_RADIUS: サッケードの範囲半径（度単位）

### Class Properties
- smoothFactor: スムージング用の係数
- userLimitAngle: ユーザー向きに向く限界の角度（度単位）
- userTarget: ユーザーへの向きを示すオブジェクト
- enableSaccade: サッケードを有効にするかどうかのフラグ

このクラスは、VRMモデルの視線制御をより自然で動的なものにするために設計されており、アニメーションとユーザー入力の両方を考慮しつつ、サッケード運動も模倣しています。


## src/lib/VRMLookAtSmootherLoaderPlugin/VRMLookAtSmootherLoaderPlugin.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはVRMLookAtSmootherLoaderPluginクラスを定義しています。このプラグインは、VRMモデルのLookAt機能にスムージング効果を追加するためのものです。VRMLookAtLoaderPluginを拡張し、GLTFファイルの読み込み後にVRMLookAtSmootherを適用します。

### Imported Modules
- @pixiv/three-vrm
  - VRMHumanoid
  - VRMLookAt
  - VRMLookAtLoaderPlugin
- three/examples/jsm/loaders/GLTFLoader
  - GLTF
- ./VRMLookAtSmoother
  - VRMLookAtSmoother

### Functions
- afterRoot: GLTFファイルのルートが読み込まれた後に呼び出される非同期関数。VRMHumanoidとVRMLookAtが存在する場合、VRMLookAtSmootherを作成し、元のLookAt設定をコピーして適用します。

### Class
- VRMLookAtSmootherLoaderPlugin: VRMLookAtLoaderPluginを拡張したクラス。nameプロパティと afterRoot メソッドを実装しています。


## src/pages/index.tsx

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、React hooks を使用して実装された複雑な会話型AIアプリケーションのメインコンポーネントです。VRMビューワー、音声合成、AIチャット、YouTubeコメント処理、WebSocket通信など、多様な機能を統合しています。ユーザーインターフェース、状態管理、外部APIとの連携を担当し、アプリケーションの中核を形成しています。

### Imported Modules
- react
- @/components/vrmViewer
- @/features/vrmViewer/viewerContext
- @/features/messages/messages
- @/features/messages/speakCharacter
- @/components/messageInputContainer
- @/features/constants/systemPromptConstants
- @/features/constants/koeiroParam
- @/features/chat/aiChatFactory
- @/components/introduction
- @/components/menu
- @/components/meta
- @/lib/i18n
- react-i18next
- @/features/youtube/youtubeComments
- @/utils/buildUrl

### Functions
- Home: メインコンポーネント関数。アプリケーションの全体的な構造と動作を定義します。
- handleChangeChatLog: チャットログを更新する関数。
- handleChangeCodeLog: コードログを更新する関数。
- handleSpeakAi: AI応答の音声再生を処理する関数。
- processAIResponse: AIからの応答を処理し、チャットログに追加する関数。
- handleSendChat: ユーザーのチャット入力を処理し、AI応答を取得する関数。
- fetchAndProcessCommentsCallback: YouTubeのライブコメントを取得し処理する関数。

このファイルには他にも多くの状態変数や副作用（useEffect）が含まれており、アプリケーションの複雑な動作を制御しています。


## src/pages/_document.tsx

以下は、提供されたファイルの分析結果をMarkdown形式で説明したものです：

### File Description
このファイルは、Next.jsアプリケーションのカスタムドキュメントコンポーネントを定義しています。主にHTMLの基本構造を設定し、グローバルなフォントの読み込みを行っています。日本語とラテン文字のフォントをGoogle Fontsから読み込む設定が含まれています。

### Imported Modules
- next/document: Html, Head, Main, NextScript

### Functions
- Document: アプリケーション全体のHTML構造を定義するカスタムドキュメントコンポーネント。<Html>タグの言語属性を日本語に設定し、Google Fontsからフォントを読み込むためのリンクタグを追加しています。


## src/pages/_app.tsx

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはNext.jsアプリケーションのメインコンポーネントである`App`を定義しています。グローバルスタイルを適用し、i18nを使用して言語設定を管理しています。アプリケーション起動時に、ローカルストレージまたはブラウザの言語設定に基づいて適切な言語を設定します。

### Imported Modules
- "@/styles/globals.css"
- "@charcoal-ui/icons"
- "next/app"
- "react"
- "../lib/i18n"

### Functions
- App: アプリケーションのメインコンポーネント。言語設定を初期化し、すべてのページコンポーネントをラップします。useEffectフックを使用して、アプリケーション起動時に言語設定を行います。


## src/pages/api/anthropic.ts

以下にMarkdown形式で分析結果を提供します：

### File Description
このファイルはNext.jsのAPIハンドラーを実装しています。AnthropicのAI APIを使用してメッセージの処理とレスポンスの生成を行います。ストリーミングと非ストリーミングの両方のモードをサポートし、システムメッセージと連続したユーザーメッセージを適切に処理します。

### Imported Modules
- NextApiRequest, NextApiResponse (from "next")
- Anthropic (from "@anthropic-ai/sdk")
- Message (from "@/features/messages/messages")

### Functions
- handler: メインのAPIハンドラー関数。リクエストを処理し、AnthropicのAPIを使用してレスポンスを生成します。ストリーミングと非ストリーミングの両方のモードをサポートしています。

この関数内では以下の主要な処理が行われています：
1. リクエストボディからメッセージ、APIキー、モデル、ストリームフラグを抽出
2. システムメッセージとユーザーメッセージの分離
3. 連続したユーザーメッセージの統合
4. AnthropicのAPIクライアントを使用したメッセージの処理（ストリーミングモードと非ストリーミングモードの両方に対応）
5. レスポンスの生成と送信


## src/pages/api/chat.ts

### File Description
このファイルはNext.jsのAPIルートハンドラーを実装しています。OpenAI APIを使用してチャット完了機能を提供する予定でしたが、現在はコメントアウトされています。APIキーの検証、OpenAI APIの設定、チャット完了リクエストの送信、そしてレスポンスの処理を行う予定でした。

### Imported Modules
（コメントアウトされていますが、以下のモジュールをインポートする予定でした）
- Configuration (from "openai")
- OpenAIApi (from "openai")
- NextApiRequest (from "next")
- NextApiResponse (from "next")

### Functions
- handler: Next.jsのAPIルートハンドラー関数。APIキーの検証、OpenAI APIの設定、チャット完了リクエストの送信、そしてレスポンスの処理を行う予定でした。

注意：現在、このコードは完全にコメントアウトされているため、実際には機能していません。実装を有効にするには、コメントを解除する必要があります。


## src/pages/api/groq.ts

以下は要求された形式での分析結果です：

### File Description
このファイルはNext.jsのAPIルートハンドラーを実装しています。Groq APIを使用してチャット完了を生成し、ストリーミングと非ストリーミングの両方のモードをサポートしています。メッセージの統合や適切なエラー処理も行っています。

### Imported Modules
- NextApiRequest, NextApiResponse from "next"
- Groq from "groq-sdk"
- Message from "@/features/messages/messages"

### Functions
- handler: メインのAPIハンドラー関数。リクエストを処理し、Groq APIを使用してチャット完了を生成します。ストリーミングと非ストリーミングの両方のモードをサポートしています。

このハンドラー関数内では、以下の主要な操作が行われています：
1. リクエストボディからメッセージ、APIキー、モデル、ストリームフラグを抽出
2. Groqクライアントの初期化
3. システムメッセージとユーザーメッセージの分離
4. 連続したメッセージの統合
5. ストリーミングモードまたは非ストリーミングモードでのGroq APIの呼び出し
6. レスポンスの生成と送信
7. エラー処理

なお、この関数は直接エクスポートされており、他の関数は定義されていません。


## src/pages/api/tts.ts

以下に、指定された形式でMarkdown形式の説明を提供します：

### File Description
このファイルは、Next.jsのAPIルートハンドラーを定義しています。音声合成のリクエストを処理し、KoeiromapまたはGoogle TTSを使用して音声を生成します。クライアントからのパラメータに基づいて適切な音声合成サービスを選択し、生成された音声データをJSON形式で返します。

### Imported Modules
- koeiromapFreeV1 from "@/features/koeiromap/koeiromap"
- googleTts from "@/features/googletts/googletts"
- NextApiRequest, NextApiResponse from "next"

### Functions
- handler: Next.jsのAPIルートハンドラー関数。HTTPリクエストを受け取り、リクエストボディから必要なパラメータを抽出し、指定された音声合成サービス（KoeiromapまたはGoogle TTS）を使用して音声を生成し、結果をJSON形式で返します。


## src/pages/api/stylebertvits2.ts

以下は要求された形式での分析結果です：

### File Description
このファイルはNext.jsのAPIルートハンドラーを実装しています。テキストを音声に変換するサービスにリクエストを送信し、生成された音声データをクライアントに返します。エラー処理も含まれており、問題が発生した場合は適切なエラーレスポンスを返します。

### Imported Modules
- NextApiRequest (from "next")
- NextApiResponse (from "next")

### Functions
- handler: APIリクエストを処理する非同期関数。クライアントから受け取ったパラメータを使用して外部の音声生成サービスにリクエストを送信し、生成された音声データをレスポンスとして返します。エラーが発生した場合は、適切なエラーメッセージを含むJSONレスポンスを返します。

