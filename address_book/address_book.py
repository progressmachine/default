import json
import os

FILE = "contacts.json"

# ---------------------------
# Helpers
# ---------------------------

def load_contacts():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

# ---------------------------
# Core functions
# ---------------------------

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {"name": name, "phone": phone, "email": email}
    contacts = load_contacts()
    contacts.append(contact)
    save_contacts(contacts)
    print("✅ Contact added.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

# ---------------------------
# Menu Loop
# ---------------------------

def main():
    while True:
        print("\n[1] Add Contact  [2] View Contacts  [3] Exit")
        choice = input("Choose: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Goodbye.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
