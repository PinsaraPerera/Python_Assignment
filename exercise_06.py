import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        try:
            if self.contacts[contact.name]:
                return f"{contact.name} already exists in the contacts"
        except:
            self.contacts[contact.name] = {"phone": contact.phone, "email": contact.email}
            self.save_contact({"name": contact.name, "phone": contact.phone, "email": contact.email})

    def del_contact(self, name):
        del self.contacts[name]

    def search_contact(self, name):
        if self.contacts and self.contacts[name]:
            return self.contacts[name]
        else:
            return f"{name} not found in the contacts"
    
    def save_contact(self, contact):
        with open("contacts.txt", "a") as file:
            file.write(f"{contact['name']}, {contact['phone']}, {contact['email']}\n")

    def load_contacts(self):
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(", ")
                if name not in self.contacts:
                    self.contacts[name] = {"phone": phone, "email": email}

# Create some contacts
contact1 = Contact("Pawan", "1234567890", "pawan@gmail.com")
contact2 = Contact("Pinsara", "9577305765", "pinsara@gmail.com")
contact3 = Contact("Perera", "4561237890", "perera@gmail.com")
contact4 = Contact("Perera", "4561237890", "perera@gmail.com")

# Create a phone book object and add the contacts
phone_book = PhoneBook()

if os.path.exists("contacts.txt"):
    # Load the contacts from the file
    phone_book.load_contacts()
    print(phone_book.contacts)

phone_book.add_contact(contact1)
phone_book.add_contact(contact2)
phone_book.add_contact(contact3)
phone_book.add_contact(contact4)

# Search for a contact "Pawan"
print(phone_book.search_contact("Pawan"))

# Delete the contact "Pinsara"
phone_book.del_contact("Pinsara")

print(phone_book.contacts)


                