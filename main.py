from Database.connector import cursor
from Jira_Requests.getRequest import getRequest, jira_rest_api


print(getRequest(jira_rest_api+"project").content)

