-- HR Database, Joins Practice

-- Query 1A: Inner Join - Names and Start Dates 
SELECT E.F_NAME, E.EMP_ID, E.DEP_ID,
		J.START_DATE, J.EMPL_ID
FROM EMPLOYEES E INNER JOIN JOB_HISTORY J 
	ON E.EMP_ID = J.EMPL_ID
WHERE E.DEP_ID=5;
	
-- Query 1B: Inner Join - Names, Start Dates, and Job Titles 
SELECT E.F_NAME, E.EMP_ID, E.DEP_ID,
		JH.START_DATE, JH.EMPL_ID, JH.JOBS_ID,
		J.JOB_IDENT, J.JOB_TITLE		
FROM EMPLOYEES E 
	INNER JOIN JOB_HISTORY JH ON E.EMP_ID = JH.EMPL_ID
	INNER JOIN JOBS J ON JH.JOBS_ID = J.JOB_IDENT	 
WHERE E.DEP_ID=5;
	
-- Query 2A: Left Outer Join - Employees and Department tables 
-- vars: E: emp_id, l_name, dep_id
-- vars: D: dept_id_dep, dep_name
-- set: all employees
SELECT E.EMP_ID, E.L_NAME, E.DEP_ID,
		D.DEPT_ID_DEP, D.DEP_NAME
FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D 
	ON E.DEP_ID=D.DEPT_ID_DEP;

-- Query 2B: Subset Query 2A to employees born before 1980.
SELECT E.EMP_ID, E.L_NAME, E.DEP_ID,
		D.DEPT_ID_DEP, D.DEP_NAME
FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D 
	ON E.DEP_ID=D.DEPT_ID_DEP
WHERE YEAR(E.B_DATE) < 1980;

-- Query 2C: Subset Query 2A 
-- include department names for only employees born before 1980.
-- set: from all employees
SELECT E.EMP_ID, E.L_NAME, E.DEP_ID,
		D.DEPT_ID_DEP, D.DEP_NAME
FROM EMPLOYEES E LEFT JOIN DEPARTMENTS D 
	ON E.DEP_ID=D.DEPT_ID_DEP
	AND YEAR(E.B_DATE) < 1980;

-- Query 3A: Full Join on the Employees and Department tables
-- vars: E: f_name, l_name
-- vars: D: dep_name
-- set: all employees
SELECT E.F_NAME, E.L_NAME,
		D.DEP_NAME
FROM EMPLOYEES E FULL JOIN DEPARTMENTS D 
	ON E.DEP_ID=D.DEPT_ID_DEP;
	
-- Query 3B: Re-write Query 3A to have the result set include all employee
-- names but department id and department names only for male employees.
SELECT E.F_NAME, E.L_NAME,
		D.DEP_NAME
FROM EMPLOYEES E FULL JOIN DEPARTMENTS D 
	ON E.DEP_ID=D.DEPT_ID_DEP
	AND E.SEX = 'M';