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

def getRequest(url=""):
    return requests.get(url=url, auth=auth)

def getOnlyJsonRequestContent(url="") -> object:
    request = getRequest(url=url)
    if request.status_code != 200:
        raise Exception("Request failed")
    requestContent = request.content
    return loads(requestContent)