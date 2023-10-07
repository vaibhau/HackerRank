/*
Enter your query here.
*/

SELECT CASE WHEN (A+B>C) AND (B+C>A) AND (A+C>B)
            THEN CASE WHEN (A=B) AND (B=C) AND (A=C)
                      THEN 'Equilateral'
                      WHEN (A=B) OR (B=C) OR (A=C)
                      THEN 'Isosceles'
                      ELSE 'Scalene'
                 END
            ELSE 'Not A Triangle'
       END
FROM Triangles;
