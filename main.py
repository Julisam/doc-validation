from fastapi import FastAPI, File, UploadFile, HTTPException
import os 
import sys
sys.path.append(os.getcwd())

# Import text extraction and LLM functions from the modularized app
from app.extraction import extract_text_from_pdf, extract_text_from_image
from app.llm import classify_and_extract_birth_certificate

app = FastAPI()

@app.post("/extract/")
async def extract_text(file: UploadFile = File(...)):
    """
    Endpoint to extract text from an uploaded document and classify it as a birth certificate.
    
    Parameters:
    - file (UploadFile): The document file uploaded by the client (PDF or PNG).

    Returns:
    - JSON object containing:
        - 'document_type': Type of the document (e.g., 'birth_certificate' or 'unknown').
        - 'fields': Extracted fields if the document is a birth certificate.
    
    Raises:
    - HTTPException with status code 400 if the file type is unsupported.
    - HTTPException with status code 500 if any error occurs during processing.
    """
    try:
        contents = await file.read()

        content_type = file.content_type
        
        # Extract text from the document
        if content_type == "image/png":
            text = extract_text_from_image(contents)

        elif content_type == "application/pdf":
            text = extract_text_from_pdf(contents)

        # Raise an error if the file type is not supported
        else:
            raise HTTPException(status_code=400, detail="Only Image and PDF files are supported.")
        
        # Use the LLM to classify the document and extract relevant fields
        output = classify_and_extract_birth_certificate(text)

        return output
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
