from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadRoles():
    try:
        issue_types = getOnlyJsonRequestContent(f"{jira_rest_api}role")
        for issue_type in issue_types:
            data = [getProperty(role, prop) for prop in ["id", "name"]]
            data.append(getProperty())
            cursor.execute("EXEC UpdateInsertIssueType @IssueTypeID = ?, @IssueTypeName = ?, @IssueTypeCategory = ?;", data)
            cursor.commit()
    except Exception as ex:
        print(ex.args)