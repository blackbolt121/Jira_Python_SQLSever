from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_agile_api
from Database.connector import cursor
from GetProperties import getProperty

def loadBoards():
    try:
        startAt=0
        flag=True
        while flag == True:
            boardRequest = getOnlyJsonRequestContent(f"{jira_agile_api}board?startAt={startAt}")
            boards = getProperty(boardRequest, "values")
            for board in boards:
                data = [getProperty(board, prop) for prop in ["id", "name", "type"]]
                data.insert(1,getProperty(getProperty(board, "location"), "projectId"))
                print(data)
                cursor.execute("EXEC UpdateInsertBoard @BoardID = ?, @ProjectID = ?, @BoardName = ?, @BoardType = ?;",data)
                cursor.commit()
            if getProperty(board, "isLast") in [True, None]:
                break
            startAt+=50
    except Exception as ex:
        print(ex.args)