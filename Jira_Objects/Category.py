from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty
def loadCategories():
    try:
        categories = getOnlyJsonRequestContent(f"{jira_rest_api}projectCategory")
        for category in categories:
            data = [ getProperty(category, prop) for prop in ["id", "name"] ]
            cursor.execute("EXEC InsertOrUpdateCategory @CategoryID = ?, @CategoryName = ?;", data)
            cursor.commit()
    except Exception as ex:
        print(ex.args)
    
