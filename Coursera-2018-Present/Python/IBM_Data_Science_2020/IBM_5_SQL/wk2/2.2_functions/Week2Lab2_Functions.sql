-- testing if table was read in
SELECT * FROM PETSALE;

-- built in functions: eg: sum, min, max, avg

-- example 1: sum
SELECT SUM(QUANTITY) from PETSALE;

-- example 2: sum as
SELECT SUM(QUANTITY) as SUM_OF_QTY
				from PETSALE;
				
-- example 3a: max 
SELECT MAX(SALEPRICE) from PETSALE;

-- example 3b: min 
SELECT MIN(SALEDATE) from PETSALE where ANIMAL = 'Dog';

-- example 4: avg func
SELECT AVG(QUANTITY) from PETSALE;

-- example 5: avg calculated
SELECT AVG(SALEPRICE / QUANTITY) from PETSALE 
				where ANIMAL = 'Dog';
				
-- example 6: round 
SELECT ROUND(SALEPRICE) from PETSALE;

-- example 7: length 
SELECT LENGTH(ANIMAL) from PETSALE;

-- example 8: ucase 
SELECT UCASE(ANIMAL) from PETSALE;

-- example 9: where plus str func 
SELECT * from PETSALE 
					where LCASE(ANIMAL) = 'cat';

-- example 10: distinct 
SELECT DISTINCT(UCASE(ANIMAL)) from PETSALE;

-- date time functions:

-- example 11: day 
SELECT DAY(SALEDATE) from PETSALE 
				WHERE ANIMAL = 'Cat';
				
-- example 12: where plus count func 
SELECT COUNT(*) from PETSALE
				WHERE MONTH(SALEDATE) = '05';

-- example 13: date calculations
SELECT (SALEDATE + 3 DAYS) from PETSALE;

-- example 14: special registers
SELECT (CURRENT_DATE - SALEDATE) from PETSALE;






















