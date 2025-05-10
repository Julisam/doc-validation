import requests
import json

url = "http://localhost:8000/extract/" 

with open('sample_payload.json') as json_file:
    data = json.load(json_file)

response = requests.post(url, json=data)

print(f"Response status code: {response.status_code}")
print(f"Response body: \n")
print('----------------------')
# print(json.loads(response.text))      # Puts it in a list, prints with repr()
print(response.json())


# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# key = os.getenv("OPEN_AI_KEY")

# print(key)
