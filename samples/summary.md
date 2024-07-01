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

### File Description
このファイルは、Tailwind CSSの設定ファイルです。Tailwind CSSは、ユーティリティファーストのCSSフレームワークで、コンポーネントスタイルをすばやく作成できます。このファイルでは、ダークモードをデフォルトに設定し、コンテンツのソースを指定し、Charcoal UIのTailwindプリセットを使用し、さらにカスタムのテーマ設定を追加しています。

### Imported Modules
- `@charcoal-ui/theme`
- `@charcoal-ui/tailwind-config`

### Functions
このファイルには明示的な関数定義はありませんが、以下の設定が含まれています:

- `darkMode: true`: ダークモードをデフォルトに設定します。
- `content`: Tailwind CSSがスタイルを適用するソースファイルのパターンを指定します。
- `presets`: Charcoal UIのTailwindプリセットを使用します。
- `theme.extend`: カスタムの色とフォントファミリーを追加します。
- `plugins`: Tailwind CSSの `@tailwindcss/line-clamp` プラグインを使用します。


## Dockerfile

### File Description
このファイルはNode.js 16を使用したDockerfileです。コンテナ内にNode.jsアプリケーションを構築し、実行する手順が記述されています。

### Imported Modules
このファイルでは外部モジュールをインポートしていません。

### Instructions
- `FROM node:16`: Node.js 16をベースイメージとして使用します。
- `WORKDIR /app`: コンテナ内の作業ディレクトリを `/app` に設定します。
- `COPY package*.json ./`: `package.json` と `package-lock.json` をコンテナ内にコピーします。
- `RUN npm ci`: 依存関係をインストールします。
- `COPY . .`: アプリケーションのソースコードをコンテナ内にコピーします。
- `RUN npm run build`: アプリケーションをビルドします。
- `EXPOSE 3000`: コンテナのポート 3000 を公開します。
- `CMD ["npm", "start"]`: コンテナ起動時に `npm start` を実行します。


## next.config.js

### File Description
このファイルは、Next.jsアプリケーションの設定を定義しています。Next.jsは、React製のサーバーサイドレンダリングを行うJavaScriptフレームワークです。このファイルでは、アプリケーションのベースパスやパブリックランタイム設定、Reactの厳格モードの有効化など、さまざまな設定を行っています。

### Imported Modules
このファイルでは、特にモジュールをインポートしていません。

### Functions
このファイルには、関数は定義されていません。代わりに、Next.jsの設定オブジェクトが定義されています。


## electron.mjs

### File Description
このファイルは、Electronアプリケーションの主要な設定と動作を定義しています。アプリケーションのメインウィンドウの作成、設定、ロード方法が記述されています。開発モードと本番モードでの動作が異なります。

### Imported Modules
- electron (app, BrowserWindow, screen)
- path
- url (fileURLToPath)
- electron-is-dev
- wait-on

### Functions
- createWindow: メインウィンドウを作成し、設定を適用し、URLをロードします。開発モードと本番モードで異なる動作をします。


## package.json

### File Description
このファイルは、Next.jsベースのReactアプリケーション「chat-vrm」のパッケージ設定とツール用の設定を含むmanifest.jsonファイルです。このアプリケーションは、VRMモデルを利用したチャットアプリケーションのようです。

### Imported Modules
このファイルには外部モジュールのインポートはありません。

### Scripts
- dev: Next.jsの開発サーバーを起動します。
- build: Next.jsアプリをビルドします。
- start: アプリをビルドし、本番サーバーを起動します。
- export: Next.jsアプリを静的ファイルとしてエクスポートします。
- lint: コードのリンティングを行います。
- electron: Electronデスクトップアプリを実行します。
- desktop: Next.jsの開発サーバーとElectronデスクトップアプリを同時に実行します。


## watch.json

### File Description
このファイルは、Next.js アプリケーションの設定を定義するための JSON 形式のファイルです。`install`、`restart`、および `throttle` の各プロパティを定義しています。

### Imported Modules
このファイルではモジュールがインポートされていません。

### Functions
このファイルには関数が定義されていません。代わりに、次のプロパティが設定されています:

- `install`: プロジェクトのインストール時に監視するファイルを指定します。この例では `package.json` ファイルが監視されます。
- `restart`: アプリケーションの再起動時に監視するファイルを指定します。この例では `.env` および `next.config.js` ファイルが監視されます。
- `throttle`: ファイルの変更を検出してから再ビルドを開始するまでの待機時間をミリ秒単位で指定します。この例では 250 ミリ秒待機します。


## tsconfig.json

### File Description
この設定ファイルは、TypeScriptのコンパイル設定を定義するために使用される`tsconfig.json`ファイルです。ここでは、TypeScriptコンパイラの動作を制御するためのさまざまなオプションが指定されています。

### Imported Modules
このファイルでは、モジュールはインポートされていません。

### Functions
このファイルには関数が定義されていません。代わりに、次のプロパティが設定されています:

- `compilerOptions`: TypeScriptコンパイラのオプションを設定します。
  - `target`: 出力されるJavaScriptのバージョンを指定します。
  - `lib`: コンパイル中に含めるライブラリを指定します。
  - `allowJs`: JavaScriptファイルの処理を許可するかどうかを指定します。
  - `skipLibCheck`: すべての宣言ファイルのタイプチェックをスキップするかどうかを指定します。
  - `strict`: すべての厳格な型チェックオプションを有効にするかどうかを指定します。
  - `forceConsistentCasingInFileNames`: ファイル名の大文字と小文字の区別を尊重するかどうかを指定します。
  - `noEmit`: エミットを行わないかどうかを指定します。
  - `esModuleInterop`: CommonJSモジュールからES6モジュールへの相互運用性を制御するかどうかを指定します。
  - `module`: 出力モジュール形式を指定します。
  - `moduleResolution`: モジュール解決方式を指定します。
  - `resolveJsonModule`: JSONファイルをモジュールとして読み込めるようにするかどうかを指定します。
  - `isolatedModules`:各ファイルをそれ自体のモジュールとして扱うかどうかを指定します。
  - `jsx`: JSXコードの出力形式を指定します。
  - `incremental`: インクリメンタルコンパイルを有効にするかどうかを指定します。
  - `paths`: モジュールの解決方法を設定します。
- `include`: コンパイルに含めるファイルパターンを指定します。
- `exclude`: コンパイルから除外するファイルパターンを指定します。


## docker-compose.yml

### File Description
このファイルは、Docker Composeを使用してアプリケーションをデプロイするための設定ファイルです。Docker Composeは、複数のコンテナをまとめて定義し、実行するためのツールです。このファイルでは、1つのサービス「app」が定義されています。

### Imported Modules
このファイルではモジュールはインポートされていません。

### Functions
このファイルには関数は定義されていません。代わりに、以下の設定が行われています:

- `build: .`: アプリケーションをビルドするためのDockerfileがカレントディレクトリにあることを示しています。
- `ports: - "3000:3000"`: ホストマシンのポート3000を、コンテナのポート3000にマップします。
- `volumes: - .:/app`: カレントディレクトリ(`.`)をコンテナ内の `/app` ディレクトリにマウントします。これにより、ホストマシン上のコードの変更がコンテナ内に反映されます。
- `env_file: - .env`: `.env` ファイルから環境変数を読み込みます。


## postcss.config.js

### File Description
このファイルは、PostCSS (CSS 後処理ツール) の設定を定義しています。PostCSS は、CSS を変換し、現代のブラウザに対応させるために使用されます。

### Imported Modules
このファイルでは外部モジュールをインポートしていません。

### Functions
このファイルには関数が定義されていません。代わりに、以下のプラグインが設定されています:

- tailwindcss: Tailwind CSS フレームワークを使用するための設定
- autoprefixer: ベンダープレフィックス (関係するブラウザに合わせて適切な CSS プロパティを自動で付与する機能) を提供するプラグイン


## src/features/emoteController/expressionController.ts

### File Description
このファイルは、VRMモデルの表情を管理するためのクラス `ExpressionController` を定義しています。主な機能は、前の表情を保持しながら新しい表情を適用する際に前の表情を0に戻すこと、および表情の適用を待つことです。また、自動的に視線を動かしたり瞬きをさせたりするための機能も含まれています。

### Imported Modules
- `three`: 3Dグラフィックスライブラリ
- `@pixiv/three-vrm`: VRMモデルを扱うためのライブラリ
- `./autoLookAt`: 自動視線制御機能を提供するモジュール
- `./autoBlink`: 自動瞬き機能を提供するモジュール

### Functions
- `playEmotion`: 指定された表情プリセットを適用します。前の表情があれば0に戻します。
- `lipSync`: 口パク用の表情プリセットと重みを設定します。前の口パク表情があれば0に戻します。
- `update`: 自動瞬きと口パクの更新を行います。


## src/features/emoteController/emoteConstants.ts

### File Description
このファイルは、瞬きに関する定数を定義しています。具体的には、目を閉じている最大時間と、目を開いている最大時間を定義しています。

### Imported Modules
このファイルではモジュールをインポートしていません。

### Functions
このファイルには関数が定義されていません。


## src/features/emoteController/autoLookAt.ts

### File Description
このファイルは、Three.jsのVRMモデルの目線制御を行うクラス「AutoLookAt」を定義しています。VRMLookAtSmootherでサッケード(目の動き)を制御しており、より大きな目線の動きが必要な場合は、このクラスに実装する必要があります。

### Imported Modules
- THREE (three.jsライブラリ)
- VRM (@pixiv/three-vrmライブラリ)

### Functions
- constructor: VRMオブジェクトとカメラオブジェクトを受け取り、目線の制御対象となるターゲットオブジェクトを作成し、カメラに追加します。VRMオブジェクトの目線制御機能を有効化し、ターゲットを設定します。


## src/features/emoteController/autoBlink.ts

### File Description
このファイルは、VRMモデルの自動瞬きを制御するクラス `AutoBlink` を定義しています。瞬きのタイミングと時間を管理し、VRMモデルの表情を更新するための機能を提供しています。

### Imported Modules
- `@pixiv/three-vrm`
- `./emoteConstants`

### Functions
- `constructor(expressionManager: VRMExpressionManager)`: VRMモデルの表情管理オブジェクトを受け取り、クラスのインスタンスを初期化します。
- `setEnable(isAuto: boolean)`: 自動瞬きのON/OFFを切り替えます。目が閉じている場合は、目が開くまでの時間を返します。
- `update(delta: number)`: 自動瞬きの状態を更新します。経過時間に基づいて目を開閉します。
- `close()`: 目を閉じる処理を行います。
- `open()`: 目を開く処理を行います。


## src/features/emoteController/emoteController.ts

### File Description
このファイルは、Three.jsとVRMを使用して、VRMモデルの感情表現と口パク機能を制御するためのクラスを提供しています。ExpressionControllerクラスを使用して、プリセットされた感情表現や口パク表現を適用することができます。

### Imported Modules
- three
- @pixiv/three-vrm
- ./expressionController

### Functions
- constructor(vrm, camera): VRMモデルとカメラオブジェクトを受け取り、ExpressionControllerインスタンスを初期化します。
- playEmotion(preset): 指定された感情表現プリセットを再生します。
- lipSync(preset, value): 指定された口パクプリセットと値を適用します。
- update(delta): 毎フレームの更新処理を行います。


## src/features/lipSync/lipSyncAnalyzeResult.ts

### File Description
このファイルは、`LipSyncAnalyzeResult`という名前のインターフェイスを定義しています。このインターフェイスには、`volume`というプロパティが含まれています。

### Imported Modules
このファイルではモジュールをインポートしていません。

### Functions
このファイルには関数が定義されていません。


## src/features/lipSync/lipSync.ts

### File Description
このファイルは、オーディオ解析とリップシンクアニメーションの更新を行うためのクラスを提供しています。LipSyncクラスは、オーディオコンテキストとオーディオ解析のためのノードを作成し、オーディオデータの取得と処理を行います。

### Imported Modules
- `./lipSyncAnalyzeResult`

### Functions
- `constructor(audio: AudioContext)`: オーディオコンテキストと解析ノードを初期化します。
- `update(): LipSyncAnalyzeResult`: オーディオデータを取得し、ボリュームを計算して返します。
- `playFromArrayBuffer(buffer: ArrayBuffer, onEnded?: () => void)`: 指定されたオーディオバッファーを再生します。
- `playFromURL(url: string, onEnded?: () => void)`: 指定されたURLからオーディオデータを取得し、再生します。


## src/features/messages/speakCharacter.ts

### File Description
このファイルは、VRMモデルに音声を与えるために、様々な音声合成APIを使用する機能を提供しています。異なる音声合成サービスからの音声データを取得し、VRMモデルに再生させることができます。また、英語の単語を日本語の読み方に変換する機能も含まれています。

### Imported Modules
- `@/utils/wait`
- `./synthesizeVoice`
- `./synthesizeVoiceGoogle`
- `./synthesizeStyleBertVITS2`
- `../vrmViewer/viewer`
- `./messages`
- `@/utils/englishToJapanese.json`

### Functions
- `createSpeakCharacter`: VRMモデルに音声を再生させる関数を返します。
- `convertEnglishToJapaneseReading`: 英語の単語を日本語の読み方に変換した文字列を返します。
- `getGoogleTtsType`: 指定された言語コードに対応するGoogle TTSの音声タイプを取得します。
- `getGppgleTtsType`: 指定された言語コードに基づいてGoogle TTSの音声タイプを返します。
- `fetchAudio`: KoeiroAPIを使用して音声データを取得します。
- `fetchAudioVoiceVox`: VoiceVox APIを使用して音声データを取得します。
- `fetchAudioGoogle`: Google TTSを使用して音声データを取得します。
- `fetchAudioStyleBertVITS2`: StyleBertVITS2を使用して音声データを取得します。
- `testVoice`: VoiceVoxを使用してテスト用の音声を再生します。
- `fetchAudioVoiceGSVIApi`: GSVI TTSを使用して音声データを取得します。


## src/features/messages/messages.ts

### File Description
このファイルは、VRMモデルの発話スクリプトを生成する機能を提供しています。発話文と感情表現を入力すると、VRMモデルに適用できる発話スタイルと感情表現のペアを返します。また、発話文の分割や感情表現の解析など、関連する機能も含まれています。

### Imported Modules
- `@pixiv/three-vrm` (VRMExpression, VRMExpressionPresetName)
- `../constants/koeiroParam` (KoeiroParam)

### Functions
- `splitSentence`: 与えられた文字列を句読点で分割し、空の文字列を除去した配列を返します。
- `textsToScreenplay`: 文字列の配列と音声パラメータを受け取り、感情表現と発話スタイルのペアを含む配列を返します。
- `emotionToTalkStyle`: 感情表現を受け取り、対応する発話スタイルを返します。


## src/features/messages/synthesizeStyleBertVITS2.ts

### File Description
このファイルは、StyleBertVITS2 APIを使用して音声合成を行う関数を含んでいます。ユーザーからのメッセージ、StyleBertVITS2サーバーのURL、モデルID、スタイル、言語を受け取り、APIリクエストを送信して音声データを取得します。

### Imported Modules
このファイルではモジュールをインポートしていません。

### Functions
- synthesizeStyleBertVITS2Api: 指定されたメッセージ、StyleBertVITS2サーバーのURL、モデルID、スタイル、言語を使用して、StyleBertVITS2 APIに音声合成リクエストを送信し、音声データを取得する非同期関数。


## src/features/messages/synthesizeVoiceGoogle.ts

### File Description
このファイルは、Google APIを利用して音声合成を行う関数を提供しています。テキストメッセージとTTS（Text-to-Speech）の種類を受け取り、サーバーにPOSTリクエストを送信することで、合成された音声データを取得します。

### Imported Modules
モジュールのインポートはありません。

### Functions
- synthesizeVoiceGoogleApi: 指定されたテキストメッセージとTTS種別を使用して、Google APIを介して音声合成を行い、合成された音声データを返します。


## src/features/messages/synthesizeVoice.ts

### File Description
このファイルは、音声合成のための機能を提供しています。`synthesizeVoice`関数は、指定された文章、話者の特性、話し方のスタイルを使って音声合成を行います。`synthesizeVoiceApi`関数は、APIキーを使って同様の音声合成を行いますが、無料版向けに話し方のスタイルを制限しています。

### Imported Modules
- `@/utils/reduceTalkStyle`
- `../koeiromap/koeiromap`
- `../messages/messages`

### Functions
- `synthesizeVoice`: 指定された文章、話者の特性、話し方のスタイルを使って音声合成を行います。
- `synthesizeVoiceApi`: APIキーを使って音声合成を行い、無料版向けに話し方のスタイルを制限しています。


## src/features/chat/localLLMChat.ts

### File Description
このファイルは、ローカルのLLMモデルにチャットメッセージを送信し、ストリーミングレスポンスを取得するための非同期関数 `getLocalLLMChatResponseStream` を提供しています。Axiosライブラリを使用してローカルLLMサーバーへのPOSTリクエストを送信し、ストリーミングレスポンスを処理します。

### Imported Modules
- axios
- { Message } from '../messages/messages'

### Functions
- getLocalLLMChatResponseStream: 指定されたチャットメッセージ、ローカルLLMのURL、およびモデル名(オプション)を使用して、ローカルLLMからストリーミングレスポンスを取得する非同期関数。レスポンスは ReadableStream として返されます。


## src/features/chat/anthropicChat.ts

### File Description
このファイルには、Anthropic APIを使用してチャット応答を取得するための2つの関数が含まれています。1つはリクエストを送信してチャット応答を取得する関数、もう1つはストリーミング形式でチャット応答を取得する関数です。

### Imported Modules
- `../messages/messages` (Message型のインポート)

### Functions
- `getAnthropicChatResponse`: Anthropic APIにリクエストを送信し、チャット応答を取得する関数。引数として、メッセージの配列、APIキー、モデル名を受け取ります。
- `getAnthropicChatResponseStream`: Anthropic APIにリクエストを送信し、ストリーミング形式でチャット応答を取得する関数。引数として、メッセージの配列、APIキー、モデル名を受け取ります。


## src/features/chat/openAiChat.ts

### File Description
このファイルは、OpenAI の API を使用してチャットレスポンスを取得するための関数を提供しています。ストリーミングによる応答取得と、一度に全てのレスポンスを取得する2つの方法が用意されています。

### Imported Modules
- { OpenAI } from "openai"
- { Message } from "../messages/messages"
- { ChatCompletionMessageParam } from "openai/resources"

### Functions
- getOpenAIChatResponse: 与えられた API キーとモデルを使って OpenAI から一括のチャットレスポンスを取得します。
- getOpenAIChatResponseStream: 与えられた API キーとモデルを使って OpenAI からストリーミングによるチャットレスポンスを取得します。


## src/features/chat/googleChat.ts

### File Description
このファイルは、Google Generative AIのAPIを使ってチャットレスポンスを取得するための機能を提供しています。メッセージ履歴と最新のユーザーメッセージを渡すと、Google Generative AIモデルからテキストレスポンスを取得できます。レスポンスを一括で取得するか、ストリーミングで取得するかを選択できます。

### Imported Modules
- @google/generative-ai
- ../messages/messages

### Functions
- getGoogleChatResponse: 指定されたメッセージ履歴と最新のユーザーメッセージに対して、Google Generative AIモデルからテキストレスポンスを取得します。
- getGoogleChatResponseStream: 指定されたメッセージ履歴と最新のユーザーメッセージに対して、Google Generative AIモデルからストリーミングでテキストレスポンスを取得します。
- processMessages: メッセージの履歴とシステムメッセージを抽出し、Google Generative AIモデルに適した形式に変換します。


## src/features/chat/groqChat.ts

### File Description
このファイルには、Groq APIとやり取りするための2つの関数が含まれています。一方は単一の応答を取得し、もう一方はストリームされた応答を取得します。

### Imported Modules
- `Message` from "../messages/messages"

### Functions
- `getGroqChatResponse`: 与えられたメッセージ、APIキー、モデルを使用して、Groq APIから単一の応答を取得します。
- `getGroqChatResponseStream`: 与えられたメッセージ、APIキー、モデルを使用して、Groq APIからストリームされた応答を取得します。応答は適切に処理され、完全なメッセージだけがストリームされます。


## src/features/chat/difyChat.ts

### File Description
このファイルは、Anthropic の API を使って会話のストリームを取得する関数 `getDifyChatResponseStream` を定義しています。この関数は、メッセージの配列、API キー、URL、会話 ID、会話 ID を設定する関数を受け取り、ストリーミングレスポンスの ReadableStream を返します。

### Imported Modules
- `{ Message }` from "../messages/messages"

### Functions
- `getDifyChatResponseStream`: 与えられた入力に基づいて、Anthropic API からストリーミングレスポンスを取得する。入力エラーがある場合は例外をスローする。レスポンスを解析して、データを返すストリームを作成する。


## src/features/chat/aiChatFactory.ts

### File Description
このファイルは、さまざまなAIサービス（OpenAI、Anthropic、Google、LocalLLM、Groq、Dify）とのチャット応答ストリームを取得するための機能を提供しています。各AIサービスごとに対応する関数が用意されており、与えられたメッセージとサービス設定に基づいて応答ストリームを返します。

### Imported Modules
- `@/features/messages/messages`
- `./openAiChat`
- `./anthropicChat`
- `./googleChat`
- `./localLLMChat`
- `./groqChat`
- `./difyChat`

### Functions
- `getAIChatResponseStream`: 指定されたAIサービスとメッセージ、設定に基づいてチャット応答ストリームを取得する。サポートされていないサービスの場合はエラーをスローする。


## src/features/constants/systemPromptConstants.ts

### File Description
このファイルは、対話システムの一部として使用されるシステムプロンプトのテキストを含んでいます。ユーザーに対して自然な会話を行うためのルールと例が記載されています。

### Imported Modules
このファイルではモジュールをインポートしていません。

### Functions
このファイルには関数は定義されていません。代わりに、`SYSTEM_PROMPT`という定数が exports されています。


## src/features/constants/koeiroParam.ts

### File Description
このファイルは、スピーカーの位置を表すパラメータ `KoeiroParam` の型と、デフォルト値とプリセットの値を定義しています。`KoeiroParam` は `speakerX` と `speakerY` の2つの数値プロパティを持つオブジェクト型です。

### Imported Modules
このファイルでは外部のモジュールがインポートされていません。

### Constants
- `DEFAULT_PARAM`: デフォルトのスピーカー位置パラメータ (`speakerX: 3`, `speakerY: 3`)
- `PRESET_A`: プリセットA (`speakerX: 4.5`, `speakerY: 10`)
- `PRESET_B`: プリセットB (`speakerX: 3`, `speakerY: 3`)
- `PRESET_C`: プリセットC (`speakerX: -5.5`, `speakerY: -3`)
- `PRESET_D`: プリセットD (`speakerX: 3.5`, `speakerY: -8`)


## src/features/vrmViewer/viewerContext.ts

### File Description
このファイルは、React の Context APIを使用してViewerオブジェクトをグローバルに利用可能にするための設定を行っています。ViewerオブジェクトはViewerクラスのインスタンスで、ファイル内で作成されています。

### Imported Modules
- react
- ./viewer

### Functions
- なし


## src/features/vrmViewer/model.ts

### ファイルの説明
このファイルは、Three.jsを使用して3Dキャラクターをロードおよび操作するためのクラスを提供しています。VRMモデルのロードや、アニメーション、リップシンク、表情制御などの機能を備えています。

### インポートされたモジュール
- three
- @pixiv/three-vrm
- three/examples/jsm/loaders/GLTFLoader
- ../../lib/VRMAnimation/VRMAnimation
- @/lib/VRMLookAtSmootherLoaderPlugin/VRMLookAtSmootherLoaderPlugin
- ../lipSync/lipSync
- ../emoteController/emoteController
- ../messages/messages

### 関数
- loadVRM(url: string): Promise<void>: 指定されたURLからVRMモデルをロードします。
- unLoadVrm(): VRMモデルをアンロードします。
- loadAnimation(vrmAnimation: VRMAnimation): Promise<void>: VRMアニメーションをロードします。
- speak(buffer: ArrayBuffer, screenplay: Screenplay): Promise<void>: 音声バッファを再生し、リップシンクとキャラクターの表情制御を行います。
- update(delta: number): void: アニメーションやリップシンクの更新を行います。


## src/features/vrmViewer/viewer.ts

### File Description
このファイルは、Three.jsライブラリを使用して3Dビューワーを構築するためのコードを含んでいます。VRMモデルの読み込み、アニメーション、カメラ制御、レンダリングなどの機能を提供しています。

### Imported Modules
- *as THREE from "three"
- { Model } from "./model"
- { loadVRMAnimation } from "@/lib/VRMAnimation/loadVRMAnimation"
- { buildUrl } from "@/utils/buildUrl"
- { OrbitControls } from "three/examples/jsm/controls/OrbitControls"

### Functions
- loadVrm(url: string): VRMモデルを指定されたURLから読み込みます。
- unloadVRM(): 読み込まれたVRMモデルをアンロードします。
- setup(canvas: HTMLCanvasElement): Reactで管理されているCanvasを設定し、レンダラー、カメラ、コントロールを初期化します。
- resize(): canvasの親要素のサイズに合わせてレンダラーとカメラを調整します。
- resetCamera(): VRMのheadノードを参照してカメラ位置を調整します。
- update(): アニメーションの更新とレンダリングを行うメソッドで、requestAnimationFrameで再帰的に呼び出されます。


## src/features/youtube/conversationContinuityFunctions.ts

### File Description
このファイルは、ChatGPTやAnthropicなどのAIサービスと対話し、返答を生成するための関数を提供しています。メッセージの履歴や選択肢となるコメントから最適なコメントを選択したり、新しい話題への切り替えや会話の継続に必要な発言を生成したりする機能があります。

### Imported Modules
- `@/features/messages/messages`
- `@/features/chat/openAiChat`
- `@/features/chat/anthropicChat`

### Functions
- `fetchAIResponse`: 指定されたAIサービスとモデルを使って、与えられたメッセージに対する応答を取得します。
- `getLastMessages`: メッセージの配列から指定された数の最新メッセージを取得し、文字列として返します。
- `getModifiedSystemMessage`: 与えられたシステムメッセージを修正し、キャラクター設定を追加した新しいシステムメッセージを返します。
- `getBestComment`: 会話の履歴とYouTubeのコメントから、最適なコメントを選択します。
- `getMessagesForSleep`: 与えられたシステムプロンプトから、ユーザーがYouTubeの配信者であることを想定した休憩用のメッセージを生成します。
- `getAnotherTopic`: 最新の会話履歴から関連する別の話題を取得します。
- `getMessagesForNewTopic`: 指定された新しい話題について、会話を切り替えるためのメッセージを生成します。
- `checkIfResponseContinuationIsRequired`: 会話の履歴から、次の発言者が現在の話者を継続すべきかどうかを判断します。
- `getMessagesForContinuation`: 会話を継続するためのメッセージを生成します。


## src/features/youtube/youtubeComments.ts

### File Description
このファイルは、YouTubeライブチャットからコメントを取得し、それに応じて適切な応答を生成する機能を提供しています。会話の継続性を維持しながら、新しいトピックを導入したり、一定期間コメントがない場合にスリープモードに入ったりする機能も備えています。

### Imported Modules
- `@/features/messages/messages`からMessage型をインポート
- `@/features/youtube/conversationContinuityFunctions`から以下の関数をインポート
  - getBestComment
  - getMessagesForSleep
  - getAnotherTopic
  - getMessagesForNewTopic
  - checkIfResponseContinuationIsRequired
  - getMessagesForContinuation

### Functions
- `getLiveChatId`: 指定されたYouTubeライブIDからアクティブなライブチャットIDを取得する関数。
- `retrieveLiveComments`: 指定されたライブチャットIDとYouTubeAPIキーを使用して、ライブチャットのコメントを取得する関数。
- `fetchAndProcessComments`: ライブチャットからコメントを取得し、適切な応答を生成する主要な関数。会話の継続性、新しいトピックの導入、スリープモードなどの機能を提供する。


## src/features/googletts/googletts.ts

### File Description
このファイルは、Google Cloud Text-to-Speech APIを使って、指定されたメッセージをオーディオデータに変換するための関数を含んでいます。指定された言語とTTSタイプに基づいて、テキストをリニア16エンコーディングのオーディオデータに変換します。

### Imported Modules
- @google-cloud/text-to-speech

### Functions
- googleTts: 指定されたメッセージとTTSタイプを受け取り、Google Cloud Text-to-Speech APIを使ってオーディオデータを生成し、そのオーディオデータを返す関数。


## src/features/koeiromap/koeiromap.ts

### File Description
このファイルには、音声合成APIである「koeiro」と「koeiromap」の2つの関数が含まれています。これらの関数は、指定されたテキストと話者の位置情報、話し方のスタイルを受け取り、音声データを生成して返すことができます。

### Imported Modules
- なし

### Functions
- koeiromapV0: 無料版のkoeiro APIを使用して音声データを生成する関数です。
- koeiromapFreeV1: 有料版のkoeiromap APIを使用して音声データを生成する関数です。APIキーが必要です。


## src/utils/reduceTalkStyle.ts

### File Description
このファイルは、koeiromap Free v1の制限に対応するための声色パラメータを制限する機能を提供しています。具体的には、許可された3つの声色パラメータ(`"talk"`, `"happy"`, `"sad"`)のみを受け入れ、それ以外の値が渡された場合は`"talk"`に変換する関数が定義されています。

### Imported Modules
インポートされているモジュールはありません。

### Functions
- `reduceTalkStyle`: 渡された`talkStyle`が`"talk"`、`"happy"`、`"sad"`のいずれかである場合はそのままを返し、それ以外の場合は`"talk"`を返す関数。koeiromap Free v1の制限に対応するために使用されます。


## src/utils/wait.ts

### File Description
このファイルは、非同期処理のためのユーティリティ関数を定義しています。具体的には、指定された時間(ミリ秒)だけ待機する機能を提供します。

### Imported Modules
なし

### Functions
- wait: 指定された時間(ミリ秒)だけ待機するPromiseを返す関数です。


## src/utils/buildUrl.ts

### File Description
このファイルは、Next.jsアプリケーションにおけるアセットの読み込み方法を定義しています。特に、GitHub Pagesに公開したときにアセットが正しく読み込まれるように、環境変数に基づいてURLにリポジトリ名を追加する関数を提供しています。

### Imported Modules
- next/config

### Functions
- buildUrl(path: string): string: 与えられたパスに対して、アプリケーションのルートURLを追加した完全なURLを返す。GitHub Pagesに公開されたアプリケーションでアセットを正しく読み込めるようにするために使用される。


## src/styles/globals.css

### File Description
このファイルは、Tailwind CSSのセットアップとスタイルのカスタマイズを行っています。背景画像の設定、カスタムレンジスライダーのスタイル、スクロールバーの非表示機能を提供しています。

### Imported Modules
モジュールはインポートされていません。

### Functions
関数は定義されていません。


## src/components/settings.tsx

### File Description

このファイルは、チャットアシスタントアプリケーションの設定ページのReactコンポーネントです。様々な設定項目を含む大規模なコンポーネントで、言語選択、キャラクター名の表示、音声エンジンの選択、AIサービスの選択、APIキーの入力、チャットログの編集などの機能があります。

### Imported Modules

- React
- useEffect (React)
- IconButton (カスタムコンポーネント)
- TextButton (カスタムコンポーネント)
- Message (カスタムコンポーネント)
- GitHubLink (カスタムコンポーネント)
- KoeiroParam, PRESET_A, PRESET_B, PRESET_C, PRESET_D (カスタムコンポーネント)
- Link (カスタムコンポーネント)
- i18next (翻訳ライブラリ)
- useTranslation (i18next)
- speakers.json (VoiceVox話者データ)

### Functions

- Settings: メイン設定コンポーネント。様々な props を受け取り、設定項目を描画します。


## src/components/chatLog.tsx

### File Description
このファイルは、ReactコンポーネントとしてのChatLogとChatを定義しています。ChatLogは、チャットメッセージのログとスクロール機能を提供し、Chatはそれぞれのメッセージを表示するためのコンポーネントです。

### Imported Modules
- react (useEffect, useRef)
- @/features/messages/messages (Message)

### Functions
- ChatLog: チャットメッセージの一覧を表示し、新しいメッセージが追加されるたびにスクロールする機能を持つコンポーネント。
- Chat: 個々のチャットメッセージを表示するコンポーネント。メッセージのロール (user や assistant) に応じて、スタイルを変更します。


## src/components/messageInput.tsx

### File Description
このファイルは、Reactコンポーネント`MessageInput`を定義しています。このコンポーネントは、ユーザーがメッセージを入力し、送信するためのインターフェースを提供します。マイクボタンとメッセージ入力欄、送信ボタンが含まれています。また、チャットの処理中はローディング表示があります。

### Imported Modules
- `IconButton` (from `./iconButton`)
- `useTranslation` (from `react-i18next`)
- `useState`, `useEffect` (from `react`)

### Functions
- `MessageInput`: メッセージ入力コンポーネントを定義する関数コンポーネント。
- `handleKeyPress`: テキストエリアでEnterキーが押された時の処理を行う関数。


## src/components/link.tsx

### File Description
このファイルは、URLとラベルを受け取り、それらを使用してリンクを生成するReactコンポーネントを定義しています。

### Imported Modules
このファイルでは外部モジュールがインポートされていません。

### Functions
- Link: URLとラベルを受け取り、それらを使用してリンクを生成するReactコンポーネントです。リンクは新しいタブで開き、適切なCSSクラスが適用されます。


## src/components/speakers.json

### File Description
このファイルは、様々な話者の情報をリスト形式で含んでいるようです。各話者は、話者の名前、話し方のスタイル(例: 普通、ツンツン、セクシーなど)、およびIDで表されています。

### Imported Modules
このファイルには、モジュールのインポートが含まれていないようです。

### Functions
このファイルには関数が定義されていないようです。これは単にデータを含むリストのようです。


## src/components/meta.tsx

### File Description
このファイルは、Next.jsを使用したWebアプリケーションのためのメタデータを定義しています。タイトル、説明、画像URLなどの情報が設定されており、これらはWebページのHTMLヘッダー要素として挿入されます。

### Imported Modules
- `buildUrl` from `@/utils/buildUrl`
- `Head` from `next/head`

### Functions
- `Meta`: Webサイトのメタデータを定義し、`<Head>` コンポーネントを返します。


## src/components/textButton.tsx

### File Description
このファイルはReactコンポーネントを定義しており、TextButtonという名前の再利用可能なボタンコンポーネントを提供しています。このコンポーネントは、HTMLの`<button>`要素をベースとし、様々なスタイルとプロパティを適用できるようになっています。

### Imported Modules
- `react`

### Functions
- `TextButton`: このコンポーネントは、HTML `<button>` 要素をベースとし、様々なスタイルとプロパティを持つカスタムボタンを提供します。受け取ったプロパティに基づいて、適切なスタイルとコンテンツを適用したボタンを描画します。


## src/components/assistantText.tsx

### File Description
このファイルは、Reactコンポーネント`AssistantText`を定義しています。このコンポーネントは、メッセージ、キャラクター名、およびキャラクター名の表示/非表示を制御するプロップを受け取り、ユーザーインターフェイスにメッセージを表示します。

### Imported Modules
このファイルでは外部モジュールがインポートされていません。

### Functions
- `AssistantText`: メッセージ、キャラクター名、およびキャラクター名の表示/非表示の設定を受け取り、それらを表示するReactコンポーネントを返します。メッセージ内の特定のパターン（`[a-zA-Z]*?]`）が削除されます。


## src/components/codeLog.tsx

### File Description
このファイルは、メッセージのリストを受け取り、それらをコンポーネントとして表示する Reactコンポーネントを定義しています。表示される内容は、メッセージのロールによって異なるスタイルが適用されます。特に、コードやアウトプットの場合は、独自のスタイリングが適用されます。

### Imported Modules
- react
- react (useEffect, useRef)
- @/features/messages/messages (Message)

### Functions
- CodeLog: 受け取ったメッセージのリストを表示するコンポーネント。メッセージの追加時に自動でスクロールします。
- Chat: 個々のメッセージを表示するコンポーネント。メッセージのロールに応じて、スタイリングを変更します。


## src/components/menu.tsx

### File Description
このファイルは、アプリケーションの設定メニューやUIを管理するReactコンポーネントです。様々な機能や設定を制御するためのプロップスやメソッドが定義されています。設定の変更はコールバック関数を介して行われます。

### Imported Modules
- `./iconButton`
- `@/features/messages/messages`
- `@/features/constants/koeiroParam`
- `./chatLog`
- `./codeLog`
- `react`
- `./settings`
- `@/features/vrmViewer/viewerContext`
- `./assistantText`
- `react-i18next`
- `@/features/messages/speakCharacter`

### Functions
- `Menu`: アプリケーションのメインコンポーネント。設定メニューやチャット履歴の表示、様々な設定の変更を行うためのコールバック関数を含む。
- `handleChangeAIService`: AIサービスの変更を処理するコールバック関数。
- `handleChangeSystemPrompt`: システムプロンプトの変更を処理するコールバック関数。
- `handleOpenAiKeyChange`: OpenAI APIキーの変更を処理するコールバック関数。
- `handleAnthropicKeyChange`: Anthropic APIキーの変更を処理するコールバック関数。
- `handleGoogleKeyChange`: Google APIキーの変更を処理するコールバック関数。
- `handleGroqKeyChange`: Groq APIキーの変更を処理するコールバック関数。
- `handleChangeLocalLlmUrl`: ローカルLLMのURLの変更を処理するコールバック関数。
- `handleDifyKeyChange`: Dify APIキーの変更を処理するコールバック関数。
- `handleDifyUrlChange`: Dify URLの変更を処理するコールバック関数。
- `handleDifyConversationIdChange`: Dify会話IDの変更を処理するコールバック関数。
- `handleChangeKoeiromapKey`: koeiromap APIキーの変更を処理するコールバック関数。
- `handleVoicevoxSpeakerChange`: VOICEVOXスピーカーの変更を処理するコールバック関数。
- `handleChangeGoogleTtsType`: Google TTSの種類の変更を処理するコールバック関数。
- `handleChangeStyleBertVits2ServerUrl`: StyleBertVits2サーバーURLの変更を処理するコールバック関数。
- `handleChangeStyleBertVits2ModelId`: StyleBertVits2モデルIDの変更を処理するコールバック関数。
- `handleChangeStyleBertVits2Style`: StyleBertVits2スタイルの変更を処理するコールバック関数。
- `handleYoutubeApiKeyChange`: YouTube APIキーの変更を処理するコールバック関数。
- `handleYoutubeLiveIdChange`: YouTube ライブIDの変更を処理するコールバック関数。
- `handleChangeKoeiroParam`: koeiroパラメータの変更を処理するコールバック関数。
- `handleWebSocketMode`: WebSocketモードの変更を処理するコールバック関数。
- `handleConversationContinuityMode`: 会話の継続モードの変更を処理するコールバック関数。
- `handleClickOpenVrmFile`: VRMファイルを開くためのコールバック関数。
- `handleClickOpenBgFile`: 背景画像ファイルを開くためのコールバック関数。
- `handleClickTestVoice`: 音声の


## src/components/messageInputContainer.tsx

### File Description
このファイルは、テキスト入力と音声入力を提供するReactコンポーネントです。音声認識の完了時は自動で送信され、返答文の生成中は入力が無効化されます。

### Imported Modules
- `@/components/messageInput`
- `react`

### Functions
- `MessageInputContainer`: テキスト入力と音声入力を提供するコンポーネントです。プロップスとして、チャットの処理状況、処理開始時のコールバック関数、音声言語を受け取ります。
- `handleRecognitionResult`: 音声認識の結果を処理する関数です。認識結果をステートに設定し、発言の終了時にはチャット処理を開始します。
- `handleRecognitionEnd`: 音声認識が無音で終了した際のコールバック関数です。マイク録音状態を解除します。
- `handleClickMicButton`: マイクボタンがクリックされた際の処理を行う関数です。マイク録音の開始と停止を切り替えます。
- `handleClickSendButton`: 送信ボタンがクリックされた際の処理を行う関数です。ユーザーの入力内容をもとにチャット処理を開始します。


## src/components/iconButton.tsx

### File Description
このファイルは、React Componentの`IconButton`を定義しています。このコンポーネントは、アイコンと任意のラベルを含むボタンを生成するためのものです。ボタンの状態(処理中や無効など)に応じて、アイコンの変更や無効化を行うことができます。

### Imported Modules
- `@charcoal-ui/icons` からの `KnownIconType`
- `react` からの `ButtonHTMLAttributes`

### Functions
- `IconButton`: アイコンと任意のラベルを含むボタンを生成するReact Componentです。`iconName`プロパティでアイコンの種類を指定し、`isProcessing`プロパティで処理中のスピナーアイコンを表示するかどうかを制御できます。`label`プロパティではボタンのテキストラベルを設定できます。その他の`ButtonHTMLAttributes`を受け取ることができます。


## src/components/githubLink.tsx

### File Description
このファイルは、GitHubリポジトリへのリンクを含むReactコンポーネントを定義しています。コンポーネントは、GitHubのロゴとテキスト "Fork me" を含むボタンを表示します。

### Imported Modules
- Image: Next.jsの画像コンポーネントをインポートしています。
- buildUrl: カスタムユーティリティ関数をインポートしています。

### Functions
- GitHubLink: このコンポーネントは、GitHubリポジトリへのリンクを含むボタンをレンダリングします。ボタンは、GitHubのロゴとテキスト "Fork me" で構成されています。


## src/components/introduction.tsx

### File Description
This file exports a React component called `Introduction`. It provides an introductory modal dialog that displays information about the application, including its description, the technologies used, and the source code repository. The component also includes an option to prevent the introduction from appearing the next time the application is launched.

### Imported Modules
- `react`: Used for React hooks (`useState`, `useCallback`)
- `./link`: Imports a `Link` component
- `./iconButton`: Imports an `IconButton` component
- `i18next`: Used for internationalization (i18n)
- `react-i18next`: Provides the `useTranslation` and `Trans` components for translation

### Functions
- `Introduction`: The main component that renders the introductory modal dialog.
- `handleDontShowIntroductionChange`: A callback function that updates the `dontShowIntroduction` state and calls `updateLanguage`.
- `updateLanguage`: A function that updates the `selectLanguage` and `selectVoiceLanguage` based on the current `i18n.language`.
- `getVoiceLanguageCode`: A utility function that maps the `selectLanguage` to the corresponding voice language code.


## src/components/vrmViewer.tsx

### File Description
このファイルは、React のフックとコンテキストを使用して、VRMビューアコンポーネントを作成しています。キャンバスにVRMモデルをロードし、ドラッグアンドドロップでVRMモデルを差し替えることができます。

### Imported Modules
- react
- ../features/vrmViewer/viewerContext
- @/utils/buildUrl

### Functions
- VrmViewer: VRMビューアコンポーネントを定義する関数です。キャンバスの設定、VRMモデルのロード、ドラッグアンドドロップによるVRMモデルの差し替えを行います。
- canvasRef: キャンバスの参照を取得し、VRMビューアの設定とVRMモデルのロードを行うコールバック関数です。


## src/lib/i18n.js

### File Description
このファイルは、i18next と react-i18next を使用して多言語対応機能を提供するための設定を行っています。利用可能な言語とその翻訳ファイルの場所を指定し、デフォルトの言語とフォールバック言語を設定しています。

### Imported Modules
- i18next
- react-i18next

### Functions
- なし (モジュールの設定とエクスポートのみ)


## src/lib/VRMAnimation/VRMAnimation.ts

### File Description
このファイルは、VRMアニメーションデータを操作するためのクラス `VRMAnimation` を定義しています。このクラスは、VRMモデルのアニメーション情報を扱うための様々なメソッドを提供しています。

### Imported Modules
- `three`
- `@pixiv/three-vrm`

### Functions
- `constructor`: `VRMAnimation` クラスのインスタンスを初期化します。
- `createAnimationClip`: VRMモデルのアニメーションデータを `THREE.AnimationClip` オブジェクトとして作成します。
- `createHumanoidTracks`: VRMモデルのヒューマノイドボーンのアニメーショントラックを作成します。
- `createExpressionTracks`: VRMモデルの表情のアニメーショントラックを作成します。
- `createLookAtTrack`: VRMモデルのLookAtアニメーショントラックを作成します。


## src/lib/VRMAnimation/VRMAnimationLoaderPluginOptions.ts

### File Description
このファイルは、VRMアニメーションローダープラグインのオプションを定義するインターフェイスを含んでいます。

### Imported Modules
なし

### Functions
なし


## src/lib/VRMAnimation/VRMAnimationLoaderPlugin.ts

### File Description
このファイルは、Three.jsのGLTFファイルからVRMアニメーションデータをロードするためのプラグインを実装しています。VRMアニメーションデータからヒューマノイドの骨格アニメーション、表情アニメーション、視線アニメーションを抽出し、Three.jsのアニメーションクリップとして利用できるようにします。

### Imported Modules
- `three`: Three.jsのコアモジュール
- `three/examples/jsm/loaders/GLTFLoader`: GLTFローダーモジュール
- `./VRMAnimationLoaderPluginOptions`: VRMAnimationLoaderPluginのオプション設定用モジュール
- `@gltf-transform/core`: GLTFスキーマ定義モジュール
- `./VRMCVRMAnimation`: VRMアニメーションデータの型定義モジュール
- `@pixiv/three-vrm`: VRMの骨格名とその親子関係を定義したモジュール
- `./VRMAnimation`: VRMアニメーションデータを格納するクラス
- `./utils/arrayChunk`: 配列をチャンクに分割するユーティリティ関数

### Functions
- `VRMAnimationLoaderPlugin`: GLTFLoaderPluginを実装したクラス。VRMアニメーションデータをパースし、Three.jsのアニメーションクリップに変換します。
- `_createNodeMap`: VRMアニメーションデータからノードマップを作成する関数。ヒューマノイド骨格、表情、視線のノードインデックスをマッピングします。
- `_createBoneWorldMatrixMap`: ヒューマノイド骨格のワールド変換行列をマッピングするための関数。
- `_parseAnimation`: VRMアニメーションデータをパースし、VRMAnimationオブジェクトに変換する関数。


## src/lib/VRMAnimation/loadVRMAnimation.ts

### File Description
このファイルは、Three.jsのGLTFLoaderを使用して、VRMアニメーションデータをロードするための機能を提供しています。VRMAnimationLoaderPluginを登録し、loadVRMAnimation関数を使用してアニメーションデータを非同期的に読み込むことができます。

### Imported Modules
- three/examples/jsm/loaders/GLTFLoader
- ./VRMAnimation
- ./VRMAnimationLoaderPlugin

### Functions
- loadVRMAnimation: 指定されたURLからVRMアニメーションデータを非同期的にロードし、VRMAnimationオブジェクトを返すPromiseを返します。データが見つからない場合はnullを返します。


## src/lib/VRMAnimation/VRMCVRMAnimation.ts

### File Description
このファイルは、VRMアニメーションデータの構造を定義するインターフェイスを提供しています。VRMはVRMデータ形式を扱う3D人型モデルのための仕様であり、このインターフェイスはそのアニメーションデータの構造を表現しています。

### Imported Modules
- `@pixiv/three-vrm`

### Functions
なし（このファイルには関数は定義されていません）

### Interfaces
- `VRMCVRMAnimation`: VRMアニメーションデータの構造を定義するインターフェイス。以下のプロパティを持ちます。
  - `specVersion`: 仕様のバージョンを表す文字列
  - `humanoid.humanBones`: VRMの人型ボーンの構造を定義するオブジェクト
  - `expressions?.preset`: VRM表情プリセットの構造を定義するオブジェクト
  - `expressions?.custom`: カスタム表情の構造を定義するオブジェクト
  - `lookAt`: 視線の構造を定義するオブジェクト


## src/lib/VRMAnimation/utils/linearstep.ts

### File Description
このファイルは、線形補間関数を実装しています。`linearstep`関数は、指定された範囲内の値を線形的に補間します。`saturate`関数は別のファイルからインポートされており、値を0と1の範囲に制限する役割を持っています。

### Imported Modules
- `saturate` from `./saturate`

### Functions
- `linearstep(a: number, b: number, t: number)`: 引数`a`と`b`で定義された範囲内の値`t`を線形的に補間します。値が範囲外の場合は`saturate`関数を使用して0または1に制限されます。


## src/lib/VRMAnimation/utils/saturate.ts

### File Description
このファイルは、数値を0と1の範囲に制限する`saturate`という関数を定義しています。この関数は、与えられた数値が0未満の場合は0に、1を超える場合は1に丸められます。

### Imported Modules
このファイルではモジュールをインポートしていません。

### Functions
- `saturate`: 与えられた数値を0と1の範囲に制限します。数値が0未満の場合は0に、1を超える場合は1に丸められます。


## src/lib/VRMAnimation/utils/arrayChunk.ts

### File Description
このファイルは、指定された間隔ごとに配列の要素を分割して、新しい二次元配列を返す `arrayChunk` 関数を定義しています。この関数は、ジェネリックな型パラメータ `T` を使用しているため、様々な型の配列に対して適用できます。

### Imported Modules
なし

### Functions
- `arrayChunk<T>(array: ArrayLike<T>, every: number): T[][]`: 指定された `every` の値ごとに配列の要素を分割し、新しい二次元配列を返します。入力の `array` は `ArrayLike` の型を持つ必要があります。


## src/lib/VRMLookAtSmootherLoaderPlugin/VRMLookAtSmoother.ts

### File Description

このファイルは、Three.jsのVRMモデルの視線制御に関する機能を拡張したクラス `VRMLookAtSmoother` を提供しています。従来の `VRMLookAt` クラスに加えて、ユーザーの方向へスムーズに視線を移動させる機能、頭部の回転による視線制御、そして眼球のサッケード運動を再現する機能を追加しています。

### Imported Modules

- `@pixiv/three-vrm`
- `three`

### Functions

- `VRMLookAtSmoother`: VRMモデルの視線制御を拡張したクラス。ユーザーの方向へスムーズに視線を移動させる機能、頭部の回転による視線制御、眼球のサッケード運動を再現する機能を備えています。
- `update(delta: number)`: 各フレームで呼び出され、視線の更新処理を行います。
- `revertFirstPersonBoneQuat()`: レンダリング後に呼び出され、頭部の回転をリセットします。


## src/lib/VRMLookAtSmootherLoaderPlugin/VRMLookAtSmootherLoaderPlugin.ts

### File Description
このファイルは、VRMLookAtSmootherLoaderPluginクラスを定義しています。このクラスは、VRMLookAtLoaderPluginを継承しており、VRMLookAtSmootherクラスを使ってVRMLookAtの動作を滑らかにするための処理を行います。

### Imported Modules
- `@pixiv/three-vrm` から `VRMHumanoid`、`VRMLookAt`、`VRMLookAtLoaderPlugin` をインポートしています。
- `three/examples/jsm/loaders/GLTFLoader` から `GLTF` をインポートしています。
- `./VRMLookAtSmoother` から `VRMLookAtSmoother` をインポートしています。

### Functions
- `get name(): string`: このプラグインの名前を返す関数です。

- `afterRoot(gltf: GLTF): Promise<void>`: GLTFデータの読み込み後に実行される関数です。VRMHumanoidとVRMLookAtオブジェクトを取得し、VRMLookAtSmootherを作成してVRMLookAtオブジェクトを置き換えます。


## src/pages/index.tsx

### File Description

This file appears to be the main component of a React application for a chatbot interface using virtual reality models (VRM). It sets up the state management for various configurations and handles user interactions with the chatbot, including voice synthesis and AI response processing.

### Imported Modules

- `react`: Core React library
- `@/components/vrmViewer`: A custom component for rendering VRM models
- `@/features/vrmViewer/viewerContext`: Context for managing the VRM viewer
- `@/features/messages/messages`: Utilities for handling chat messages and text-to-speech
- `@/features/messages/speakCharacter`: Function for speaking a character's dialogue
- `@/components/messageInputContainer`: A component for user input in the chat
- `@/features/constants/systemPromptConstants`: Constants related to system prompts
- `@/features/constants/koeiroParam`: Constants for koeiromap (voice synthesis) parameters
- `@/features/chat/aiChatFactory`: Functions for handling AI chat responses
- `@/components/introduction`: A component for displaying an introduction
- `@/components/menu`: A component for displaying the application menu
- `@/components/meta`: A component for handling metadata
- `@/lib/i18n`: Internationalization utilities
- `react-i18next`: Library for internationalization in React
- `@/features/youtube/youtubeComments`: Functions for handling YouTube comments
- `@/utils/buildUrl`: Utility function for building URLs

### Functions

- `Home`: The main React component that manages the application state and renders other components.
- `incrementChatProcessingCount`: Increments a counter for ongoing chat processing.
- `decrementChatProcessingCount`: Decrements the counter for ongoing chat processing.
- `handleChangeChatLog`: Updates the chat log with a modified message at a specific index.
- `handleChangeCodeLog`: Updates the code log with a modified message at a specific index.
- `handleSpeakAi`: Handles the text-to-speech synthesis and playback of AI responses.
- `processAIResponse`: Processes the AI response stream and updates the chat log accordingly.
- `preProcessAIResponse`: A wrapper around `processAIResponse` with predefined parameters.
- `handleSendChat`: Handles user input, sends messages to the AI, and processes the response.
- `fetchAndProcessCommentsCallback`: Fetches and processes YouTube comments, integrating with the AI response handling.

The file also includes various state variables and utility functions to manage different aspects of the application, such as voice synthesis settings, AI service configuration, YouTube integration, and more.


## src/pages/_document.tsx

### File Description
このファイルは、Next.js の `Document` コンポーネントを定義しています。`Document` は、HTML ドキュメントの構造を定義するためのカスタマイズが可能な React コンポーネントです。ここでは、Google Fonts の読み込みと、`Main` と `NextScript` コンポーネントをレンダリングする設定が行われています。

### Imported Modules
- `next/document`

### Functions
- `Document`: HTML ドキュメントの構造を定義するカスタマイズ可能な React コンポーネントです。Google Fonts の読み込みと、`Main` と `NextScript` コンポーネントをレンダリングする設定が行われています。


## src/pages/_app.tsx

### ファイル説明
このファイルは、Next.jsアプリケーションのエントリーポイントです。アプリケーションの初期化ロジックと言語設定を含んでいます。

### インポートされたモジュール
- "@/styles/globals.css"
- "next/app"
- "@charcoal-ui/icons"
- "react"
- "../lib/i18n"

### 関数
- App: Next.jsアプリケーションのルートコンポーネントを定義します。ユーザーの言語設定を検出し、i18nライブラリの言語を適切に設定します。


## src/pages/api/anthropic.ts

### File Description
このファイルは、Next.js APIルートハンドラーで、Anthropic AIモデルを利用してメッセージを生成し、ストリーミングまたは単一のレスポンスとして応答を返すためのロジックが含まれています。メッセージの前処理、APIキーの処理、ストリーミング設定に基づいた応答の生成が行われます。

### Imported Modules
- `@anthropic-ai/sdk`: Anthropic AIの公式SDKモジュール
- `next`: Next.jsのAPIルートハンドラーに必要なモジュール
- `@/features/messages/messages`: メッセージデータ構造を定義するカスタムモジュール

### Functions
- `handler`: APIルートハンドラーの関数。Anthropic AIモデルを使用してメッセージを生成し、ストリーミングまたは単一のレスポンスとして応答を返します。


## src/pages/api/chat.ts

### File Description
このファイルは、OpenAI APIを使用してチャットボットの応答を生成するNext.jsのAPIルートハンドラーを定義しています。クライアントからAPIキーとメッセージを受け取り、OpenAIのGPT-3.5-turboモデルを使用して応答を生成し、その応答をクライアントに返します。

### Imported Modules
- openai (Configuration, OpenAIApi)
- next (NextApiRequest, NextApiResponse)

### Functions
- handler: このAPIルートのメイン関数です。クライアントからのリクエストを処理し、OpenAI APIを呼び出して応答を生成し、その応答をクライアントに返します。


## src/pages/api/groq.ts

### File Description
このファイルは、Next.jsのAPIルーターで定義された非同期関数ハンドラーです。メッセージデータ、APIキー、モデル、およびストリーミングフラグを受け取り、Groq APIを使用してOpenAIのChat Completionsを生成します。ストリーミングが有効な場合、チャンクデータをレスポンスストリームに書き込みます。ストリーミングが無効な場合、完全な応答を返します。

### Imported Modules
- `NextApiRequest`、`NextApiResponse` (`next`)
- `Groq` (`groq-sdk`)
- `Message` (`@/features/messages/messages`)

### Functions
- `handler`: APIルートのハンドラー関数。リクエストボディからデータを抽出し、Groq APIを使用してChat Completionsを生成し、レスポンスを返します。


## src/pages/api/tts.ts

### File Description
このファイルは、Next.jsのAPIルートハンドラーで、音声合成の機能を提供しています。クライアントから受け取ったパラメーターに基づいて、音声合成エンジンを選択し、音声データを生成して返します。

### Imported Modules
- `@/features/koeiromap/koeiromap`からの`koeiromapFreeV1`
- `@/features/googletts/googletts`からの`googleTts`

### Functions
- `handler`: クライアントからの音声合成リクエストを処理し、生成された音声データをレスポンスとして返す。パラメーターに基づいて`koeiromapFreeV1`または`googleTts`関数を呼び出す。


## src/pages/api/stylebertvits2.ts

### File Description
このファイルは、Next.js APIルートのハンドラー関数を定義しています。フロントエンドからの要求を受け取り、stylebertvits2サーバーにテキストを送信して音声合成を行い、生成された音声データをクライアントに返します。

### Imported Modules
- `type { NextApiRequest, NextApiResponse } from "next"`

### Functions
- `handler`: フロントエンドからの要求を処理し、stylebertvits2サーバーに音声合成要求を送信して、生成された音声データをクライアントに返す関数です。

