# Solutions to Advanced Joins  
  
## Population Census  
**Question : You are given a table, Projects, containing three columns: Task_ID, Start_Date and End_Date. It is guaranteed that the difference between the End_Date and the Start_Date is equal to 1 day for each row in the table. If the End_Date of the tasks are consecutive, then they are part of the same project. Samantha is interested in finding the total number of different projects completed.
Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.**   
Solution :   
SELECT START_DATE, MIN(END_DATE)  
FROM (SELECT START_DATE FROM PROJECTS  
     WHERE START_DATE NOT IN (SELECT END_DATE FROM PROJECTS)) A,  
     (SELECT END_DATE FROM PROJECTS WHERE END_DATE NOT IN   
      (SELECT START_DATE FROM PROJECTS)) B  
WHERE START_DATE < END_DATE  
GROUP BY START_DATE  
ORDER BY DATEDIFF(MIN(END_DATE),START_DATE) ASC, START_DATE ASC;  
  
## Placements  
**Question : You are given three tables: Students, Friends and Packages. Students contains two columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of the ONLY best friend). Packages contains two columns: ID and Salary (offered salary in $ thousands per month). Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.**   
Solution :   
SELECT S.NAME FROM STUDENTS S JOIN FRIENDS F ON S.ID = F.ID  
JOIN PACKAGES P1 ON S.ID = P1.ID  
JOIN PACKAGES P2 ON F.FRIEND_ID = P2.ID  
WHERE P2.SALARY > P1.SALARY  
ORDER BY P2.SALARY;   

## Symmetric Pairs  
**Question : Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.**   
Solution :   
SELECT F1.X, F1.Y FROM FUNCTIONS F1  
WHERE F1.X = F1.Y AND   
(SELECT COUNT( * ) FROM FUNCTIONS  
WHERE X = F1.X AND Y = F1.Y) > 1  
UNION  
SELECT F1.X, F1.Y FROM FUNCTIONS F1  
WHERE EXISTS(SELECT X, Y FROM FUNCTIONS   
            WHERE F1.X = Y AND F1.Y = X  
            AND F1.X < X)  
            ORDER BY X;  
          
## Interviews  
**Question : Samantha interviews many candidates from different colleges using coding challenges and contests. Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. Exclude the contest from the result if all four sums are 0.
Note: A specific contest can be used to screen candidates at more than one college, but each college only holds 1 screening contest.**   
Solution :   
SELECT CON.CONTEST_ID, CON.HACKER_ID, CON.NAME, SUM(SG.TOTAL_SUBMISSIONS), SUM(SG.TOTAL_ACCEPTED_SUBMISSIONS),  
SUM(VG.TOTAL_VIEWS), SUM(VG.TOTAL_UNIQUE_VIEWS)   
FROM CONTESTS CON   
JOIN COLLEGES COL   
ON CON.CONTEST_ID = COL.CONTEST_ID  
JOIN CHALLENGES CHA   
ON CHA.COLLEGE_ID = COL.COLLEGE_ID  
LEFT JOIN  
(SELECT SS.CHALLENGE_ID, SUM(SS.TOTAL_SUBMISSIONS) AS TOTAL_SUBMISSIONS, SUM(SS.TOTAL_ACCEPTED_SUBMISSIONS) AS TOTAL_ACCEPTED_SUBMISSIONS FROM   
SUBMISSION_STATS SS GROUP BY SS.CHALLENGE_ID) SG  
ON CHA.CHALLENGE_ID = SG.CHALLENGE_ID  
LEFT JOIN  
(SELECT VS.CHALLENGE_ID, SUM(VS.TOTAL_VIEWS) AS TOTAL_VIEWS, SUM(TOTAL_UNIQUE_VIEWS) AS TOTAL_UNIQUE_VIEWS FROM VIEW_STATS AS VS GROUP BY VS.CHALLENGE_ID) VG  
ON CHA.CHALLENGE_ID = VG.CHALLENGE_ID  
GROUP BY CON.CONTEST_ID, CON.HACKER_ID, CON.NAME  
HAVING SUM(SG.TOTAL_SUBMISSIONS)+  
       SUM(SG.TOTAL_ACCEPTED_SUBMISSIONS)+  
       SUM(VG.TOTAL_VIEWS)+  
       SUM(VG.TOTAL_UNIQUE_VIEWS) > 0  
ORDER BY CON.CONTEST_ID;  
