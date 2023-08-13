# [日本の選挙運動](https://politic-partner.github.io/election-campaign/)
この Web サイトは日本の選挙運動を執筆するための GitHub リポジトリです。
文書を読みたい方は[日本の選挙運動の GitHub Pages](https://politic-partner.github.io/election-campaign/)で読むことができます。

# みんなで情報を集めましょう

## 書き方の方針

### 柔らかい表現
できるだけ堅い表現をさけて柔らかい表現を使いましょう。

| 堅い表現 | 柔らかい表現 | 
| ------- | ---------- |
| ❌️ 行う | ⭕️ する |
| ❌️ 異なる | ⭕️ ちがう |

[ひらがな書きが適当な語](http://www.yamanouchi-yri.com/yrihp/techwrt-2-4s/t-2-4s03a.htm)を意識しましょう。

### 定量的な表現
できるだけ定性的な表現をさけて定量的な表現を使いましょう。

| 定性的な表現 | 定量的な表現 | 
| ------- | ---------- |
| ❌️ たくさん | ⭕️ 100個 |
| ❌️ すごく | ⭕️ 200℃ |
| ❌️ そのうち | ⭕️ 3日以内 |

## 技術的なメモ
- [Sphinx](https://www.sphinx-doc.org/ja/master/index.html)ドキュメント生成ツール
- [Markdown](https://myst-parser.readthedocs.io/en/latest/syntax/optional.html) シンタックス
  - [Roles and Directives](https://myst-parser.readthedocs.io/en/latest/syntax/roles-and-directives.html) コードブロックでディレクティブが利用できます
    ````
    ```{toctree}
    :hidden:
    volunteer/index
    staff/index
    reference
    ```
    ````
- [Twitter/Facebookへのページシェアでコンテンツを埋め込む(OGP)](https://sphinx-users.jp/cookbook/ogp/index.html)

