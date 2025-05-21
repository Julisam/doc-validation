# from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi import FastAPI, HTTPException
import os 
# from typing import Dict, List, Optional
# import base64

import sys
sys.path.append(os.getcwd())

# Import text extraction and LLM functions from the modularized app
from app.conversion import convert_pdf_to_image
from app.llm import generate_response
# from app.validation import validate

from app.model import DocumentExtractionRequest
from app.prompt import engineer_prompt

app = FastAPI()

@app.post("/extract/")
async def extract_text(payload: DocumentExtractionRequest):
    """
    Endpoint to extract text from an uploaded document and evaluate it.
    
    Args:
        - payload (DocumentExtractionRequest): The request payload containing document details.

    Returns:
        - JSON object containing:
            - 'document_type': Type of the document (e.g., 'birth_certificate' or 'unknown').
            - 'extracted_fields': Extracted fields if the document is a birth certificate.
        
        Raises:
        - HTTPException with status code 400 if the file type is unsupported.
        - HTTPException with status code 500 if any error occurs during processing.
    """
    try:
        content_type = payload.MimeType

        # Extract text from the document
        if content_type == "image/png":
            payload.FileContent = [payload.FileContent]

        elif content_type == "application/pdf":
            images = convert_pdf_to_image(payload.FileContent)
            payload.FileContent = images # take the list of images

        # Raise an error if the file type is not supported
        else:
            raise HTTPException(status_code=400, detail="Only Image and PDF files are supported.")

        # return text
    
        # Engineer prompt
        prompt = engineer_prompt(payload=payload)

        # return(prompt)

        # Use the LLM to extract relevant fields
        response = generate_response(prompt)

        # # Validate the response
        # validate(response)

        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

