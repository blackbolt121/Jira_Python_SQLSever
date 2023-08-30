from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from os import getenv
from requests import get
from GetProperties import getProperty

def loadUsersByRestAPI():
    users = getOnlyJsonRequestContent(f"{jira_rest_api}users/search")        
    for user in users:
        if getProperty(user,"accountType") == "atlassian":
            data = [getProperty(user, prop) for prop in ["accountId","displayName","emailAddress","active"]]
            cursor.execute("EXEC InsertOrUpdateUserWithoutDate @ACCOUNTID =?, @DISPLAYNAME = ?, @EMAILADDRESS = ?, @ACTIVE = ?", data)
            cursor.commit()

def loadUsersEmailDetails():
    org = getenv("ORG_ID")
    api_key = getenv("API_KEY")
    accountId = "70121:86ff4d8f-1af9-4446-897e-573e1b3459f0"
    headers = {
        "Authorization": f"Bearer {api_key}",
        'Accept': 'application/json'
    }
    r = get(url=f'https://api.atlassian.com/admin/v1/orgs/{org}/directory/users/{accountId}/last-active-dates', headers=headers)
    print(r.content)
    print(r)

def loadUsersLastSeenDetails():
    org = getenv("ORG_ID")
    api_key = getenv("API_KEY")
    accountId = "70121:86ff4d8f-1af9-4446-897e-573e1b3459f0"
    headers = {
        "Authorization": f"Bearer {api_key}",
        'Accept': 'application/json'
    }
    r = get(url=f'https://api.atlassian.com/admin/v1/orgs/{org}/directory/users/{accountId}/last-active-dates', headers=headers)
    print(r.content)
    print(r)