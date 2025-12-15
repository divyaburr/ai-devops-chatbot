import os
from fastapi import FastAPI
from openai import OpenAI

# Create FastAPI app
app = FastAPI()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Health check (VERY IMPORTANT for Jenkins)
@app.get("/health")
def health():
    return {"status": "ok"}

# Chat endpoint
@app.get("/chat")
def chat(query: str):
    if not query:
        return {"error": "Query is empty"}

    try:
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
