# SQL Advanced Select Solutions. 
  
## Type of Triangle
**Question : Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with 3 sides of equal length.
Isosceles: It's a triangle with 2 sides of equal length.
Scalene: It's a triangle with 3 sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.**  
  
Solution :  
SELECT CASE
WHEN A + B <= C OR B + C <= A OR A + C <= B THEN 'Not A Triangle'
WHEN A = B AND B = C THEN 'Equilateral'
WHEN A = B OR B = C OR A = C THEN 'Isosceles'
ELSE 'Scalene'
END
FROM TRIANGLES;  

## The PADS
**Question : Generate the following two result sets:

Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format: There are a total of [occupation_count] [occupation]s.
where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.

Note: There will be at least two entries in the table for each type of occupation.**    
  
Solution :    
SELECT CONCAT(NAME, '(', LEFT(OCCUPATION,1), ')')
FROM OCCUPATIONS
ORDER BY NAME;  
   
SELECT CONCAT('There are a total of ', COUNT(OCCUPATION),' ',LOWER(OCCUPATION),'s.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(OCCUPATION), OCCUPATION;

## Occupations
**Question : Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.**    
  
Solution :    
select max(d), max(p),max(s), max(a)

from (select case when occupation = 'Doctor' then name end as d,

    case when occupation = 'Professor' then name end as p,

    case when occupation = 'Singer' then name end as s,

    case when occupation = 'Actor' then name end as a,

    row_number() over(partition by occupation order by name) as rn
from occupations) as t group by rn;

## Binary Tree Nodes
**Question : You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.**    
  
Solution :    
SELECT N, CASE
WHEN P IS NULL THEN 'Root'
WHEN N IN (SELECT P FROM BST) THEN 'Inner'
ELSE 'Leaf'
END
FROM BST
ORDER BY N;  

## New Companies
**Question : Amber's conglomerate corporation just acquired some new companies.
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

Note:

The tables may contain duplicate records.
The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.**    
  
Solution :    
SELECT C.COMPANY_CODE, C.FOUNDER, COUNT(DISTINCT(E.LEAD_MANAGER_CODE)),
COUNT(DISTINCT(E.SENIOR_MANAGER_CODE)), COUNT(DISTINCT(MANAGER_CODE)), 
COUNT(DISTINCT(EMPLOYEE_CODE)) FROM COMPANY C JOIN EMPLOYEE E
ON C.COMPANY_CODE = E.COMPANY_CODE
GROUP BY C.COMPANY_CODE, C.FOUNDER
ORDER BY C.COMPANY_CODE;
