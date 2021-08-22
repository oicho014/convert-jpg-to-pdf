import os
import img2pdf
from PIL import Image # img2pdfと一緒にインストールされたPillowを使う

if __name__ == '__main__':
    pdf_FileName = "/tmp/jpg/output.pdf" # 出力するPDFの名前
    jpg_Folder = "/tmp/jpg/" # 画像フォルダ
    extension  = ".jpg" # 拡張子がjpgのものを対象
    listfolder = os.listdir(jpg_Folder)
    sortfolder = sorted(listfolder, key=lambda s: int(re.search(r'\d+', s).group()))

    with open(pdf_FileName,"wb") as f:
        # 画像フォルダの中にあるjpgファイルを取得し配列に追加、バイナリ形式でファイルに書き込む
        f.write(img2pdf.convert([Image.open(jpg_Folder+j).filename for j in os.listdir(jpg_Folder)if j.endswith(extension)]))
