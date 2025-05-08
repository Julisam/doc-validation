from fastapi import FastAPI
import ollama

app = FastAPI()

# @app.post("/ask")
# def ask_llm(prompt):
#     response = ollama.chat(
#         model="mistral", 
#         messages=[{'role': 'user', 'content': prompt}]
#     )
#     response = response['message']['content']
#     return {"response": response}


@app.post("/vision")
def ask_llm2(prompt, images=[]):
    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': images
        }]
        )
    # response = response['message']['content']
    return {"resoponse": response}

