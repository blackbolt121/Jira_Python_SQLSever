from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadIssueType():
    try:
        issue_types = getOnlyJsonRequestContent(f"{jira_rest_api}issuetype")
        for issue_type in issue_types:
            data = [getProperty(issue_type, prop) for prop in ["id", "name", "hierarchyLevel"]]
            cursor.execute("EXEC UpdateInsertIssueType @IssueTypeID = ?,@IssueTypeName = ?, @IssueHierarchy = ?;", data)
            cursor.commit()
    except Exception as ex:
        print(ex.args)