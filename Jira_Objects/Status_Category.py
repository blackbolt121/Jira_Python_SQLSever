from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadStatusCategory():
    try:
        statuses = getOnlyJsonRequestContent(f"{jira_rest_api}statuscategory")
        for status in statuses:
            data = [getProperty(status, prop) for prop in ["id", "name","key"]]
            cursor.execute("EXEC UpdateInsertStatusCategory @ID = ?, @NAME = ?, @KEY = ?;", data)
            cursor.commit()
    except Exception as ex:
        print(ex.args)