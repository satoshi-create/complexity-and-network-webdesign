import os
import pytesseract
from pdf2image import convert_from_path

# PDFファイルパス
PDF_PATH = '../data/raw/machida_gomi.pdf'
OUTPUT_DIR = '../data/ocr_text'

# 出力ディレクトリが無ければ    作成
os.makedirs(OUTPUT_DIR, exist_ok=True)

# PDF → 画像に変換
images = convert_from_path(PDF_PATH, dpi=300)

# ページごとにOCR実行
for i, img in enumerate(images):


    custom_config = r'--psm 6'  # レイアウト認識モードの調整
    text = pytesseract.image_to_string(img, lang='jpn', config=custom_config)

    # text = pytesseract.image_to_string(img, lang='jpn')

    output_path = os.path.join(OUTPUT_DIR, f'page_{i+1}.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'✅ OCR done: page_{i+1}.txt')

print('🎉 OCR extraction complete!')
