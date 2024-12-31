import cv2
import pytesseract
from pytesseract import Output
import re
from pdf2image import convert_from_path

def extract_invoice_details_from_pdf(pdf_path):
    # 將 PDF 轉換為影像
    images = convert_from_path(pdf_path)

    # 初始化結果字典
    results = {
        "company_name": None,
        "invoice_number": None,
        "invoice_date": None,
        "tax_excluded_amount": None,
        "tax": None,
        "tax_included_amount": None
    }

    # 定義欄位的正則表達式
    patterns = {
        "company_name": r"(?:公司名稱|發票抬頭)[:：]?\s*(.+)",
        "invoice_number": r"(?:發票號碼|統一發票號碼)[:：]?\s*([A-Z0-9\-]+)",
        "invoice_date": r"(?:日期|開立日期|發票日期)[:：]?\s*(\d{4}[\-/\.]\d{1,2}[\-/\.]\d{1,2})",
        "tax_excluded_amount": r"(?:未稅金額|銷售額)[:：]?\s*([\d,]+\.?\d*)",
        "tax": r"(?:稅金|營業稅)[:：]?\s*([\d,]+\.?\d*)",
        "tax_included_amount": r"(?:已稅金額|總金額)[:：]?\s*([\d,]+\.?\d*)"
    }

    # 處理每一頁影像
    for image in images:
        # 使用 Tesseract OCR 提取文字
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract 路徑
        text = pytesseract.image_to_string(image, lang='chi_tra+eng')

        # 根據正則表達式提取對應欄位
        for field, pattern in patterns.items():
            if not results[field]:  # 只在尚未提取到該欄位時進行匹配
                match = re.search(pattern, text)
                if match:
                    results[field] = match.group(1).strip()

    return results

if __name__ == "__main__":
    # PDF 路徑
    pdf_path = "HF.pdf"  # 替換為您的發票 PDF 檔案路徑

    # 提取發票資料
    invoice_details = extract_invoice_details_from_pdf(pdf_path)

    # 顯示提取結果
    for field, value in invoice_details.items():
        print(f"{field}: {value}")

