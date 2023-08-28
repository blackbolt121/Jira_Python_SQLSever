from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadStatus():
    try:
        statuses = getOnlyJsonRequestContent(f"{jira_rest_api}status")
        for status in statuses:
            data = [getProperty(status, prop) for prop in ["id", "name"]]
            cursor.execute("EXEC UpdateInsertStatus @StatusID = ?, @StatusName = ?;", data)
            cursor.commit()
    except Exception as ex:
        print(ex.args)
    