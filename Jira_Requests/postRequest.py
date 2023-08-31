import requests
from requests.auth import HTTPBasicAuth
from os import getenv
from json import loads
from dotenv import load_dotenv

load_dotenv()

email = getenv("EMAIL")
token = getenv("TOKEN")

auth = HTTPBasicAuth(username=email,password=token)
jira_rest_api = getenv("JIRA_API")
jira_agile_api = getenv("JIRA_AGILE_API")

def postRequest(url="", payload = None):
    if payload != None:
        return requests.post(url=url, auth=auth, json=payload)
    else:
        return requests.post(url=url, auth=auth)

def postAttachment(url="", filename="file.txt", filepath="file.txt"):
    headers = {
        "Accept": "application/json",
        "X-Atlassian-Token": "no-check"
    }
    response = requests.post(
        url,
        headers = headers,
        auth = auth,
        files = {
            "file": (filename, open(filepath,"rb"), "application-type")
        }
    )
    print(response.content)

def postOnlyJsonRequestContent(url="", payload=None) -> object:
    print("here")
    request = postRequest(url=url, payload=payload)
    print(request.status_code)
    print(request.content)
    if request.status_code < 200 or request.status_code >= 300:
        raise Exception("Request failed")
    requestContent = request.content
    return loads(requestContent)