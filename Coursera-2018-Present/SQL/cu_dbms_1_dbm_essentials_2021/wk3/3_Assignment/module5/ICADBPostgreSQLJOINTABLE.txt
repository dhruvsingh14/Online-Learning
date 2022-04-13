-- Programmer: Dhruv Singh
-- Date Modified: 11/26/20
-- Title: Module 5: Assignment
-- Topic: Insert Statements
-- DBMS: PostgreSQL

-- SECTION 1: SELECT STATEMENTS

-- Part 1: Inner Join
SELECT EventRequest.EventNo, DateHeld, Count(PlanNo)
  FROM EventRequest INNER JOIN EventPlan ON EventRequest.EventNo = EventPlan.EventNo
  WHERE DATE_PART('YEAR', EventPlan.WorkDate) = 2018
  AND DATE_PART('MONTH', EventPlan.WorkDate) = 12
  GROUP BY EventRequest.EventNo
  Having COUNT(PlanNo) > 0; 
 
-- Part 2: Joining Three Tables
SELECT PlanNo, EventPlan.EventNo, WorkDate, Activity	
  FROM Facility INNER JOIN EventRequest ON Facility.FacNo = EventRequest.FacNo
    INNER JOIN EventPlan ON EventRequest.EventNo = EventPlan.EventNo
  WHERE DATE_PART('YEAR', WorkDate) = 2018
  AND DATE_PART('MONTH', WorkDate) = 12
  AND Facility.FacName = 'Basketball arena';

-- Part 3: Date Range
SELECT EventRequest.EventNo, DateHeld, Status, EstCost	
  FROM EventRequest INNER JOIN EventPlan ON EventRequest.EventNo = EventPlan.EventNo
    INNER JOIN Employee ON EventPlan.EmpNo = Employee.EmpNo
    INNER JOIN Facility ON Facility.FacNo = EventRequest.FacNo
  WHERE Employee.EmpName = 'Mary Manager'
  AND DATE_PART('YEAR', DateHeld) = 2018
  AND DATE_PART('MONTH', DateHeld) BETWEEN 10 AND 12
  AND DATE_PART('DAY', DateHeld) BETWEEN 1 AND 31 
  AND FacName = 'Basketball arena';  

-- Part 4: 6 Table Join
SELECT EventPlan.PlanNo, LineNo, ResName, NumberFld, LocName, TimeStart, TimeEnd
  FROM Facility INNER JOIN Location ON Facility.FacNo = Location.FacNo
    INNER JOIN EventPlanLine ON Location.LocNo = EventPlanLine.LocNo
    INNER JOIN ResourceTbl ON ResourceTbl.ResNo = EventPlanLine.ResNo
    INNER JOIN EventPlan ON EventPlan.PlanNo = EventPlanLine.PlanNo
    INNER JOIN Employee ON Employee.EmpNo = EventPlan.EmpNo
  WHERE FacName = 'Basketball arena'
  AND Activity = 'Operation'
  AND DATE_PART('YEAR', WorkDate) = 2018
  AND DATE_PART('MONTH', WorkDate) BETWEEN 10 AND 12
  AND DATE_PART('DAY', WorkDate) BETWEEN 1 AND 31;   

-- SECTION 2: MODIFICATION STATEMENTS
  
-- Part 1: Insert
INSERT INTO Facility
  (FacNo, FacName)
VALUES ('F104', 'Swimming Pool');

-- Part 2: Insert continued table 2
INSERT INTO Location
  (LocNo, FacNo, LocName)
VALUES ('L107', 'F104', 'Door');

-- Part 3: Insert continued row 2 table 2
INSERT INTO Location
  (LocNo, FacNo, LocName)
VALUES ('L108', 'F104', 'Locker Room');

-- Part 4: Update
UPDATE Location
  SET LocName = 'Gate'
  WHERE LocName = 'Door';

-- Part 5: Delete
DELETE FROM Location
  WHERE LocNo = 'L108'
  AND FacNo = 'F104';
  
-- SECTION 3: QUERY ERRORS

-- Part 1: missing join from eventrequest to eventplan
-- doing so misses the 'and' function, and acts more as an 'or' statement
SELECT eventrequest.eventno, dateheld, status, estcost
FROM eventrequest, employee, facility, eventplan
WHERE estaudience > 5000 
  AND eventplan.empno = employee.empno 
  AND eventrequest.eventno = eventplan.eventno
  AND eventrequest.facno = facility.facno
  AND facname = 'Football stadium' 
  AND empname = 'Mary Manager';

-- Part 2: Group By is completely redundant
-- and uses up compute power
SELECT DISTINCT eventrequest.eventno, dateheld, status, estcost
FROM eventrequest, eventplan
WHERE estaudience > 4000
  AND eventplan.eventno = eventrequest.eventno;

-- Part 3: Employee table and Join are completely redundant
-- since it is not called in the where clause at all
SELECT DISTINCT eventrequest.eventno, dateheld, status, estcost
FROM eventrequest, facility, eventplan
WHERE estaudience > 5000
  AND eventplan.eventno = eventrequest.eventno 
  AND eventrequest.facno = facility.facno
  AND facname = 'Football stadium';


-- Part 4: Between is misspelt, and eventno is an ambiguous call
SELECT DISTINCT eventrequest.eventno, dateheld, status, estcost
FROM eventrequest, employee, eventplan
WHERE estaudience BETWEEN 5000 AND 10000
  AND eventplan.empno = employee.empno 
  AND eventrequest.eventno = eventplan.eventno
  AND empname = 'Mary Manager';
  
-- Part 5: Indentation
SELECT eventplan.planno, lineno, resname, numberfld, timestart, timeend
  FROM eventrequest, facility, eventplan, eventplanline, resourcetbl
    WHERE estaudience = '10000'
	AND eventplan.planno = eventplanline.planno 
	AND eventrequest.facno = facility.facno
    AND facname = 'Basketball arena' 
	AND eventplanline.resno = resourcetbl.resno
    AND eventrequest.eventno = eventplan.eventno;





















