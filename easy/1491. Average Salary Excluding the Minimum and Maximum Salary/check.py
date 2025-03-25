from typing import List

salary_1 = [4000,3000,1000,2000]
salary_2 = [1000,2000,3000]

def average(salary: List[int]) -> float:
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
    print(salary_sum, len(salary) - 2)

average(salary_2)