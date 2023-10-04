import tkinter as tk
import pandas as pd
import encryption
from tkinter import scrolledtext
from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    """adds password to txt file in json encrypted format as bytes"""
    cur_website = website_entry.get()
    cur_user = user_name_entry.get()
    cur_password = password_entry.get()
    cur_main_password = main_password_entry.get()
    if cur_website and cur_user and cur_password and cur_main_password:
        password = {"user_name": cur_user, "password": cur_password}
        if not encryption.encrypt_data(
            main_pass=cur_main_password, website=cur_website, new_password=password
        ):
            messagebox.showinfo("Error", "something went wrong with the encryption")
        messagebox.showinfo("Success", "password as added succesfully")
    else:
        messagebox.showinfo("Information", "you didnt enter all info")


def format_data_for_display(data):
    """reforamts json to string

    Parameters:
    data- json formated data

    Returns:
    string formated credentials"""
    formatted_text = ""
    for website, credentials in data.items():
        formatted_text += f"Website name: {website}\n"
        formatted_text += f"User name: {credentials['user_name']}\n"
        formatted_text += f"Password: {credentials['password']}\n"
        formatted_text += "\n"
    return formatted_text


def show_passwords():
    """prints passwords to another window"""
    cur_main_password = main_password_entry.get()
    if not cur_main_password:
        messagebox.showinfo("Information", "please enter myPass password.")
        return
    passwrods_window = tk.Toplevel()
    passwrods_window.title("All passwords")
    text_widget = scrolledtext.ScrolledText(passwrods_window, wrap=tk.WORD)
    decrypted_data = encryption.decrypt_data(cur_main_password)
    if decrypted_data == None:
        messagebox.showinfo("Error", "something went wrong with the decryption")
        return
    passwords_as_json = json.loads(decrypted_data.replace("'", '"'))
    formated_data = format_data_for_display(passwords_as_json)
    text_widget.insert(tk.END, formated_data)
    text_widget.pack(expand=True, fill="both")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")

window.config(padx=20, pady=20)
canvas = tk.Canvas(width=220, height=189)
lock_img = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=1)

# labels
main_password_label = tk.Label(text="myPass password: ", anchor="w", pady=5)
main_password_label.grid(row=0, column=0, sticky="w", columnspan=2)
wbsite_label = tk.Label(text="Website URL: ", anchor="w", pady=5)
wbsite_label.grid(row=2, column=0, sticky="w")
user_name_label = tk.Label(text="User name: ", anchor="w", pady=5)
user_name_label.grid(row=3, column=0, sticky="w")
password_label = tk.Label(text="Password: ", anchor="w", pady=5)
password_label.grid(row=4, column=0, sticky="w")

# entrys
main_password_entry = tk.Entry(width=20)
main_password_entry.grid(row=0, column=1)
main_password_entry.focus()
website_entry = tk.Entry(width=50)
website_entry.grid(row=2, column=1, columnspan=2)
user_name_entry = tk.Entry(width=50)
user_name_entry.grid(row=3, column=1, columnspan=2)
password_entry = tk.Entry(width=25)
password_entry.grid(row=4, column=1, sticky="w", pady=5)

# buttons
generate_button = tk.Button(text="Generate password", width=19)
generate_button.grid(row=4, column=1, columnspan=2, sticky="e", pady=5)
add_button = tk.Button(text="add", width=21, command=add_password)
add_button.grid(row=5, column=1, sticky="w")
show_button = tk.Button(text="show", width=19, command=show_passwords)
show_button.grid(row=5, column=1, columnspan=2, sticky="e")


window.mainloop()
