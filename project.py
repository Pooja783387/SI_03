import csv

class ContactManagementSystem:
    def __init__(self, contact_file='contacts.csv'):
        self.contact_file = contact_file
        self.contacts = self.load_contacts()

    def load_contacts(self):
        contacts = []
        try:
            with open(self.contact_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:  # skip empty rows
                        name, phone, email, address = row
                        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
        except FileNotFoundError:
            print("Contact file not found. Creating a new one.")
        return contacts

    def save_contacts(self):
        with open(self.contact_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact['name'], contact['phone'], contact['email'], contact['address']])

    def add_contact(self, name, phone, email, address):
        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact {name} added successfully.")

    def view_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\nAll Contacts:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                found = True
        if not found:
            print(f"No contact found for search term '{search_term}'.")

    def edit_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address
                self.save_contacts()
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def main():
    system = ContactManagementSystem()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            system.add_contact(name, phone, email, address)

        elif choice == '2':
            system.view_all_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            system.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to edit: ")
            new_phone = input("Enter new phone number (leave blank to keep unchanged): ")
            new_email = input("Enter new email (leave blank to keep unchanged): ")
            new_address = input("Enter new address (leave blank to keep unchanged): ")
            system.edit_contact(name, new_phone or None, new_email or None, new_address or None)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            system.delete_contact(name)

        elif choice == '6':
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
