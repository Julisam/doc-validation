import base64
import io
from pdf2image import convert_from_bytes

def convert_pdf_to_image(pdf_encoded, dpi=200):
    """
    Converts a base64-encoded PDF to a list of base64-encoded PNG images.

    Parameters:
    - pdf_encoded (str): Base64-encoded PDF.
    - dpi (int): Dots per inch for the output image quality.

    Returns:
    - List[str]: A list of base64-encoded PNG images (one per page).
    """
    # Decode the base64 PDF to bytes
    pdf_bytes = base64.b64decode(pdf_encoded)
    
    # Convert PDF pages to PIL images
    images = convert_from_bytes(pdf_bytes, dpi=dpi)
    
    # Encode each image to base64 PNG
    encoded_images = []
    for img in images:
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        encoded_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        encoded_images.append(encoded_image)
    
    return encoded_images
