# devops_faq.py

FAQS = {
    "what is jenkins": "Jenkins is a CI/CD automation tool used to build, test, and deploy applications.",
    "what is ci cd": "CI/CD stands for Continuous Integration and Continuous Deployment.",
    "what is docker": "Docker is a containerization platform."
}

def get_faq_answer(query: str):
    for q, ans in FAQS.items():
        if q in query.lower():
            return ans
    return None
