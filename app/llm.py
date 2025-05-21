import ollama
import json
import requests

def generate_response(prompt, images=None):
    """
    Generates a response from the LLM using the Ollama API.

    Args:
        prompt (str): The input prompt for the LLM.

    Returns:
        str: The generated response from the LLM.
    """
    # Call the Ollama API to generate a response

    # Note: Ensure that the Ollama API is running and accessible
    v_payload = {
        "model": "llama3.2-vision:11b",
        "prompt": prompt,
        "images": images,
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=v_payload)
    response = response.json()["response"]

    # try :
    #     # Attempt to parse the response as JSON
    #     response = json.loads(response)
    # except json.JSONDecodeError:
    #     # If parsing fails, return the raw response
    #     return {
    #         "document_type": "unknown",
    #         "extracted_fields": {}
    #     }

    return response




# # CHATgpt
# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# openai_key = os.getenv("OPENAI_API_KEY")

# if openai_key is None:
#     raise ValueError("OPENAI_API_KEY environment variable not set.")

# client = OpenAI(
#     api_key=openai_key,
# )


# def generate_response(prompt):
#     # Use the API
#     response = client.responses.create(
#         model="gpt-4o",
#         instructions="",
#         input=prompt,
#     )

#     return (response.output_text)