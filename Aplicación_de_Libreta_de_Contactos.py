# Mini proyecto. Libreta de contactos.

def display_menu():
    print('''Contact Book Menu:
    1. Add Contact
    2. View Contact
    3. Edit Contact
    4. Delete Contact
    5. List All Contacts
    6. Exit
    ''')


def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()

    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")


def view_contact(contact_book):
    name = input()

    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")


def edit_contact(contact_book):
    name = input()

    if name not in contact_book:
        print("Contact not found!")
        return

    phone = input()
    email = input()
    address = input()

    if phone != "":
        contact_book[name]["phone"] = phone
    if email != "":
        contact_book[name]["email"] = email
    if address != "":
        contact_book[name]["address"] = address

    print("Contact updated successfully!")


def delete_contact(contact_book):
    name = input()

    if name not in contact_book:
        print("Contact not found!")

    else:
        del contact_book[name]
        print("Contact deleted successfully!")


def list_all_contacts(contact_book):

    if not contact_book:
        print("No contacts available.")
        return

    for name, details in contact_book.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print()


contact_book = {}

while True:
    display_menu()
    choice = input()

    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        print('Exiting Contact book. Goodbye!')
        break
    else:
        print("Invalid option. Please try again.")

# Funciona en la terminal, ejecuta y observa las opciones enumeradas de lo que puedes hacer.

# Solo escribe números enteros. No decimales ni ningún otro digito que no esté entre 1 y 6.
