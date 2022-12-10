# Solutions to SQL Aggregation  
  
## Revising Aggregations - The Count Function  
**Question : Query a count of the number of cities in CITY having a Population larger than 100,000.**   
Solution :   
SELECT COUNT(ID) FROM CITY
WHERE POPULATION > 100000;  

## Revising Aggregations - The Sum Function  
**Question : Query the total population of all cities in CITY where District is California.**   
Solution :   
SELECT SUM(POPULATION) FROM CITY  
WHERE DISTRICT = 'California';  

## Revising Aggregations - Averages  
**Question : Query the average population of all cities in CITY where District is California.**   
Solution :   
SELECT AVG(POPULATION) FROM CITY  
WHERE DISTRICT = 'California';  

## Average Population  
**Question : Query the average population for all cities in CITY, rounded down to the nearest integer.**   
Solution :   
SELECT ROUND(AVG(POPULATION)) FROM CITY;  

## Japan Population  
**Question : Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.**   
Solution :   
SELECT SUM(POPULATION) FROM CITY  
WHERE COUNTRYCODE = 'JPN';  

## Population Density Difference  
**Question : Query the difference between the maximum and minimum populations in CITY.**   
Solution :   
SELECT MAX(POPULATION) - MIN(POPULATION) FROM CITY;  

## The Blunder   
**Question : Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.
Write a query calculating the amount of error (i.e.: actual-miscalculated  average monthly salaries), and round it up to the next integer.**   
Solution :   
SELECT CEIL(AVG(SALARY)- AVG(REPLACE(SALARY, '0', ''))) FROM EMPLOYEES;  

## Top Earners.   
**Question : We define an employee's total earnings to be their monthly salary x months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as 2 space-separated integers.
**   
Solution :   
SELECT SALARY*MONTHS, COUNT(*) FROM EMPLOYEE  
GROUP BY SALARY * MONTHS  
ORDER BY SALARY * MONTHS DESC  
LIMIT 1;  

## Weather Observation Station 2      
**Question : Query the following two values from the STATION table:  
The sum of all values in LAT_N rounded to a scale of  decimal places.  
The sum of all values in LONG_W rounded to a scale of  decimal places.**   
Solution :   
SELECT CAST(ROUND(SUM(LAT_N),2) AS DECIMAL (10,2)),   
CAST(ROUND(SUM(LONG_W),2) AS DECIMAL (10,2)) FROM STATION;  

## Weather Observation Station 13     
**Question : Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345. Truncate your answer to 4 decimal places.**   
Solution :   
SELECT TRUNCATE(SUM(LAT_N),4) FROM STATION  
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;  
