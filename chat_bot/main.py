contacts = {}

def parse_input(user_input):
    parts = user_input.strip().lower().split()
    cmd = parts[0]
    args = parts [1:]
    return cmd, args

def add_contact(args) :
    if len(args) < 2:
        print("Enter name and phone number")
        return
    name, phone = args[0], args[1]
    contacts[name] = phone
    print(f"Contact with name {name} and number {phone} added ")

def change_contact(args):
    if len(args) < 2 :
        print("Enter name and new phone number")
        return
    name, phone = args[0], args[1]

    if name in contacts:
        contacts[name] = phone
        print(f"Phone number for {name} changed to {phone}")
    else:
        print(f"Contact with name {name} not found ")

def show_phone(args) :
    if not args:
        print("Enter contact name")
        return
    name = args[0]
    phone = contacts.get(name)
    if phone:
        print(f"Phone number for {name}: {phone}")
    else:
        print(f"Contact with name {name} not found")

def show_all():
    if not contacts:
        print("Contact is absent")
    else:    
        print("All contacts:")
    for name, phone in contacts.items():
        print(f"{name.title()}: {phone}")

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            add_contact(args)

        elif command == "change":
            change_contact(args)

        elif command == "phone":
            show_phone(args)

        elif command == "all":
            show_all()

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
