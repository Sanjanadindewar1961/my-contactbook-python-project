from contact import Contact

class ContactBook:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,contact):
        self.contacts.append(contact)
    def display_all_contacts(self):
        if not self.contacts:
           print("No contacts to display")
        else:
            for contact in self.contacts:
                contact.display_contact()
    def search_contact(self,name):
           name=name.strip().lower()
           for contact in self.contacts:
               if contact.name.lower()==name:
                   return contact
           return None   
    def update_contact(self,name,new_name=None,new_phone=None,new_email=None):
        contact=self.search_contact(name)
        if contact:
            if new_name:
                contact.name=new_name.strip()
            if new_phone:
                contact.phone=new_phone.strip()
            if new_email:
                contact.email=new_email.strip()
            print(f"Contact '{name}' has been updated")
        else:
            print(f"Contact '{name}' not found.")
    def delete_contact(self,name):
        contact=self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact {name} has been deleted")
        else:
            print(f"Contact {name} not found.")