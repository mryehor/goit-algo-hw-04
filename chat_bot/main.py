def parse_input(user_input):
    parts = user_input.strip().lower().split()
    cmd = parts[0]
    args = parts [1:]
    return cmd, args

def add_contact(contacts, args) :
    if len(args) < 2:
        return "Enter name and phone number (e.g. add Alice 12345)"
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Contact with name {name} and number {phone} added "

def change_contact(contacts, args):
    if len(args) < 2 :
        return "Enter name and new phone number"
    name, phone = args[0], args[1]

    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        return f"Contact with name {name} not found "

def show_phone(contacts, args) :   
    if not args:
        return "Enter contact name"
    name = args[0]
    phone = contacts.get(name)
    if phone:
        return f"Phone number for {name}: {phone}"
    else:
        return f"Contact with name {name} not found"

def show_all(contacts):
    if not contacts:
        return "Contact list is empty"
    else:    
        result = ["All contacts: "]
        for name, phone in contacts.items():
            result.append(f"{name.title()}: {phone}")
        return "\n".join(result)
        
def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            result = add_contact(contacts, args)
            print(result)

        elif command == "change":
            result = change_contact(contacts, args)
            print(result)

        elif command == "phone":
            result = show_phone(contacts, args)
            print(result)

        elif command == "show":
            result = show_all(contacts)
            print(result)
            
        else:
            print("Unknown command. Try: add, change, phone, show, exit")

if __name__ == "__main__":
    main()
