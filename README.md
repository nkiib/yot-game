# yot-game
このレポジトリは、ダイスゲーム「ヨット」（ヤッツィー）をPythonで再現したものとなります。シングルプレイのみ対応しています。マルチは、検討中です。

# ルール

「ヨット」を再現しています。ただし、一部「役」が実装されていない可能性があります。

このゲームでは、5つのサイコロを振ります。その出目でポイントを決めるというゲームです。ダイスの出目で役を成立させ、その点数の合計を争います。ただしこのゲームにはパスの概念がないため、たとえ自分が望まない役が0点でもそれを選ばないといけない場面があるかもしれません。

現在実装している役は以下のとおりです。

* ヨット（すべての出目が同じ）
* フルハウス（2つと3つでそれぞれ出目が同じ ex.1,1,2,2,2）
* ビッグストレート（すべての数が連続している ex.1,2,3,4,5）
* スモールストレート（4つ以上が連続している ex.1,2,3,4,6,6）
* フォーカード（4つ以上の出目が同じ ex.1,1,1,1,2）
* チョイス（常時成立）
* エース（常時成立）
* デュース（常時成立）
* スリー（常時成立）
* フォー（常時成立）
* ファイブ（常時成立）
* シックス（常時成立）

## 点数

| 役 | 点数 |
|---|---|
| ヨット | 50 |
| フルハウス | 出目の合計 |
| ビッグストレート | 30 |
| スモールストレート | 15 |
| フォーカード | 出目の合計 |
| チョイス | 出目の合計 |
| エース | 1の合計 |
| デュース | 2の合計 |
| スリー | 3の合計 |
| フォー | 4の合計 |
| ファイブ | 5の合計 |
| シックス | 6の合計 |

最終的に、エース・デュース・スリー・フォー・ファイブ・シックスの合計が63点以上の場合、最終の点数に35点が加わります。
