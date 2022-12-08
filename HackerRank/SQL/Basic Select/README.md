# Solutions to SQL Basic Select

## Revising the Select Query 1 
**Question : Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.**
Solution : 
SELECT * FROM CITY 
WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';

## Revising the Select Query 2 
**Question : Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.**
Solution : 
SELECT NAME FROM CITY 
WHERE POPULATION > 120000 AND COUNTRYCODE = 'USA';

## SELECT ALL
**Question : Query all columns (attributes) for every row in the CITY table.**
Solution : 
SELECT * FROM CITY;

## SELECT BY ID
**Question : Query all columns for a city in CITY with the ID 1661.**
Solution : 
SELECT * FROM CITY WHERE ID = 1661;


## Japanese Cities' Attributes
**Question : Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.**
Solution : 
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';

## Japanese Cities' Names
**Question : Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.**
Solution : 
SELECT NAME FROM CITY
WHERE COUNTRYCODE = 'JPN';

## Weather Observation Station 1
**Question : Query a list of CITY and STATE from the STATION table.**
Solution : 
SELECT CITY, STATE FROM STATION;

## Weather Observation Station 3
**Question : Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.**
Solution : 
SELECT DISTINCT(CITY) FROM STATION 
WHERE MOD(ID,2) = 0;

## Weather Observation Station 4
**Question : Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.**
Solution : 
SELECT COUNT(CITY) - COUNT(DISTINCT(CITY)) FROM STATION;

## Weather Observation Station 5
**Question : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.**
Solution : 
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY length(city) ASC,city ASC LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY length(city) DESC,city ASC LIMIT 1;

## Weather Observation Station 6
**Question : Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT(CITY) FROM STATION WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' 
OR CITY LIKE 'U%' ORDER BY CITY ASC; 

## Weather Observation Station 7
**Question : Query the list of CITY names ending with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT(CITY) FROM STATION WHERE CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' 
OR CITY LIKE '%u';       

## Weather Observation Station 8
**Question : Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT(CITY) FROM STATION WHERE (CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' 
OR CITY LIKE 'U%')  AND (CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%i' OR CITY LIKE '%o' 
OR CITY LIKE '%u'); 

## Weather Observation Station 9
**Question : Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT CITY FROM STATION WHERE upper(SUBSTR(CITY,1,1)) NOT IN ('A','E','I','O','U') AND lower(SUBSTR(CITY,1,1)) NOT IN
('a','e','i','o','u');  

## Weather Observation Station 10
**Question : Query the list of CITY names from STATION that do not END with vowels. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT CITY FROM STATION WHERE upper(SUBSTR(CITY,LENGTH(CITY),1)) NOT IN ('A','E','I','O','U') AND lower(SUBSTR(CITY,LENGTH(CITY),1)) NOT IN
('a','e','i','o','u'); 

## Weather Observation Station 11
**Question : Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY,1,1)) NOT IN ('a','e','i','o','u') OR LOWER(SUBSTR(CITY, LENGTH(CITY),1)) NOT IN ('a','e','i','o','u');  

## Weather Observation Station 12
**Question : Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.**
Solution : 
SELECT DISTINCT CITY FROM STATION WHERE LOWER(SUBSTR(CITY,1,1)) NOT IN ('a','e','i','o','u') AND LOWER(SUBSTR(CITY, LENGTH(CITY),1)) NOT IN ('a','e','i','o','u');   

## Higher Than 75 Marks
**Question : Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.**
Solution : 
SELECT NAME FROM STUDENTS
WHERE MARKS > 75 
ORDER BY SUBSTR(NAME,LENGTH(NAME)-2,3), ID;   

## Employee Names
**Question : Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.**
Solution : 
SELECT NAME FROM EMPLOYEE
ORDER BY NAME;

## Employee SALARIES
**Question : Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than $2000 per month who have been employees for less than  months. Sort your result by ascending employee_id.**
Solution : 
SELECT NAME FROM EMPLOYEE 
WHERE SALARY > 2000 AND MONTHS < 10
ORDER BY EMPLOYEE_ID;
