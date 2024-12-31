import cv2
import pytesseract
from pytesseract import Output
import re

def extract_invoice_details(image_path):
    # 加載影像
    image = cv2.imread(image_path)

    # 使用 Tesseract OCR 提取文字
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract 路徑
    text = pytesseract.image_to_string(image, lang='chi_tra+eng')

    # 定義欄位的正則表達式
    patterns = {
        "company_name": r"(?:公司名稱|發票抬頭)[:：]?\s*(.+)",
        "invoice_number": r"(?:發票號碼|統一發票號碼)[:：]?\s*([A-Z0-9\-]+)",
        "invoice_date": r"(?:日期|開立日期|發票日期)[:：]?\s*(\d{4}[\-/\.]\d{1,2}[\-/\.]\d{1,2})",
        "tax_excluded_amount": r"(?:未稅金額|銷售額)[:：]?\s*([\d,]+\.?\d*)",
        "tax": r"(?:稅金|營業稅)[:：]?\s*([\d,]+\.?\d*)",
        "tax_included_amount": r"(?:已稅金額|總金額)[:：]?\s*([\d,]+\.?\d*)"
    }

    # 初始化結果字典
    results = {}

    # 根據正則表達式提取對應欄位
    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        results[field] = match.group(1).strip() if match else None

    return results

if __name__ == "__main__":
    # 發票影像路徑
    image_path = "invoice_sample.jpg"  # 替換為您的發票影像路徑

    # 提取發票資料
    invoice_details = extract_invoice_details(image_path)

    # 顯示提取結果
    for field, value in invoice_details.items():
        print(f"{field}: {value}")
