import pytesseract
from PIL import Image
import io
from pdf2image import convert_from_bytes

def extract_text_from_image(file_content):
    """Extracts text from an Image file.

    Args:
        file_content (bytes): The binary content of the image file.

    Returns:
        str: The extracted text from the image.
    """
    image = Image.open(io.BytesIO(file_content))
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(file_content):
    """Extracts text from a PDF file.

    Args:
        file_content (bytes): The binary content of the PDF file.

    Returns:
        str: The extracted text from all pages of the PDF.
    """
    all_pages = convert_from_bytes(file_content)
    page_texts = []
    for i, page in enumerate(all_pages):
        text = f'Page {i+1} \n' + pytesseract.image_to_string(page)
        page_texts.append(text)
    page_texts = "\n".join(page_texts)
    return text