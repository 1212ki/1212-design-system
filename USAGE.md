# 1212 Design System 使い方（初心者向け）

このファイルは、デザインシステムの基本運用を「知識ゼロ」前提でまとめたものです。

## まず知っておくこと
- このリポジトリが「デザインの正」です
  - 正（ソース）: `1212-core.tokens.json`
  - 出力（参照用）: `dist/1212-core.tokens.json`, `dist/1212-core.tokens.css`
- Figma側は「見える化・共有・UI作成の場」です
- Tokens Studioは **GitHub ↔ Figma をつなぐ同期ツール** です

## 用語の超ざっくり説明
- トークン: 色/文字/余白/角丸/影などの「名前付きの数値」
  - 例: `color.primary = #E46F4D`
- Styles/Variables: Figma内で使える「トークンの実体」
  - 画面作成時に選べるようになります

## 初回セットアップ（Figma）
1. デザインシステム用のFigmaファイルを開く
2. `Tokens Studio` を開く
3. Sync設定（GitHub）
   - Repository: `1212ki/1212-design-system`
   - Branch: `main`
   - Token storage location: `1212-core.tokens.json`
4. `Pull` を押す
5. `global` をON
6. `Apply` → **Whole document** を選ぶ

※この操作は「キャンバスの見た目は変わらない」のが普通です。
右パネルの **Styles/Variables** に追加されていれば成功です。

## 日々の更新フロー（推奨）
1. `1212-core.tokens.json` を編集
2. `python3 design-builder.py build`
3. 直接コミット&push（main）
4. Figmaで `Pull` → `Apply`（Whole document）

## プロダクト（例: kondate-loop）での使い方
1. デザインシステムFigmaでコンポーネントを作る
2. LibraryをPublish
3. kondate-loop側のFigmaでLibraryを有効化
4. Styles/Variablesとコンポーネントを使ってUIを作成

## 他プロダクトに割り当てる例
例: 新プロダクト「foo-app」を作る場合
1. `1212 Design System` のFigmaを最新化（Pull → Apply）
2. 必要ならコンポーネントを追加してLibraryをPublish
3. `foo-app` のFigmaファイルを作成
4. Assets → Libraries で `1212 Design System` をON
5. 以後は Styles/Variables とコンポーネントを使ってUIを作る

プロダクト固有の色が必要な場合は、
`foo-theme.tokens.json` のような差分トークンを追加して上書き運用します。

## よくある詰まり
- Pullしても何も出ない
  - Token storage location が `1212-core.tokens.json` になっているか確認
- Apply後に何も変わらない
  - 見た目は変わりません。Styles/Variablesに追加されているか確認
- 影や余白が見えない
  - 右パネルの入力欄の「変数アイコン」から選べる仕様です

## 方針（運用ルール）
- 変更は **JSONが正**。Figmaでの直接編集は最小限
- UIが増えるほど、トークンで統一するほど楽になる
- プロダクトごとの差分が必要になったら
  - `kondate-theme.tokens.json` のような「差分トークン」を追加する
