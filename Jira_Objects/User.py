from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadUsersByRestAPI():
    users = getOnlyJsonRequestContent(f"{jira_rest_api}users/search")        
    for user in users:
        if getProperty(user,"accountType") == "atlassian":
            data = [getProperty(user, prop) for prop in ["accountId","displayName","emailAddress","active"]]
            cursor.execute("EXEC InsertOrUpdateUserWithoutDate @ACCOUNTID =?, @DISPLAYNAME = ?, @EMAILADDRESS = ?, @ACTIVE = ?", data)
            cursor.commit()