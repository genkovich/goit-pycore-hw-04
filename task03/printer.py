from colorama import Fore


def print_files(dest, tabs=0):
    if not dest.is_dir():
        return
    for file in dest.iterdir():
        if file.is_file():
            print_file(file.name, tabs)
        else:
            tabs += 1
            print_directory(file.name, tabs)
            print_files(file, tabs)


def print_directory(name, tabs):
    print(f"{Fore.BLUE}{'  ' * tabs} {name}/{Fore.RESET}")


def print_file(name, tabs):
    print(f"{Fore.GREEN}{'  ' * (tabs + 1)}{name}{Fore.RESET}")
