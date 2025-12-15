import openai
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
print("LOADED KEY:", openai.api_key)


app = FastAPI()

@app.get("/chat")
def chat(query: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    return {"answer": response["choices"][0]["message"]["content"]}
