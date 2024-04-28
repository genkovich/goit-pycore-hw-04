from pathlib import Path


def total_salary(path: Path) -> ():
    with open(path, 'r') as file:
        salary_sum = 0
        count = 0
        for line in file:
            name, salary = line.split(',')
            salary_sum += int(salary)
            count += 1

    if count == 0:
        return 0, 0
    average = salary_sum / count
    return salary_sum, average
