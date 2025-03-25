"""
1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of UNIQUE integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

"""


# This is my solution
class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = -1
        min_salary = 100000000
        salary_sum = 0
        for s in salary:
            salary_sum += s
            if s > max_salary:
                max_salary = s
            if s < min_salary:
                min_salary = s
        salary_sum = salary_sum - max_salary - min_salary
        return float(salary_sum / (len(salary) - 2))


# More pythonic
class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary=min(salary)
        max_salary=max(salary)
        sum_salary=sum(salary)
        sum_salary=sum_salary -(min_salary + max_salary)
        result=sum_salary / (len(salary)-2)
        return result

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary = salary[1:len(salary)-1]
        return sum(salary) / len(salary)