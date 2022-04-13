-- Programmer: Dhruv Singh
-- Date Modified: 11/21/20
-- Title: Module 5: Practice
-- Topic: Insert Statements
-- DBMS: PostgreSQL

-- Part 1: Boulder customers
SELECT EventNo, DateHeld, Customer.CustNo, CustName, Facility.FacNo, FacName
FROM Facility, EventRequest, Customer
WHERE Facility.FacNo = EventRequest.FacNo
AND Customer.CustNo = EventRequest.CustNo
AND City = 'Boulder'
AND DATE_PART('YEAR', DateHeld) = 2018;

-- Part 2: Calculations
SELECT Customer.CustNo, CustName, EventNo, DateHeld, Facility.FacNo, FacName, 
		EstCost/EstAudience as EstCostPc
FROM Facility, EventRequest, Customer
WHERE Facility.FacNo = EventRequest.FacNo
AND Customer.CustNo = EventRequest.CustNo
AND EstCost/EstAudience < 0.2;

-- Part 3: Group by
SELECT Customer.CustNo, CustName, SUM(EstCost) as TotalEstCost 
FROM Customer, EventRequest
WHERE Customer.CustNo = EventRequest.CustNo
AND Status = 'Approved'
GROUP BY Customer.CustNo, CustName;

-- Part 4: Insert
INSERT INTO Customer
  (CustNo, CustName, Address, Internal, Contact, Phone, 
   City, State, Zip)
VALUES ('C106', 'Men''s Distance Running' , '2800 Quebec Street NW', 'Y', 'Dhruv Singh',
	'7516229', 'Washington', 'DC', '20008');

-- Part 5: Update
UPDATE ResourceTbl
  SET Rate = 1.1*Rate
  WHERE ResName = 'nurse';

-- Part 6: Delete
DELETE FROM Customer
  WHERE CustName = 'Men''s Distance Running';









