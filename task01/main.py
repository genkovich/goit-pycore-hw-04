from pathlib import Path
from salary import total_salary


def main():
    try:
        path = Path('db_salaries')
        salary_sum, average = total_salary(path)
        print(f'Total salary: {salary_sum}, average salary: {average}')
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    main()
