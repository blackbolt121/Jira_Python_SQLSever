from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor

def loadCategories():
    try:
        categories = getOnlyJsonRequestContent(f"{jira_rest_api}projectCategory")
        for category in categories:
            """
            try:
                data = [category["id"], category["name"]]
                statement = "INSERT INTO CATEGORY VALUES(?,?);"
                cursor.execute(statement, data)
                cursor.commit()
            except:
                try:
                    data = [category["name"],category["id"]]
                    statement = "UPDATE CATEGORY SET NAME = ? WHERE ID = ?"
                    cursor.execute(statement, data)
                    cursor.commit()
                except Exception as ex:
                    print(ex.args)
            """
            cursor.execute("EXEC InsertOrUpdateCategory @CategoryID = ?, @CategoryName = ?;", category["id"], category["name"])
            cursor.commit()
    except Exception as ex:
        print(ex.args)
    
