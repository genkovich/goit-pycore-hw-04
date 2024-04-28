from input_parser import parse_input
import phone_base


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid number of arguments.")
            else:
                name, phone = args
                phone_base.add_contact(name, phone)
                print(f"Contact {name} with phone {phone} was added.")
        elif command == "change":
            if len(args) != 2:
                print("Invalid number of arguments.")
            else:
                name, phone = args
                phone_base.change_contact(name, phone)
                print(f"Contact {name} with phone {phone} was changed.")
        elif command == "phone":
            if len(args) != 1:
                print("Invalid number of arguments.")
            else:
                name, = args
                phone_base.show_phone(name)
        elif command == "all":
            phone_base.show_contacts()
        else:
            print("Invalid command.")


if __name__ == '__main__':
    main()
