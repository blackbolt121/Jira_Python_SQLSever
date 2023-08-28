from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadRoles():
    try:
        roles = getOnlyJsonRequestContent(f"{jira_rest_api}role")
        for role in roles:
            data = [getProperty(role, prop) for prop in ["id", "name"]]
            cursor.execute("EXEC UpdateInsertIssueType @IssueTypeID = ?, @IssueTypeName = ?;", data)
            cursor.commit()
    except Exception as ex:
        print(ex.args)