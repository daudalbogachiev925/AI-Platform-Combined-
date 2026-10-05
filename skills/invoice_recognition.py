import pytesseract
from PIL import Image

def recognize_invoice(path):
    text = pytesseract.image_to_string(Image.open(path), lang="rus")
    return parse_invoice(text)

def parse_invoice(text):
    lines = text.splitlines()
    total = next((l for l in lines if "Итого" in l), "")
    return {"raw": text, "total": total}
