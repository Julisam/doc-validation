from typing import Dict
def engineer_prompt(payload: Dict = None, text: str = None) -> str:
    """
    Generates a prompt for the LLM to classify and extract fields from a document.
    
    Args:
        payload (Dict): The request payload containing document details. 
    
    Returns:
        str: The generated prompt for the LLM.
    """
    prompt = (
        "You are an expert document assistant. "
        "The document is a scanned image of a document. "
        "The text is the result of OCR processing. "
        "The text may contain errors, and the formatting may not be perfect. "
        "\nYour task is to analyze the provided OCR’ed text, determine if it is a "
        f"{payload.DocumentType} and extract the fields from the text. "
        "\nIf it is, extract the following fields: ")
    
    for field in payload.ExpectedFields:
        prompt += f"\n  - {field.FieldName} <{field.FieldType}> --> {field.FieldDescription}"
    
    prompt += (
        "\n\n"
        "Return a JSON object with two keys: 'document_type' and 'extracted_fields'. "
        f"\nIf the document is a {payload.DocumentType}, "
        f"set 'document_type' to '{payload.DocumentType}' and include the "
        "extracted fields (use 'Unavailable' for field that is not found). "
        f"\nIf it is not a {payload.DocumentType}, set 'document_type' to 'unknown' and 'extracted_fields' as an empty object.\n\n"
        "Here is the Document text:\n"
        f"------START OF DOCUMENT TEXT------\n\n"
        f"{text}\n\n"

        "------END OF DOCUMENT TEXT------\n\n"

        "Return only a valid JSON with no other text. The JSON should be formatted as follows:\n"
        "```json\n"
        "{\n"
        "    \"document_type\": \"<extracted_value>\",\n"
        "    \"extracted_fields\": {\n"
    )
    for field in payload.ExpectedFields:
        prompt += f"        \"{field.FieldName}\": \"<extracted_value>\",\n"
    
    prompt += (
        "    }\n"
        "}\n"
        "```"
    )
    return prompt