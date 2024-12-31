import re
from PyPDF2 import PdfReader

def extract_invoice_numbers_from_pdf(pdf_path):
    """
    從 PDF 文件中提取發票號碼
    :param pdf_path: PDF 文件的路徑
    :return: 發票號碼清單
    """
    # 初始化 PDF 讀取器
    reader = PdfReader(pdf_path)
    all_text = ""

    # 讀取每一頁的內容
    for page in reader.pages:
        all_text += page.extract_text()

    # 使用正則表達式提取發票號碼 (格式假設為 "AB12345678")
    invoice_numbers = re.findall(r'[A-Z]{2}\d{8}', all_text)

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
    # 指定 PDF 檔路徑
    pdf_path = "HF.pdf"  # 替換為你的 PDF 文件路徑
    output_file = "invoice_numbers.txt"

    # 提取發票號碼
    invoice_numbers = extract_invoice_numbers_from_pdf(pdf_path)

    if invoice_numbers:
        print(f"提取到的發票號碼: {invoice_numbers}")
        
        # 將發票號碼存入檔案
        save_to_file(invoice_numbers, output_file)
        print(f"發票號碼已存入檔案: {output_file}")
    else:
        print("未能提取到發票號碼，請檢查 PDF 文件格式或內容。")
