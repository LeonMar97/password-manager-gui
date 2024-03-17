import tkinter as tk
import pandas as pd
import encryption
from tkinter import scrolledtext
from tkinter import messagebox
import json
import pyperclip as pc
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genrate_secure_password():
    '''genrate secure password, past in entry and copies it to clipboard'''
    password_entry.delete(0,tk.END)
    pw=encryption.password_generator()
    password_entry.insert(tk.END,pw)
    pc.copy(pw)

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
            messagebox.showerror("Error", "something went wrong with the encryption")
        else:
            messagebox.showinfo("Success", "password as added succesfully")
    else:
        messagebox.showerror("Information", "you didnt enter all info")

def check_first_time():
    '''checks if its first time adding password to txt file, to print out warning message'''
    try:
        with open(file="passwords/encrypted-passwords.txt", mode="rb") as f:
            if not f.read():
                messagebox.showwarning("info", "hello and welcome to whatPassword ,\
please create first password at top. this is the only password you will need to remmember :) \
but you cant recover it, DONT FORGET IT !")
                global check_first_flag
                check_first_flag=True
    except OSError as e:
        messagebox.showerror("error !!!","file 'passwords/encrypted-passwords.txt',\
not found, please make sure there is a 'passwords' folder with 'encrypted-passwords.txt'\
 in it" )
        exit()

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
        messagebox.showerror("Information", "please enter whatPassword  password.")
        return
    
    decrypted_data = encryption.decrypt_data(cur_main_password)
    if decrypted_data == None:
        messagebox.showerror("Error", "whatPassword  password is incorrect")
        return
    else:
        passwrods_window = tk.Toplevel()
        passwrods_window.title("All passwords")
        text_widget = scrolledtext.ScrolledText(passwrods_window, wrap=tk.WORD)
        passwords_as_json = json.loads(decrypted_data.replace("'", '"'))
        formated_data = format_data_for_display(passwords_as_json)
        text_widget.insert(tk.END, formated_data)
        text_widget.pack(expand=True, fill="both")


# ---------------------------- UI SETUP ------------------------------- #
check_first_flag=False
window = tk.Tk()

window.title("Password Manager")

window.config(padx=20, pady=20)
canvas = tk.Canvas(width=220, height=189)
lock_img = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=1)

# labels
main_password_label = tk.Label(text="whatPassword  password: ", anchor="w", pady=5)
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
# main_password_entry.focus()
website_entry = tk.Entry(width=50)
website_entry.grid(row=2, column=1, columnspan=2)
user_name_entry = tk.Entry(width=50)
user_name_entry.grid(row=3, column=1, columnspan=2)
password_entry = tk.Entry(width=25)
password_entry.grid(row=4, column=1, sticky="w", pady=5)

# buttons
generate_button = tk.Button(text="Generate password", width=19,command=genrate_secure_password)
generate_button.grid(row=4, column=1, columnspan=2, sticky="e", pady=5)
add_button = tk.Button(text="add", width=21, command=add_password)
add_button.grid(row=5, column=1, sticky="w")
show_button = tk.Button(text="show", width=19, command=show_passwords)
show_button.grid(row=5, column=1, columnspan=2, sticky="e")
main_password_entry.focus()
if not check_first_flag:
    check_first_time()
    main_password_entry.focus_force()
window.mainloop()
