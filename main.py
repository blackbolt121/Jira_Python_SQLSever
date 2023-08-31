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
from Database.GetTableContentInCsv import GenerateCsvFromTable, GenerateCsvFromQuery
"""
loadCategories()
loadProjects()
loadStatus()
loadBoards()
loadRoles()
loadStatusCategory()
loadIssueType()
loadGroups()
loadRoles()
loadUsersByRestAPI()
loadUserMembers()
loadUsersEmailDetails()
"""



GenerateCsvFromQuery("SELECT p.name AS 'Project Name', COUNT(b.name) AS 'Board Name' FROM PROJECT p, BOARD b WHERE p.id = b.projectID GROUP BY p.name")