import tkinter as tk
import pandas as pd
import encryption
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    cur_website=website_entry.get()
    cur_user=user_name_entry.get()
    cur_password=password_entry.get()
    if cur_website and cur_user and cur_password:
        password={'user_name':cur_user,'password':cur_password}
        encryption.encrypt_data(website=cur_website,new_password=password)
    else:
        print("you didnt enter all the information for password")

def show_passwords():
    cur_website=website_entry.get()
    if cur_website:
        print(encryption.decrypt_data())
    else:
        print("you didnt enter the website name")

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")

window.config(padx=20, pady=20)
canvas = tk.Canvas(width=220, height=189)
lock_img = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=1, column=1)

# labels
wbsite_label = tk.Label(text="Website URL: ", anchor="w", pady=5)
wbsite_label.grid(row=2, column=0, sticky="w")
user_name_label = tk.Label(text="User name: ", anchor="w", pady=5)
user_name_label.grid(row=3, column=0, sticky="w")
password_label = tk.Label(text="Password: ", anchor="w", pady=5)
password_label.grid(row=4, column=0, sticky="w")

# entrys
website_entry = tk.Entry(width=50)
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=2)
user_name_entry = tk.Entry(width=50)
user_name_entry.grid(row=3, column=1, columnspan=2)
password_entry = tk.Entry(width=25)
password_entry.grid(row=4, column=1, sticky="w", pady=5)

# buttons
generate_button = tk.Button(text="Generate password", width=19)
generate_button.grid(row=4, column=1, columnspan=2, sticky="e", pady=5)
add_button = tk.Button(text="add", width=21,command=add_password)
add_button.grid(row=5, column=1,sticky="w")
show_button = tk.Button(text="show", width=19,command=show_passwords)
show_button.grid(row=5, column=1,columnspan=2,sticky="e")

window.mainloop()
