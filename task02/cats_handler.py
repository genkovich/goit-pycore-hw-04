from pathlib import Path


def get_cats_info(path: Path) -> []:
    cats = []
    line_number = 1
    with open(path, 'r') as file:
        for line in file:
            try:
                id, name, age = line.split(',')

                cats.append({
                    'id': id,
                    'name': name,
                    'age': age
                })
            except ValueError:
                print('Invalid line:', line_number)
            finally:
                line_number += 1

    return cats
