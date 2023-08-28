from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_agile_api
from Database.connector import cursor

def loadCategories():
    try:
        
        categories = getOnlyJsonRequestContent(f"{jira_agile_api}projectCategory")
        
        for category in categories:
        
            cursor.execute("EXEC InsertOrUpdateCategory @CategoryID = ?, @CategoryName = ?;", category["id"], category["name"])
        
            cursor.commit()
        
    except Exception as ex:
        print(ex.args)