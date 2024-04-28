import sys
from pathlib import Path
from printer import print_files


def main():
    if len(sys.argv) < 2:
        print("No path passed")
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print("Path does not exist")
        sys.exit(1)

    print_files(path)


if __name__ == "__main__":
    main()
