
import pytesseract
from PIL import Image
import os

# Default Windows installation path
tesseract_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

image = Image.open("ocr_sample.png")
text = pytesseract.image_to_string(image)

print("OCR extracted text:")
print(text)
