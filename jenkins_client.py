import requests
import os

JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USER = os.getenv("JENKINS_USER")
JENKINS_TOKEN = os.getenv("JENKINS_TOKEN")

def get_job_status(job_name):
    url = f"{JENKINS_URL}/{job_name}/lastBuild/api/json"
    res = requests.get(url, auth=(JENKINS_USER, JENKINS_TOKEN))
    if res.status_code != 200:
        return "Unable to fetch Jenkins data"
    data = res.json()
    return f"Job: {job_name}\nStatus: {data['result']}\nURL: {data['url']}"
