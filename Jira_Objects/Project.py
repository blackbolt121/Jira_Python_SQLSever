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
                projectKey = getProperty(project, "key")
                projectName = getProperty(project, "name")
                projectId = getProperty(project, "id")
                categoryId = getProperty(getProperty(project, "projectCategory"), "id")
                archived = getProperty(project, "archived")
                if archived == None:
                    archived = False
                style = getProperty(project, "style")
                isPrivate = getProperty(project, "isPrivate")
                data = [projectId, categoryId, projectName, projectKey, archived, style, isPrivate]
                cursor.execute("EXEC UpdateInsertProject @ProjectID = ?, @CategoryID = ?, @ProjectName = ?, @ProjectKey = ?, @Archived = ?, @STYLE = ?, @ISPRIVATE = ?;", data)
                cursor.commit()
            if projectsRequest["isLast"] == True:
                flag = False
            startAt+=50
        except Exception as ex:
            print(ex.args)
            break
