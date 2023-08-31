from Jira_Requests.postRequest import postOnlyJsonRequestContent, postAttachment, jira_rest_api
from Database.GetTableContentInCsv import GenerateCsvFromQuery
from GetProperties import getProperty



def publishMultipleScrumReport():
    issue_payload = {
        "fields": {
            "project": {
                "key": "PT1"  # Replace with your project key
            },
            "summary": "Create a REST API Story",
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                    "type": "paragraph",
                    "content": [
                        {
                        "type": "text",
                        "text": "A nice summary"
                        }
                    ]
                    }
                ]
            },
            "issuetype": {
                "name": "Story"
            }
        }
    }
    try:
        content = postOnlyJsonRequestContent(url=f"{jira_rest_api}/issue", payload=issue_payload)
        id = getProperty(content,"id")
        GenerateCsvFromQuery(query="SELECT p.name as 'Project Name', count(b.id) '# of Scrum Boards' FROM PROJECT p, BOARD b WHERE p.id = b.projectId AND b.type = 'scrum' GROUP BY p.name HAVING count(p.id) > 1")
        postAttachment(url=f"{jira_rest_api}/issue/{id}/attachments", filename="report.csv", filepath="./file.txt")
    except Exception as ex:
        print(ex.args)
    print(content)