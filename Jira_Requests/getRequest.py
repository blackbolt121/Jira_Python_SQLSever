import requests
from requests.auth import HTTPBasicAuth
import os

email = os.getenv("EMAIL")
token = os.getenv("TOKEN")
auth = HTTPBasicAuth(username=email,password=token)
jira_rest_api = os.getenv("JIRA_API")
def getRequest(url=""):
    return requests.get(url=url, auth=auth)