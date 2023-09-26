import json

# Initialize an empty contacts dictionary to store contact information
contacts = {}

# Define the filename for storing contact data
contact_file = "contacts.json"

# Load existing contacts from the file, if available
try:
    with open(contact_file, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    pass

def save_contacts():
    # Save the updated contacts dictionary to the file
    with open(contact_file, "w") as file:
        json.dump(contacts, file)

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    
    save_contacts()
    print(f"Contact '{name}' added successfully.")

def view_contact_list():
    print("Contact List:")
    for name, contact in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print("-----------")

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    
    for name, contact in contacts.items():
        if query in (name, contact['phone']):
            print("Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
    
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        phone = input(f"Enter new phone number for {name}: ")
        email = input(f"Enter new email for {name}: ")
        address = input(f"Enter new address for {name}: ")
        
        contacts[name]["phone"] = phone
        contacts[name]["email"] = email
        contacts[name]["address"] = address
        
        save_contacts()
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def show_menu():
    print("Contact Management Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact_list()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()