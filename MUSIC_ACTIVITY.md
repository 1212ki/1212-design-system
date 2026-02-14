# 1212 Design System: Music Activity

音楽活動（アーティスト公式サイト、告知物、簡易的な管理画面など）向けの専用ルールです。

## コアコンセプト

- DIYインディー精神 x 抜け感 x 洗練
- モノクロ基調（黒/白/グレー）に、**テラコッタ `#BF674D` を最小限のアクセント**として使う
- かっこつけすぎず、余白と整列で「ちゃんと感」を担保する

## 色（最重要）

- ベース: 黒 / 白 / グレー
- アクセント: **テラコッタ `#BF674D` のみ**
- アクセント比率: 全体の 10-20% 以下（理想は 5-10%）

## タイポ

- サンセリフ（細字〜レギュラー）中心
- 日本語はゴシックを優先、字間/行間をやや広めに

## トークン（Tokens Studio）

このルールをトークンとして定義したファイル:

- Source: `1212-music.tokens.json`
- Outputs:
  - `dist/1212-music.tokens.json`
  - `dist/1212-music.tokens.css`

### 使い方（Web/CSS）

1. `1212-design-system` でビルド:
   - `python design-builder.py build --src 1212-music.tokens.json`
2. 生成された `dist/1212-music.tokens.css` をプロダクト側へ取り込み
3. UIの色/余白/角丸/影は `--color-*`, `--space-*`, `--radius-*`, `--shadow-*` を使う

## 実装の注意

- 新しい色（別HEX）の増殖は禁止。濃淡は alpha/影/枠で表現する
- コンポーネントは「足す」より「削る」「余白を増やす」を優先する

