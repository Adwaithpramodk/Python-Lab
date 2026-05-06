import json

contacts = {}

FILE_NAME = 'contact.json'

def load_contacts():
    global contacts
    try:
        with open(FILE_NAME,'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}

def save_contacts():
    with open(FILE_NAME,'w') as f:
        json.dump(contacts,f,indent=4)

def add_contacts():
    name  = input("Enter the name: ")
    if name in contacts:
        print("Contact Already Exists")
        return
    
    phone = input("Enter the Phone Numeber: ")
    email = input("Enter the Email: ")

    contacts[name] = {
        "phone":phone,
        "email":email
    }
    save_contacts()
    print("Contact saved Successfully")

def delete_contact():
    name = input('Enter the name')

    if name in contacts:
        contacts.pop(name)
        save_contacts()
        print("Contacts Updated Successfully")
    else:
        print("Contact Not Found")

def search_contact():
    name  = input("Enter the name: ")

    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone Number: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")

    else:
        print("Contact Not Found")

def view_contacts():
    if not contacts:
        print("No Contacts Available")
        return
    
    print("----Contact List----")
    for name,details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone Number: {details['phone']}")
        print(f"Email: {details['email']}")
        print("-----------------------------")


load_contacts()

while True:
    print("--- Contact Book App ---")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_contacts()

    elif choice == '2':
        delete_contact()

    elif choice == '3':
        search_contact()

    elif choice == '4':
        view_contacts()

    elif choice == '5':
        print("Closing Contact Book...")
        break

    else:
        print("Invalid choice")