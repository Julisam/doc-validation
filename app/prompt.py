from typing import Dict

def engineer_prompt(payload: Dict = None, text: str = None) -> str:
    """
    Generates a strict prompt for the LLM to classify and extract fields from a document.
    The LLM must return structured JSON only, with rules check and confidence evaluations.
    """
    prompt = (
        "You are a highly accurate document analysis assistant.\n"
        "You are given a scanned document image (encoded in base64). The image may include handwritten or printed text and can contain noise, distortions, or formatting inconsistencies.\n"
        "\n"
        "Your task is to visually inspect the image and extract only the text values that are clearly visible. Do not infer missing information or make assumptions.\n"
        "\n"
        "**Instructions:**\n"
        "- If a value is not clearly visible in the image, return 'Unavailable'.\n"
        "- Match the text exactly as it appears.\n"
        "- Use context from layout, proximity, and labels to identify field values.\n"
        "\n"
        f"The expected document type is: '{payload['DocumentType']}'. Your responsibilities are:\n"
        "1. Identify the actual document type (based on visual clues).\n"
        "2. Extract each of the expected fields below and evaluate their rules.\n"
        "\n"
        "For every field, return:\n"
        "- field_name: The name of the field.\n"
        "- extracted_value: The exact value found, or 'Unavailable'.\n"
        "- confidence_score: A float (0.0–1.0) showing how closely the value matches the expected one.\n"
        "- rules_check: A list of dictionaries like `{ rule_name: 'pass' | 'fail' }`.\n"
        "\n"
        "Then compute overall:\n"
        "- confidence_score: Average of field-level confidence scores.\n"
        "- is_valid: true if average score ≥ 0.7, otherwise false.\n"
        "- validation_message: A short summary of the result.\n"
        "\n"
        "Expected fields and rules:\n"
    )

    for field in payload["ExpectedFields"]:
        prompt += (
            f"- {field['FieldName']} <{field['FieldType']}>: {field['FieldDescription']} "
            f"('expected_value': '{field['FormValue']}')\n"
        )
        if field.get("FieldRules"):
            for rule in field["FieldRules"]:
                prompt += f"    • Rule - '{rule['RuleType']}': {rule['RuleDescription']}\n"

    prompt += (
        "\nReturn ONLY the JSON object using the format below:\n"
        "{\n"
        "  \"document_type\": \"<inferred_document_type>\",\n"
        "  \"extracted_fields\": [\n"
        "    {\n"
        "      \"field_name\": \"<field name>\",\n"
        "      \"extracted_value\": \"<value or 'Unavailable'>\",\n"
        "      \"rules_check\": [\n"
        "        { \"<rule_name>\": \"pass\" },\n"
        "        { \"<rule_name>\": \"fail\" }\n"
        "      ],\n"
        "      \"confidence_score\": <float>\n"
        "    }\n"
        "  ],\n"
        "  \"confidence_score\": <average float>,\n"
        "  \"is_valid\": <true or false>,\n"
        "  \"validation_message\": \"<summary message>\"\n"
        "}\n"
        "\n"
        "Return a valid JSON only with no additional text.\n"
    )


    return prompt