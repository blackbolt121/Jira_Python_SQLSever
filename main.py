from Jira_Objects.Board import loadBoards
from Jira_Objects.Project import loadProjects
from Jira_Objects.Status import loadStatus
from Jira_Objects.Project_Role import loadRoles
from Jira_Objects.Category import loadCategories
from Jira_Objects.Status_Category import loadStatusCategory
from Jira_Objects.Issue_Type import loadIssueType
from Jira_Objects.Group import loadGroups
from Jira_Objects.Project_Role import loadRoles
from Jira_Objects.User import loadUsersByRestAPI, loadUsersEmailDetails
from Jira_Objects.User_Members import loadUserMembers
from Jira_Objects.Story import publishMultipleScrumReport
from Database.GetTableContentInCsv import GenerateCsvFromTable, GenerateCsvFromQuery
from sys import argv

commands = {
    "categories": loadCategories,
    "projects" : loadProjects,
    "status" : loadStatus,
    "boards" : loadBoards,
    "roles" : loadRoles,
    "statusCategory" : loadStatusCategory,
    "issueType" : loadIssueType,
    "groups" : loadGroups,
    "Users" : loadUsersByRestAPI,
    "UserMembers" : loadUserMembers,
    "scrum" : publishMultipleScrumReport
}

try:
    if len(argv) > 1:
        if argv[1] == "all":
            for key in commands.keys():
                if key != "scrum":
                    commands[key]()
        else:
            commands[argv[1]]()
except:
    print("Command not valid...")
