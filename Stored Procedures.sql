USE JIRA
GO
CREATE PROCEDURE InsertOrUpdateCategory
    @CategoryID INT,
    @CategoryName VARCHAR(255)
AS
BEGIN
    MERGE INTO Category AS target
    USING (SELECT @CategoryID AS CategoryID, @CategoryName AS CategoryName) AS source
    ON (target.ID = source.CategoryID)
    WHEN MATCHED THEN
        UPDATE SET target.Name = source.CategoryName
    WHEN NOT MATCHED THEN
        INSERT (ID, Name)
        VALUES (source.CategoryID, source.CategoryName);
END;
GO
CREATE PROCEDURE InsertOrUpdateProject
    @ProjectID INT,
    @ProjectName VARCHAR(255),
	@ProjectCategory INT,
	@ProjectKey VARCHAR(50),
	@Archived BIT,
	@TYPE AS VARCHAR(50),
	@ISPRIVATE AS BIT
AS
BEGIN
    MERGE INTO PROJECT AS target
    USING (SELECT @ProjectID AS ProjectID, 
				  @ProjectCategory AS CategoryID, 
				  @ProjectName AS ProjectName, 
				  @ProjectKey as ProjectKey, 
				  @Archived AS Archived,
				  @TYPE AS [TYPE],
				  @ISPRIVATE AS [ISPRIVATE]
				  ) AS source
    ON (target.ID = source.ProjectID)
    WHEN MATCHED THEN
        UPDATE SET target.[NAME] = source.ProjectName, 
				   target.[CATEGORY] = source.CategoryID, 
				   target.[KEY] = source.ProjectKey, 
				   target.[ARCHIVED] = source.Archived,
				   target.[TYPE] = source.[TYPE],
				   target.[ISPRIVATE] = source.[ISPRIVATE]
    WHEN NOT MATCHED THEN
        INSERT (ID, 
				[NAME], 
				[CATEGORY], 
				[KEY], 
				[ARCHIVED], 
				[TYPE], 
				[ISPRIVATE])
        VALUES (source.CategoryID, 
				source.ProjectName, 
				source.CategoryID, 
				source.ProjectKey, 
				source.Archived, 
				source.[TYPE], 
				source.[ISPRIVATE]);
END;
GO
CREATE PROCEDURE InsertOrUpdateProjectRole
    @ID INT,
    @Name VARCHAR(255)
AS
BEGIN
    MERGE INTO PROJECT_ROLE AS target
    USING (SELECT @ID AS ID, @Name AS [NAME]) AS source
    ON (target.ID = source.ID)
    WHEN MATCHED THEN
        UPDATE SET target.Name = source.[NAME]
    WHEN NOT MATCHED THEN
        INSERT (ID, Name)
        VALUES (source.ID, source.[NAME]);
END;
GO
CREATE PROCEDURE InsertOrUpdateProjectSecurityGroup
    @PROJECTID INT,
    @GROUPID VARCHAR(255),
	@ROLEID VARCHAR
AS
BEGIN
    MERGE INTO PROJECT_SECURITY_GROUP AS target
    USING (SELECT @PROJECTID AS PROJECTID, @GROUPID AS GROUPID, @ROLEID AS ROLEID) AS source
    ON (target.PROJECTID = source.PROJECTID AND target.GROUPID = source.GROUPID AND target.ROLEID = source.ROLEID)
    WHEN NOT MATCHED THEN
        INSERT (PROJECTID, GROUPID, ROLEID)
        VALUES (source.PROJECTID, source.GROUPID, source.ROLEID);
END;
GO
CREATE PROCEDURE InsertOrUpdateUserProjectRole
    @PROJECTID INT,
    @USERID VARCHAR(255),
	@ROLEID VARCHAR
AS
BEGIN
    MERGE INTO USER_PROJECT_ROLE AS target
    USING (SELECT @PROJECTID AS PROJECTID, @USERID AS USERID, @ROLEID AS ROLEID) AS source
    ON (target.PROJECTID = source.PROJECTID AND target.USERID = source.USERID AND target.ROLEID = source.ROLEID)
    WHEN NOT MATCHED THEN
        INSERT (PROJECTID, USERID, ROLEID)
        VALUES (source.PROJECTID, source.USERID, source.ROLEID);
END;
GO
CREATE PROCEDURE InsertOrUpdateUser
    @ACCOUNTID VARCHAR(128),
	@DISPLAYNAME VARCHAR(255),
	@EMAILADDRESS VARCHAR(255),
    @ACTIVE VARCHAR(25),
	@LASTSEEN DATETIME,
	@ADDEDTOORG DATETIME
AS
BEGIN
    MERGE INTO USERS AS target
    USING (SELECT @ACCOUNTID AS ACCOUNTID, @DISPLAYNAME AS DISPLAYNAME, @EMAILADDRESS AS EMAILADDRESS, @ACTIVE AS ACTIVE, @LASTSEEN AS LASTSEEN, @ADDEDTOORG AS ADDEDTOORG) AS source
    ON (target.ACCOUNTID = source.ACCOUNTID)
	WHEN MATCHED THEN
		UPDATE SET DISPLAYNAME = source.DISPLAYNAME, ACTIVE = source.ACTIVE, LASTSEEN = source.LASTSEEN, ADDEDTOORG = source.ADDEDTOORG, EMAILADDRESS = source.EMAILADDRESS
    WHEN NOT MATCHED THEN
        INSERT (ACCOUNTID, DISPLAYNAME, EMAILADDRESS, ACTIVE, LASTSEEN, ADDEDTOORG)
        VALUES (source.ACCOUNTID, source.DISPLAYNAME, source.EMAILADDRESS, source.ACTIVE, source.LASTSEEN, source.ADDEDTOORG);
END;
GO
CREATE PROCEDURE InsertOrUpdateUserWithOutDate
    @ACCOUNTID VARCHAR(128),
	@DISPLAYNAME VARCHAR(255),
	@EMAILADDRESS VARCHAR(255),
    @ACTIVE VARCHAR(25)
AS
BEGIN
    MERGE INTO USERS AS target
    USING (SELECT @ACCOUNTID AS ACCOUNTID, @DISPLAYNAME AS DISPLAYNAME, @EMAILADDRESS AS EMAILADDRESS, @ACTIVE AS ACTIVE) AS source
    ON (target.ACCOUNTID = source.ACCOUNTID)
	WHEN MATCHED THEN
		UPDATE SET DISPLAYNAME = source.DISPLAYNAME, ACTIVE = source.ACTIVE, EMAILADDRESS = source.EMAILADDRESS
    WHEN NOT MATCHED THEN
        INSERT (ACCOUNTID, DISPLAYNAME, EMAILADDRESS, ACTIVE)
        VALUES (source.ACCOUNTID, source.DISPLAYNAME, source.EMAILADDRESS, source.ACTIVE);
END;
GO
CREATE PROCEDURE UpdateInsertProject
    @ProjectID INT,
    @CategoryID INT,
    @ProjectName VARCHAR(128),
    @ProjectKey VARCHAR(50),
    @Archived BIT,
    @TYPE VARCHAR(50),
    @ISPRIVATE BIT
AS
BEGIN
    MERGE INTO [PROJECT] AS target
    USING (
        SELECT
            @ProjectID AS ProjectID,
            @CategoryID AS CategoryID,
            @ProjectName AS ProjectName,
            @ProjectKey AS ProjectKey,
            @Archived AS Archived,
            @TYPE AS [TYPE],
            @ISPRIVATE AS [ISPRIVATE]
    ) AS source
    ON (target.ID = source.ProjectID)
    WHEN MATCHED THEN
        UPDATE SET
            [CATEGORY] = source.CategoryID,
            [NAME] = source.ProjectName,
            [KEY] = source.ProjectKey,
            ARCHIVED = source.Archived,
            [TYPE] = source.[TYPE],
            ISPRIVATE = source.[ISPRIVATE]
    WHEN NOT MATCHED THEN
        INSERT (
            ID,
            [CATEGORY],
            [NAME],
            [KEY],
            ARCHIVED,
            [TYPE],
            ISPRIVATE
        )
        VALUES (
            source.ProjectID,
            source.CategoryID,
            source.ProjectName,
            source.ProjectKey,
            source.Archived,
            source.[TYPE],
            source.[ISPRIVATE]
        );
END;
GO
CREATE PROCEDURE UpdateInsertSprint
    @SprintID INT,
    @BoardID INT,
    @Status VARCHAR(128),
    @StartDate DATETIME,
    @EndDate DATETIME,
    @CompletedDate DATETIME
AS
BEGIN
    MERGE INTO [SPRINT] AS target
    USING (
        SELECT
            @SprintID AS SprintID,
            @BoardID AS BoardID,
            @Status AS Status,
            @StartDate AS StartDate,
            @EndDate AS EndDate,
            @CompletedDate AS CompletedDate
    ) AS source
    ON (target.ID = source.SprintID)
    WHEN MATCHED THEN
        UPDATE SET
            BOARDID = source.BoardID,
            [STATUS] = source.Status,
            STARTDATE = source.StartDate,
            ENDDATE = source.EndDate,
            COMPLETEDDATE = source.CompletedDate
    WHEN NOT MATCHED THEN
        INSERT (
            ID,
            BOARDID,
            [STATUS],
            STARTDATE,
            ENDDATE,
            COMPLETEDDATE
        )
        VALUES (
            source.SprintID,
            source.BoardID,
            source.Status,
            source.StartDate,
            source.EndDate,
            source.CompletedDate
        );
END;
GO
CREATE PROCEDURE UpdateInsertSprintIssues
    @StoryID INT,
    @SprintID INT
AS
BEGIN
    MERGE INTO [SPRINT_ISSUES] AS target
    USING (
        SELECT
            @StoryID AS StoryID,
            @SprintID AS SprintID
    ) AS source
    ON (target.STORY = source.StoryID AND target.SPRINT = source.SprintID)
    WHEN NOT MATCHED THEN
        INSERT (
            STORY,
            SPRINT
        )
        VALUES (
            source.StoryID,
            source.SprintID
        );
END;
GO
CREATE PROCEDURE UpdateInsertStory
    @StoryID INT,
    @StoryPoints INT
AS
BEGIN
    MERGE INTO [STORY] AS target
    USING (
        SELECT
            @StoryID AS StoryID,
            @StoryPoints AS StoryPoints
    ) AS source
    ON (target.ID = source.StoryID)
    WHEN MATCHED THEN
        UPDATE SET
            STORY_POINTS = source.StoryPoints
    WHEN NOT MATCHED THEN
        INSERT (
            ID,
            STORY_POINTS
        )
        VALUES (
            source.StoryID,
            source.StoryPoints
        );
END;
GO
CREATE PROCEDURE UpdateInsertIssues
    @IssueID INT,
    @IssueKey VARCHAR(50),
    @ProjectID INT,
    @IssueType INT,
    @StatusID INT,
    @Created DATETIME,
    @Updated DATETIME,
    @Assignee VARCHAR(128),
    @Reporter VARCHAR(128),
    @Parent INT
AS
BEGIN
    MERGE INTO [ISSUES] AS target
    USING (
        SELECT
            @IssueID AS IssueID,
            @IssueKey AS IssueKey,
            @ProjectID AS ProjectID,
            @IssueType AS IssueType,
            @StatusID AS StatusID,
            @Created AS Created,
            @Updated AS Updated,
            @Assignee AS Assignee,
            @Reporter AS Reporter,
            @Parent AS Parent
    ) AS source
    ON (target.ID = source.IssueID)
    WHEN MATCHED THEN
        UPDATE SET
            [KEY] = source.IssueKey,
            PROJECT = source.ProjectID,
            [TYPE] = source.IssueType,
            [STATUS] = source.StatusID,
            [CREATED] = source.Created,
            [UPDATED] = source.Updated,
            [ASIGNEE] = source.Assignee,
            [REPORTER] = source.Reporter,
            [PARENT] = source.Parent
    WHEN NOT MATCHED THEN
        INSERT (
            ID,
            [KEY],
            PROJECT,
            [TYPE],
            [STATUS],
            [CREATED],
            [UPDATED],
            [ASIGNEE],
            [REPORTER],
            [PARENT]
        )
        VALUES (
            source.IssueID,
            source.IssueKey,
            source.ProjectID,
            source.IssueType,
            source.StatusID,
            source.Created,
            source.Updated,
            source.Assignee,
            source.Reporter,
            source.Parent
        );
END;
GO
CREATE PROCEDURE UpdateInsertUserMembers
    @AccountID VARCHAR(128),
    @GroupID VARCHAR(128)
AS
BEGIN
    MERGE INTO [USER_MEMBERS] AS target
    USING (
        SELECT
            @AccountID AS AccountID,
            @GroupID AS GroupID
    ) AS source
    ON (target.ACCOUNTID = source.AccountID AND target.GROUPID = source.GroupID)
    WHEN NOT MATCHED THEN
        INSERT (
            ACCOUNTID,
            GROUPID
        )
        VALUES (
            source.AccountID,
            source.GroupID
        );
END;
GO
CREATE PROCEDURE UpdateInsertIssueType
    @IssueTypeID INT,
    @IssueTypeName VARCHAR(128),
	@IssueHierarchy INT
AS
BEGIN
    MERGE INTO [ISSUE_TYPE] AS target
    USING (
        SELECT
            @IssueTypeID AS IssueTypeID,
            @IssueTypeName AS IssueTypeName,
            @IssueHierarchy AS IssueHierarchy
    ) AS source
    ON (target.ID = source.IssueTypeID)
    WHEN MATCHED THEN
        UPDATE SET
            [NAME] = source.IssueTypeName,
			[HIERARCHY_LEVEL] = source.IssueHierarchy
    WHEN NOT MATCHED THEN
        INSERT (
            [ID],
            [NAME],
            [HIERARCHY_LEVEL]
        )
        VALUES (
            source.IssueTypeID,
            source.IssueTypeName,
            source.IssueHierarchy
        );
END;
GO
CREATE PROCEDURE UpdateInsertBoard
    @BoardID INT,
    @ProjectID INT,
    @BoardName VARCHAR(128),
    @BoardType VARCHAR(50)
AS
BEGIN
    MERGE INTO [BOARD] AS target
    USING (
        SELECT
            @BoardID AS BoardID,
            @ProjectID AS ProjectID,
            @BoardName AS BoardName,
            @BoardType AS BoardType
    ) AS source
    ON (target.ID = source.BoardID)
    WHEN MATCHED THEN
        UPDATE SET
            PROJECTID = source.ProjectID,
            [NAME] = source.BoardName,
            [TYPE] = source.BoardType
    WHEN NOT MATCHED THEN
        INSERT (
            ID,
            PROJECTID,
            [NAME],
            [TYPE]
        )
        VALUES (
            source.BoardID,
            source.ProjectID,
            source.BoardName,
            source.BoardType
        );
END;
GO
CREATE PROCEDURE UpdateInsertGroup
    @GroupID VARCHAR(128),
    @GroupName VARCHAR(128)
AS
BEGIN
    MERGE INTO [GROUP] AS target
    USING (
        SELECT
            @GroupID AS GroupID,
            @GroupName AS GroupName
    ) AS source
    ON (target.GROUPID = source.GroupID)
    WHEN MATCHED THEN
        UPDATE SET
            [NAME] = source.GroupName
    WHEN NOT MATCHED THEN
        INSERT (
            [GROUPID],
            [NAME]
        )
        VALUES (
            source.GroupID,
            source.GroupName
        );
END;
GO
CREATE PROCEDURE UpdateInsertSprintMetrics
    @MetricsID INT,
    @SPCommitted INT,
    @SPAdded INT,
    @SPChanged INT,
    @SPCompleted INT,
    @SPCompletedOfCommitted INT,
    @NIssuesCommitted INT,
    @NIssuesRemoved INT,
    @NIssuesCompleted INT,
    @NIssuesCompletedCommitted INT,
    @NIssuesNotCompleted INT
AS
BEGIN
    MERGE INTO [SPRINT_METRICS] AS target
    USING (
        SELECT
            @MetricsID AS MetricsID,
            @SPCommitted AS SPCommitted,
            @SPAdded AS SPAdded,
            @SPChanged AS SPChanged,
            @SPCompleted AS SPCompleted,
            @SPCompletedOfCommitted AS SPCompletedOfCommitted,
            @NIssuesCommitted AS NIssuesCommitted,
            @NIssuesRemoved AS NIssuesRemoved,
            @NIssuesCompleted AS NIssuesCompleted,
            @NIssuesCompletedCommitted AS NIssuesCompletedCommitted,
            @NIssuesNotCompleted AS NIssuesNotCompleted
    ) AS source
    ON (target.ID = source.MetricsID)
    WHEN MATCHED THEN
        UPDATE SET
            SP_COMMITTED = source.SPCommitted,
            SP_ADDED = source.SPAdded,
            SP_CHANGED = source.SPChanged,
            SP_COMPLETED = source.SPCompleted,
            SP_COMPLETED_OF_COMMITTED = source.SPCompletedOfCommitted,
            N_ISSUES_COMMITTED = source.NIssuesCommitted,
            N_ISSUES_REMOVED = source.NIssuesRemoved,
            N_ISSUES_COMPLETED = source.NIssuesCompleted,
            N_ISSUES_COMPLETED_COMMITTED = source.NIssuesCompletedCommitted,
            N_ISSUES_NOT_COMPLETED = source.NIssuesNotCompleted
    WHEN NOT MATCHED THEN
        INSERT (
            ID,
            SP_COMMITTED,
            SP_ADDED,
            SP_CHANGED,
            SP_COMPLETED,
            SP_COMPLETED_OF_COMMITTED,
            N_ISSUES_COMMITTED,
            N_ISSUES_REMOVED,
            N_ISSUES_COMPLETED,
            N_ISSUES_COMPLETED_COMMITTED,
            N_ISSUES_NOT_COMPLETED
        )
        VALUES (
            source.MetricsID,
            source.SPCommitted,
            source.SPAdded,
            source.SPChanged,
            source.SPCompleted,
            source.SPCompletedOfCommitted,
            source.NIssuesCommitted,
            source.NIssuesRemoved,
            source.NIssuesCompleted,
            source.NIssuesCompletedCommitted,
            source.NIssuesNotCompleted
        );
END;
GO
CREATE PROCEDURE UpdateInsertStatusCategory
    @ID INT,
    @Key VARCHAR(25),
    @Name VARCHAR(50)
AS
BEGIN
    MERGE INTO [STATUS_CATEGORY] AS target
    USING (
        SELECT
            @ID AS ID,
            @Name AS [NAME],
            @KEY AS [KEY]
    ) AS source
    ON (target.ID = source.ID)
    WHEN MATCHED THEN
        UPDATE SET
            [NAME] = source.[NAME],
            [KEY] = source.[KEY]
    WHEN NOT MATCHED THEN
        INSERT (
            [ID],
            [NAME],
            [KEY]
        )
        VALUES (
            source.ID,
            source.[NAME],
            source.[KEY]
        );
END;
GO
GO
CREATE PROCEDURE UpdateInsertStatus
    @StatusID INT,
    @StatusName VARCHAR(50),
    @StatusCategory INT
AS
BEGIN
    MERGE INTO [STATUS] AS target
    USING (
        SELECT
            @StatusID AS StatusID,
            @StatusName AS StatusName,
            @StatusCategory AS StatusCategory
    ) AS source
    ON (target.ID = source.StatusID)
    WHEN MATCHED THEN
        UPDATE SET
            [STATUS] = source.StatusName,
            [Category] = source.StatusCategory
    WHEN NOT MATCHED THEN
        INSERT (
            [ID],
            [STATUS],
            [CATEGORY]
        )
        VALUES (
            source.StatusID,
            source.StatusName,
            source.StatusCategory
        );
END;
GO
