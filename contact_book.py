import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})

    def get_all_contacts(self):
        return self.contacts

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact["name"].lower() or query in contact["phone"]:
                results.append(contact)
        return results

    def update_contact(self, old_contact, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact == old_contact:
                self.contacts[idx] = new_contact
                return True
        return False

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            return True
        return False

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contact_book = ContactBook()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        self.add_frame = tk.Frame(self.root)
        self.add_frame.pack(pady=10)

        tk.Label(self.add_frame, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.add_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.add_frame, text="Phone").grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.add_frame)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.add_frame, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(self.add_frame)
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.add_frame, text="Address").grid(row=3, column=0)
        self.address_entry = tk.Entry(self.add_frame)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, columnspan=2, pady=10)

        self.contacts_frame = tk.Frame(self.root)
        self.contacts_frame.pack(pady=10)

        self.contacts_listbox = tk.Listbox(self.contacts_frame, width=50)
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.contacts_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.contacts_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contacts_listbox.yview)

        self.contacts_listbox.bind('<Double-1>', self.show_contact_details)

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(pady=10)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_contact)
        self.search_button.pack(side=tk.LEFT)

        self.show_all_button = tk.Button(self.search_frame, text="Show All", command=self.display_contacts)
        self.show_all_button.pack(side=tk.LEFT, padx=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            self.contact_book.add_contact(name, phone, email, address)
            self.display_contacts()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields")

    def display_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contact_book.get_all_contacts():
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def search_contact(self):
        query = self.search_entry.get()
        if query:
            results = self.contact_book.search_contact(query)
            self.contacts_listbox.delete(0, tk.END)
            for contact in results:
                self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
        else:
            messagebox.showwarning("Input Error", "Please enter a search query")

    def show_contact_details(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            contact = self.contact_book.get_all_contacts()[selected_index[0]]
            self.show_contact_dialog(contact)

    def show_contact_dialog(self, contact):
        dialog = tk.Toplevel(self.root)
        dialog.title("Contact Details")

        tk.Label(dialog, text="Name").grid(row=0, column=0)
        name_entry = tk.Entry(dialog)
        name_entry.grid(row=0, column=1)
        name_entry.insert(0, contact["name"])

        tk.Label(dialog, text="Phone").grid(row=1, column=0)
        phone_entry = tk.Entry(dialog)
        phone_entry.grid(row=1, column=1)
        phone_entry.insert(0, contact["phone"])

        tk.Label(dialog, text="Email").grid(row=2, column=0)
        email_entry = tk.Entry(dialog)
        email_entry.grid(row=2, column=1)
        email_entry.insert(0, contact["email"])

        tk.Label(dialog, text="Address").grid(row=3, column=0)
        address_entry = tk.Entry(dialog)
        address_entry.grid(row=3, column=1)
        address_entry.insert(0, contact["address"])

        def update_contact():
            new_contact = {
                "name": name_entry.get(),
                "phone": phone_entry.get(),
                "email": email_entry.get(),
                "address": address_entry.get()
            }
            self.contact_book.update_contact(contact, new_contact)
            self.display_contacts()
            dialog.destroy()

        def delete_contact():
            self.contact_book.delete_contact(contact)
            self.display_contacts()
            dialog.destroy()

        update_button = tk.Button(dialog, text="Update", command=update_contact)
        update_button.grid(row=4, column=0, pady=10)

        delete_button = tk.Button(dialog, text="Delete", command=delete_contact)
        delete_button.grid(row=4, column=1, pady=10)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()

