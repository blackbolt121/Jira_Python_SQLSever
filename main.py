from Jira_Objects.Board import loadBoards
from Jira_Objects.Project import loadProjects
from Jira_Objects.Status import loadStatus
from Jira_Objects.Project_Role import loadRoles
from Jira_Objects.Category import loadCategories
from Jira_Objects.Status_Category import loadStatusCategory
from Jira_Objects.Issue_Type import loadIssueType
from Jira_Objects.Group import loadGroups
from Jira_Objects.Project_Role import loadRoles
from Jira_Objects.User import loadUsersByRestAPI

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