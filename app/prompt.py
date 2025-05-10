from typing import Dict

def engineer_prompt(payload: Dict = None, text: str = None) -> str:
    """
    Generates a strict prompt for the LLM to classify and extract fields from a document.
    The LLM must return structured JSON only, with rules check and confidence evaluations.
    """

    prompt = (
        "You are a highly accurate document analysis assistant.\n"
        "You are given OCR text from a scanned document. The OCR text may contain typos or formatting issues.\n"
        "Your job is to strictly extract the requested information.\n"
        "\n"
        "Do not assume or infer field values. If any value is not clearly found in the text, use 'Unavailable'.\n"
        "\n"
        
        "------START OF DOCUMENT TEXT------\n"
        f"{text}\n"
        "------END OF DOCUMENT TEXT------\n\n"

        f"Determine if the document type is: '{payload.DocumentType}' and extract fields from the text.\n"
        "For each expected field, return:\n"
        "- field_name: The name of the field.\n"
        "- extracted_value: The exact value found in the OCR text, or 'Unavailable'.\n"
        "- confidence_score: A float between 0 and 1 representing similarity between extracted value (from OCR text) and the expected value. A score of zeros means that the extracted value is totally different from the expected value and vice versa\n"
        "- rules_check: List of `{ rule_name: \"pass/fail\" }` (empty list if no rules).\n"
        "\n"
        "Then compute:\n"
        "- confidence_score: The average of all field-level confidence scores.\n"
        "- is_valid: true if overall confidence_score >= 0.7, otherwise false.\n"
        "- validation_message: a short message summarizing the result.\n"
        "\n"
        "Expected fields and their rules:\n"
    )
    # return prompt

    for field in payload.ExpectedFields:
        prompt += f"- {field.FieldName} <{field.FieldType}>: {field.FieldDescription} ('expected_value':'{field.FormValue}')\n"
        if field.FieldRules:
            for field_rule in field.FieldRules:
                rule_type = field_rule.RuleType
                desc = field_rule.RuleDescription
                # for rule_type, desc in rule.items():
                    # if rule_type != "match_type":
                prompt += f"    • Rule - '{rule_type}': {desc}\n"
    # return prompt
    prompt += (
        "\nReturn ONLY the JSON object in the exact format below:\n"
        "{\n"
        "  \"document_type\": \"<inferred_document_type>\",\n"
        "  \"extracted_fields\": [\n"
        "    {\n"
        "      \"field_name\": \"<field name e.g. FullName>\",\n"
        "      \"extracted_value\": \"<extracted value or 'Unavailable'>\",\n"
        "      \"rules_check\": [\n"
        "        { \"<rule_name>\": <pass/fail> },\n"
        "        ...\n"
        "      ],\n"
        "      \"confidence_score\": <float between 0 and 1>\n"
        "    }\n"
        "  ],\n"
        "  \"confidence_score\": <average score>,\n"
        "  \"is_valid\": <true or false>,\n"
        "  \"validation_message\": \"<summary message>\"\n"
        "}\n"
        "\n"
        "Return JSON only and no other text.\n"
        "\n"

    )

    return prompt