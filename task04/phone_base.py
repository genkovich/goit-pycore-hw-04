phones = {}


def add_contact(name, phone):
    if name in phones:
        print(f"Contact {name} already exists.")

    phones[name] = phone


def change_contact(name, phone):
    if name not in phones:
        print(f"Contact {name} does not exist.")
    else:
        phones[name] = phone


def show_contacts():
    for name, phone in phones.items():
        print(f"{name}: {phone}")


def show_phone(name):
    if name in phones:
        print(f"{name}: {phones[name]}")
    else:
        print(f"Contact {name} does not exist.")