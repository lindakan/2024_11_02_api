import cv2
import pytesseract
from PIL import Image
import re

# 設定 Tesseract 執行檔位置（請修改為你的 Tesseract 路徑）
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_invoice_number(image_path):
    """
    從發票影像中提取發票號碼
    :param image_path: 發票影像的路徑
    :return: 發票號碼清單
    """
    # 讀取影像
    image = cv2.imread(image_path)
    
    # 轉為灰階以提高 OCR 成效
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 使用 OCR 提取文字
    text = pytesseract.image_to_string(gray, lang='eng')

    # 使用正則表達式提取發票號碼（假設格式為英數組合，如 "AB12345678"）
    invoice_numbers = re.findall(r'[A-Z]{2}\d{8}', text)

    return invoice_numbers

def save_to_file(invoice_numbers, output_file):
    """
    將發票號碼存入檔案
    :param invoice_numbers: 發票號碼清單
    :param output_file: 輸出的檔案路徑
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        for number in invoice_numbers:
            file.write(f"{number}\n")

# 主程式
if __name__ == "__main__":
    # 指定影像路徑
    image_path = "invoice_sample.jpg"  # 替換為你的發票影像
    output_file = "invoice_numbers.txt"

    # 提取發票號碼
    invoice_numbers = extract_invoice_number(image_path)
    if invoice_numbers:
        print(f"提取到的發票號碼: {invoice_numbers}")
        
        # 將發票號碼存入檔案
        save_to_file(invoice_numbers, output_file)
        print(f"發票號碼已存入檔案: {output_file}")
    else:
        print("未能提取到發票號碼，請檢查發票格式或影像品質。")
