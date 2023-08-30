from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadProjects():
    flag = True
    startAt=0
    while flag == True:
        try:
            projectsRequest = getOnlyJsonRequestContent(f"{jira_rest_api}project/search?startAt={startAt}")
            projects = projectsRequest["values"]
            for project in projects:
                data = [getProperty(project, prop) for prop in ["id","name","key","archived","style","isPrivate"]]
                data.insert(1,getProperty(getProperty(project, "projectCategory"), "id"))
                print(data)
                cursor.execute("EXEC InsertOrUpdateProject @ProjectID = ?, @ProjectCategory = ?, @ProjectName = ?, @ProjectKey = ?, @Archived = ?, @TYPE = ?, @ISPRIVATE = ?;", data)
                cursor.commit()
            if projectsRequest["isLast"] == True:
                flag = False
            startAt+=50
        except Exception as ex:
            print(ex.args)
            break
