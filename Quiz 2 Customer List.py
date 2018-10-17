import csv

FILENAME = "customers.txt"

def write_customers(customers):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(customers)


def read_customers():
    customers = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            customers.append(line)
    return customers


def list_customers(customers):
    for i in range(len(customers)):
        customer = customers[i]
        print(str(i + 1) + ". " + customer[0] + " (" + customer[1] + ")")
    print()


def add_customer(customers):
    name = input("Name: ")
    email = input("E-mail: ")
    phone = input("Phone: ")
    customer = []
    name.append(name)
    email.append(email)
    phone.append(phone)
    write_customers(customers)
    print(customer + " was added.\n")


def delete_customer(customers):
    index = int(input("Customer: "))
    customer = customers.pop(index - 1)
    write_customers(customers)
    print(customer[0] + " was deleted.\n")


def display_menu():
    print("The Customer List program")
    print()
    print("COMMAND MENU")
    print("list - List all customers")
    print("slist - sorts and prints customer list")
    print("add -  Add a customer")
    print("del -  Delete a customer")
    print("exit - Exit program")
    print()


def main():
    display_menu()
    customers = read_customers()
    while True:
        command = input("Command: ")
        if command == "list":
            list_customers(customers)
        elif command == "add":
            add_customer(customers)
        elif command == "del":
            delete_customer(customers)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")


if __name__ == "__main__":
    main()