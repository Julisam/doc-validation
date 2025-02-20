# Document Extraction and Classification API

Document Extraction and Classification API is a FastAPI-based application that processes uploaded documents by extracting text using `pytesseract` and then use Large Language Model (LLM) to extract key fields from the document. `main.py` serves as the entry point for the FastAPI application that processes document uploads. 

## Features

- **File Upload:** Accepts PDF and PNG files via an API endpoint.
    - Endpoint: /extract/
    - HTTP Method: POST
	- File Types Supported: Images and PDF

- **Text Extraction:** 
  - Extracts text from PDFs and images using `pytesseract`.

- **LLM-Based Classification:** 
  - Will use a LLaMA-based model to classify documents.
  - Will extract relevant fields (e.g., Name, Date of Birth, Place of Birth) if the document is a birth certificate.

- **Error Handling:** Returns appropriate HTTP error responses for unsupported file types or processing errors.
