-- Programmer: Dhruv Singh
-- Date Modified: 11/20/20
-- Title: Module 4: Practice
-- Topic: Select Statements
-- DBMS: PostgreSQL

-- Part 1: Unique distinct rows, no duplicates
SELECT DISTINCT City, State, Zip 
FROM Customer;

-- Part 2: String start matching
SELECT EmpName, Department, Phone, Email
FROM Employee
WHERE Phone LIKE '3-%';

-- Part 3: Rows with constraints
SELECT * FROM ResourceTbl
WHERE Rate BETWEEN 10 and 20
ORDER BY Rate;

-- Part 4: Date based querying
SELECT EventNo, DateAuth, Status 
FROM EventRequest 
WHERE Status IN ('Approved', 'Denied')
AND DATE_PART('YEAR', DateAuth) = 2018
AND DATE_PART('MONTH', DateAuth) = 07;

-- Part 5: Joins: facility and location
SELECT LocNo, LocName
FROM Location, Facility
WHERE Location.FacNo = Facility.FacNo
AND FacName = 'Basketball arena';

-- Part 6: Counting up unique instances for each plan number
SELECT PlanNo, COUNT(LineNo), SUM(NumberFld) as ResourceSum
FROM EventPlanLine
GROUP BY PlanNo
Having COUNT(LineNo) > 0; 















