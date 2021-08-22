# convert-jpg-to-pdf
## 概要
複数のjpgファイルをpdfにまとめたいときに使えるツール

## 使い方
0. `pip3 install img2pdf` でimg2pdfライブラリをインストールしておく
1. `convert2pdf.py`と同じディレクトリに、`/tmp/png`という名前のディレクトリを作成
3. `/tmp/png`ディレクトリに、学習に使いたい画像を*.pngという形式で画像を入れる
    * 変換前の拡張子を変えたい場合は`convert2pdf.py`の`extension  = ".png"`を好きな拡張子に変える。
4. `convert2pdf.py`の置いてあるディレクトリで`convert2pdf.py`を実行
    * `python3 convert2pdf.py`
5. `/tmp/png`に`output.pdf`が出来上がる

## tree
<pre>
.
├── README.md   //説明書
├── convert2pdf.py  //実行ファイル
└── tmp //変換処理フォルダ
    └── png //ここに画像をぶっこむと同フォルダに変換したpdfが出来上がる
</pre>
