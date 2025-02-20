
# Sample 
def classify_and_extract_birth_certificate(text: str) -> dict:
    """
    Sends a prompt to the LLM to classify and extract fields from a document.
    Expected output: JSON with keys 'document_type' and 'fields'.
    """

    prompt = (
        "You are a document analysis assistant. "
        "Analyze the following text extracted from a document and determine if it is a birth certificate. "
        "If it is, extract the following fields: Name, Date of Birth, Place of Birth. "
        "Return a JSON object with two keys: 'document_type' and 'fields'. "
        "If the document is a birth certificate, set 'document_type' to 'birth_certificate' and include the extracted fields (use 'Unavailable' for field that is not found). "
        "If it is not a birth certificate, set 'document_type' to 'unknown' and 'fields' as an empty object.\n\n"
        "Document text:\n"
        f"{text}\n\n"
        "Return only valid JSON."
    )
    
    # response = llama_pipeline(prompt, max_length=MAX_LENGTH, do_sample=False)
    # generated_text = response[0]["generated_text"]

    # parsed_output = extract_json_from_text(generated_text)
    # if not parsed_output:
    #     raise ValueError("Failed to extract JSON from LLM output.")
    
    return {
        "document_type": "birth_certificate",
        "fields": {
            "Name": "Sample Name",
            "Date of Birth": "01/01/2000",
            "Place of Birth": "Sample City, Sample Country"
        }
    }