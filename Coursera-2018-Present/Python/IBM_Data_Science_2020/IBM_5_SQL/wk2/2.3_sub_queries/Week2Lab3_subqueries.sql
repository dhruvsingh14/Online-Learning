SELECT * FROM EMPLOYEES;

-- sub queries and nested selects

-- sub query using sub select statement in where clause 
SELECT EMP_ID, F_NAME, L_NAME, SALARY
			from EMPLOYEES
			where SALARY < 
			(select AVG(SALARY) from EMPLOYEES);
			
-- sub queries: column expressions
SELECT EMP_ID, SALARY, 
				( SELECT AVG(SALARY) from EMPLOYEES )
									AS AVG_SALARY
				from EMPLOYEES;
				
-- derived tables  
SELECT * from 
				( SELECT EMP_ID, F_NAME, L_NAME, DEP_ID
									from EMPLOYEES) AS EMP4ALL ;

-- multiple tables

-- subsetting using other table, by department id
SELECT * from EMPLOYEES
				WHERE DEP_ID IN 
				( SELECT DEPT_ID_DEP from DEPARTMENTS) ;
				
-- to retrieve records based on location info  from other table 
SELECT * from EMPLOYEES
				WHERE DEP_ID IN 
				( SELECT DEPT_ID_DEP from DEPARTMENTS
									WHERE LOC_ID = 'L0002');
									
-- retrieving dept id and name for those earning more than 70 k 
SELECT DEPT_ID_DEP, DEP_NAME from DEPARTMENTS
	WHERE DEPT_ID_DEP IN 
		( SELECT DEP_ID from EMPLOYEES
			WHERE SALARY > 70000 ) ;
			
-- joins

-- full join, or cartesian join 
SELECT * from EMPLOYEES, DEPARTMENTS; 

-- using aliases to perform implicit join 
SELECT * from EMPLOYEES E, DEPARTMENTS D
				WHERE E.DEP_ID = D.DEPT_ID_DEP;
				
				
-- selecting columns from multiple tables by id using implicit join 
SELECT E.EMP_ID, D.DEP_ID_DEP from
				EMPLOYEES E, DEPARTMENTS D 
				WHERE E.DEP_ID = D.DEPT_ID_DEP;		
-- [giving error at this point]
				

			
			
			
			
			
			
			
			
			
			
			
			