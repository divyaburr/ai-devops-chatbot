# jenkins_client.py

def analyze_jenkins_issue(query: str):
    if "build failed" in query.lower():
        return "Possible reasons: test failures, dependency issues, or wrong Jenkinsfile."
    return None
