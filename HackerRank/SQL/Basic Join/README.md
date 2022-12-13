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

## Top Competitors
**Question : Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.**   
Solution :   
SELECT S.HACKER_ID, H.NAME FROM SUBMISSIONS S  
JOIN HACKERS H ON S.HACKER_ID = H.HACKER_ID  
JOIN CHALLENGES C ON S.CHALLENGE_ID = C.CHALLENGE_ID  
JOIN DIFFICULTY D ON C.DIFFICULTY_LEVEL = D.DIFFICULTY_LEVEL  
WHERE S.SCORE = D.SCORE  
GROUP BY H.NAME,S.HACKER_ID  
HAVING COUNT(S.CHALLENGE_ID) > 1  
ORDER BY COUNT(S.CHALLENGE_ID) DESC, S.HACKER_ID;  

## Ollivander's Inventory
**Question : Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.**   
Solution :   
SELECT W.ID, WP.AGE, W.COINS_NEEDED, W.POWER FROM WANDS W  
JOIN WANDS_PROPERTY WP ON W.CODE = WP.CODE  
WHERE W.COINS_NEEDED = (SELECT MIN(COINS_NEEDED) FROM WANDS W1  
                       INNER JOIN WANDS_PROPERTY WP1  
                       ON W1.CODE = WP1.CODE  
                       WHERE WP1.IS_EVIL = 0 AND WP.AGE = WP1.AGE  
                       AND W.POWER = W1.POWER). 
                       ORDER BY W.POWER DESC, WP.AGE DESC;  
                       
## Ollivander's Inventory
**Question : Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.**   
Solution :   
SELECT W.ID, WP.AGE, W.COINS_NEEDED, W.POWER FROM WANDS W  
JOIN WANDS_PROPERTY WP ON W.CODE = WP.CODE  
WHERE W.COINS_NEEDED = (SELECT MIN(COINS_NEEDED) FROM WANDS W1  
                       INNER JOIN WANDS_PROPERTY WP1  
                       ON W1.CODE = WP1.CODE  
                       WHERE WP1.IS_EVIL = 0 AND WP.AGE = WP1.AGE  
                       AND W.POWER = W1.POWER). 
                       ORDER BY W.POWER DESC, WP.AGE DESC;  
