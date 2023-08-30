from Jira_Requests.getRequest import getOnlyJsonRequestContent, jira_rest_api
from Database.connector import cursor
from GetProperties import getProperty

def loadUserMembers():
    users = cursor.execute("SELECT accountId FROM USERS").fetchall()
    cursor.execute("DELETE FROM USER_MEMBERS")
    cursor.commit()
    for user in users:
        accountId = user[0]
        userGroup = getOnlyJsonRequestContent(f'{jira_rest_api}/user?accountId={accountId}&expand=groups')
        array_groups = userGroup["groups"]
        if getProperty(array_groups,"size") in [None, 0]:
            continue
        for object_group in getProperty(array_groups,"items"):
            groupId = getProperty(object_group, "groupId")
            cursor.execute("EXEC UpdateInsertUserMembers @AccountID = ?, @GroupID = ?", [accountId, groupId])
            cursor.commit()