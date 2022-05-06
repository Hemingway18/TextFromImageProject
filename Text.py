import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def get_text(file, lang='eng'):
    return pytesseract.image_to_string(file, lang)
