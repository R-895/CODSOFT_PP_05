contacts = []

def add_contact():
    print("\nAdd New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    print("Contact added successfully!")

def view_contacts():
    print("\nContact List")
    if contacts:
        for idx, contact in enumerate(contacts):
            print(f"{idx+1}. {contact['name']} - {contact['phone']}")
    else:
        print("No contacts found.")

def search_contacts():
    print("\nSearch Contact")
    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact['name'].lower() or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
    else:
        print("No contacts found with that search term.")

def update_contact():
    print("\nUpdate Contact")
    search_term = input("Enter name or phone number to search: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("\nEnter new details (leave blank to keep current value):")
            contact['name'] = input(f"Name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
            return
    print("No contact found with that search term.")

def delete_contact():
    print("\nDelete Contact")
    search_term = input("Enter name or phone number to search: ").lower()
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("No contact found with that search term.")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
