# Write your MySQL query statement below
select  max(salary) as SecondHighestSalary
from Employee
WHERE Salary<>(SELECT max(salary)from Employee)