import ollama
import json

def generate_response(prompt):
    """
    Generates a response from the LLM using the Ollama API.

    Args:
        prompt (str): The input prompt for the LLM.

    Returns:
        str: The generated response from the LLM.
    """
    # Call the Ollama API to generate a response

    # Note: Ensure that the Ollama API is running and accessible
    response = ollama.chat(
        model="llama3.2", 
        messages=[{"role": "user", "content": prompt}]
        )

    response = response['message']['content']

    try :
        # Attempt to parse the response as JSON
        response = json.loads(response)
    except json.JSONDecodeError:
        # If parsing fails, return the raw response
        return {
            "document_type": "unknown",
            "extracted_fields": {}
        }

    return response
