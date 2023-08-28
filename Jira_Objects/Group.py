from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor


def loadGroups():
    flag = True
    startAt=0
    while flag == True:
        try:
            groupsRequest = getOnlyJsonRequestContent(f"{jira_rest_api}group/bulk?startAt={startAt}")
            groups = groupsRequest["values"]
            for group in groups:
                cursor.execute("EXEC UpdateInsertGroup @GroupID = ?, @GroupName = ?;", group["groupId"], group["name"])
                cursor.commit()
            if groupsRequest["isLast"] == True:
                flag = False
            startAt+=50
        except Exception as ex:
            print(ex.args)
            break
