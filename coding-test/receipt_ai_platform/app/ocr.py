import pytesseract
from PIL import Image
from dotenv import load_dotenv
import re
import os

load_dotenv()

tess_cmd = os.getenv("TESSERACT_CMD")
if tess_cmd:
    pytesseract.pytesseract.tesseract_cmd = tess_cmd


def extract_receipt_text(image_path: str) -> str:
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    print("Extracted Text:\n", text)
    return text


def parse_receipt(text: str) -> dict:
    lines = text.split("\n")
    items = []
    receipt_date = None
    merchant = None

    date_match = re.search(r"Receipt date[:\s]+(\d{2}-\d{2}-\d{4})", text, re.IGNORECASE)
    if date_match:
        receipt_date = date_match.group(1)

    for line in lines:
        if re.search(r"(inc|company|store|shop)", line, re.IGNORECASE):
            merchant = line.strip()
            break

    for line in lines:
        match = re.match(r"(\d+)\s+(.+?)\s+([\d]+\.\d{2})\s+\$([\d]+\.\d{2})", line)
        if match:
            qty, item_name, unit_price, total_price = match.groups()

            if any(keyword in item_name.lower() for keyword in ["subtotal", "tax", "total"]):
                continue

            items.append(
                {
                    "item": item_name.strip(),
                    "quantity": int(qty),
                    "unit_price": float(unit_price),
                    "price": float(total_price),
                }
            )

    return {
        "items": items,
        "date": receipt_date,
        "merchant": merchant
    }