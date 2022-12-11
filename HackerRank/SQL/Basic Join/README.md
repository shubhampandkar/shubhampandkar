# Solutions to Basic Joins
  
## Population Census  
**Question : Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.  
Note: CITY.CountryCode and COUNTRY.Code are matching key columns.**   
Solution :   
SELECT SUM(C.POPULATION) FROM CITY C JOIN COUNTRY CO   
ON C.COUNTRYCODE = CO.CODE   
WHERE CO.CONTINENT = 'Asia';  

## African Cities  
**Question : Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.  
Note: CITY.CountryCode and COUNTRY.Code are matching key columns.**   
Solution :   
SELECT C.NAME FROM CITY C JOIN COUNTRY CO   
ON C.COUNTRYCODE = CO.CODE   
WHERE CO.CONTINENT = 'Africa';  

## Average Population of Each Continent 
**Question : Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.
Note: CITY.CountryCode and COUNTRY.Code are matching key columns.**   
Solution :   
SELECT CO.CONTINENT, FLOOR(AVG(C.POPULATION))  
FROM COUNTRY CO JOIN CITY C ON CO.CODE = C.COUNTRYCODE  
GROUP BY CO.CONTINENT;  

## The Report 
**Question : You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks. Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.
Write a query to help Eve.**   
Solution :   
SELECT   
CASE WHEN G.GRADE < 8 THEN NULL   
WHEN G.GRADE >= 8 THEN S.NAME END,  
G.GRADE, S.MARKS FROM STUDENTS S, GRADES G  
WHERE S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK  
ORDER BY G.GRADE DESC, S.NAME ASC;  
