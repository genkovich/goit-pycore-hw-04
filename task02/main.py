from pathlib import Path
from cats_handler import get_cats_info


def main():
    try:
        path = Path('db_cats')
        cats = get_cats_info(path)
        print(cats)
    except FileNotFoundError:
        print('File not found')


if __name__ == '__main__':
    main()
