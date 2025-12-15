from fastapi import FastAPI
from dotenv import load_dotenv
import os

from devops_faq import get_faq_answer
from jenkins_client import analyze_jenkins_issue

load_dotenv()

app = FastAPI()

@app.get("/chat")
def chat(query: str):

    # 1️⃣ First try Jenkins logic
    jenkins_answer = analyze_jenkins_issue(query)
    if jenkins_answer:
        return {"source": "jenkins", "answer": jenkins_answer}

    # 2️⃣ Then try DevOps FAQ
    faq_answer = get_faq_answer(query)
    if faq_answer:
        return {"source": "faq", "answer": faq_answer}

    # 3️⃣ AI fallback (mock for now)
    return {
        "source": "ai-mock",
        "answer": f"AI analysis pending for query: {query}"
    }
