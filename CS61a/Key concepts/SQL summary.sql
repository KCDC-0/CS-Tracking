-- ============================================================================
-- CS61A SQL REFERENCE
-- ============================================================================
-- SQL is a declarative language, these are common uses and syntax


-- 1. CREATING TABLES
-- Tables are created using 'CREATE TABLE ... AS' and 'UNION'

CREATE TABLE students AS
  SELECT "Oski" AS name, "A+" AS grade, 11 AS section UNION
  SELECT "Cal",          "B",      11            UNION
  SELECT "Peter",        "A",      12            UNION
  SELECT "Jane",         "A",      13            UNION
  SELECT "Joe",          "B",      13;



-- 2. BASIC SELECT STATEMENTS
-- Syntax: SELECT [columns] FROM [table] WHERE [condition] ORDER BY [sort];
-- '*' means select all columns
-- 'AS' renames a column in the output

-- COMMON OPERATORS
-- comparison operators: =, >, <, <=, >=, <> or != 
-- boolean operators: AND, OR
-- arithmetic operators: +, -, *, /
-- concatenation operator: ||

SELECT name, section FROM students WHERE grade = 'A' ORDER BY name;



-- 3. JOINS (COMBINING TABLES)
-- A join creates a Cartesian Product (all pairs) then filters them
-- Use aliases (e.g., 'AS s1') to join a table with itself

SELECT s1.name, s2.name
FROM students AS s1, students AS s2
WHERE s1.section = s2.section
  AND s1.name < s2.name;

-- the last line is used to avoid duplicates in pairing



-- 4. INSERTIONS
-- Inserting new data into an existing table

INSERT INTO students (name, grade, section) 
VALUES ('Ben', 'A-', 14);

-- Deleting data
-- DELETE FROM students WHERE name = 'Joe';



-- 5. AGGREGATION & GROUPING
-- Aggregates take many rows and condense them into one value
-- Common functions: COUNT(*), SUM(), AVG(), MIN(), MAX()

-- This statement counts students in each section
SELECT section, COUNT(*) AS total
FROM students
GROUP BY section;

-- Filter groups using HAVING
-- WHERE filters rows BEFORE grouping; HAVING filters groups AFTER aggregation
SELECT section, AVG(CASE WHEN grade = 'A' THEN 4 ELSE 3 END) AS gpa
FROM students
GROUP BY section
HAVING COUNT(*) >= 2;



-- 6. RECURSIVE SELECT (WITH STATEMENTS / CTEs)
-- This is the syntax for recursion: 
-- Base Case + UNION + Recursive Step

-- This statement generates Fibonacci numbers
WITH fib(curr, next) AS (
    SELECT 0, 1 UNION                             -- Base Case
    SELECT next, curr + next FROM fib WHERE next < 100 -- Recursive Step
)
SELECT curr FROM fib;



-- 7. BUILT-IN STRING CONCATENATION & LOGIC
-- SQLite uses || for string concatenation
-- Use 'CASE' for conditional logic within a SELECT statement

SELECT name || ' is in section ' || section FROM students;



-- ============================================================================
-- SUMMARY OF EXECUTION ORDER (Logical Flow)
-- 1. FROM (and JOINs) - Get the raw data
-- 2. WHERE            - Filter rows
-- 3. GROUP BY         - Group filtered rows
-- 4. HAVING           - Filter the groups
-- 5. SELECT           - Pick columns and calculate aggregates
-- 6. ORDER BY         - Final sorting
-- 7. LIMIT            - Truncate output
-- ============================================================================
