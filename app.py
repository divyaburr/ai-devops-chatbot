import os
from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()

# Initialize client lazily to avoid startup crash
def get_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/chat")
def chat(query: str):
    if not query:
        return {"error": "Query is empty"}

    try:
        client = get_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI DevOps assistant."},
                {"role": "user", "content": query}
            ]
        )
        return {
            "query": query,
            "response": response.choices[0].message.content
        }
    except Exception as e:
        return {"error": str(e)}
