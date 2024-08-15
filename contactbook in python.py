import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = {}

        # Create frames
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack(fill="x", pady=5)
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(fill="x", pady=5)
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack(fill="x", pady=5)

        # Create labels and entries for adding a contact
        self.name_label = tk.Label(self.frame1, text="Name:")
        self.name_label.pack(side="left", padx=5)
        self.name_entry = tk.Entry(self.frame1, width=20)
        self.name_entry.pack(side="left", padx=5)
        
        self.phone_label = tk.Label(self.frame1, text="Phone:")
        self.phone_label.pack(side="left", padx=5)
        self.phone_entry = tk.Entry(self.frame1, width=20)
        self.phone_entry.pack(side="left", padx=5)
        
        self.email_label = tk.Label(self.frame1, text="Email:")
        self.email_label.pack(side="left", padx=5)
        self.email_entry = tk.Entry(self.frame1, width=20)
        self.email_entry.pack(side="left", padx=5)
        
        self.address_label = tk.Label(self.frame1, text="Address:")
        self.address_label.pack(side="left", padx=5)
        self.address_entry = tk.Entry(self.frame1, width=20)
        self.address_entry.pack(side="left", padx=5)

        # Create buttons
        self.add_button = tk.Button(self.frame2, text="Add Contact", command=self.add_contact)
        self.add_button.pack(side="left", padx=5)
        
        self.view_button = tk.Button(self.frame2, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(side="left", padx=5)
        
        self.search_button = tk.Button(self.frame2, text="Search Contact", command=self.search_contact)
        self.search_button.pack(side="left", padx=5)
        
        self.update_button = tk.Button(self.frame2, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side="left", padx=5)
        
        self.delete_button = tk.Button(self.frame2, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side="left", padx=5)

        # Create listbox for displaying contacts
        self.listbox = tk.Listbox(self.frame3, width=80, height=10)
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            self.listbox.insert(tk.END, f"{name} - {phone}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        self.listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.listbox.insert(tk.END, f"{name} - {details['phone']}")

    def search_contact(self):
        search_term = self.name_entry.get()
        if search_term:
            self.listbox.delete(0, tk.END)
            found = False
            for name, details in self.contacts.items():
                if search_term.lower() in name.lower() or search_term in details["phone"]:
                    self.listbox.insert(tk.END, f"{name} - {details['phone']}")
                    found = True
            if not found:
                messagebox.showinfo("Search Result", "Contact not found.")
        else:
            messagebox.showerror("Error", "Please enter a search term.")

    def update_contact(self):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            name, phone = selected_contact.split(" - ")
            new_name = self.name_entry.get()
            new_phone = self.phone_entry.get()
            new_email = self.email_entry.get()
            new_address = self.address_entry.get()
            if new_name and new_phone:
                del self.contacts[name]
                self.contacts[new_name] = {"phone": new_phone, "email": new_email, "address": new_address}
                self.view_contacts()
                messagebox.showinfo("Update Result", "Contact updated successfully.")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Please enter name and phone number.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            name, phone = selected_contact.split(" - ")
            del self.contacts[name]
            self.view_contacts()
            messagebox.showinfo("Delete Result", "Contact deleted successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def on_select(self, event):
        selected_contact = self.get_selected_contact()
        if selected_contact:
            name, phone = selected_contact.split(" - ")
            details = self.contacts[name]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, phone)
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, details["email"])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, details["address"])

    def get_selected_contact(self):
        try:
            index = self.listbox.curselection()[0]
            return self.listbox.get(index)
        except IndexError:
            return None

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
