# Password Manager Application

## Overview
This Python application is a simple password manager that allows users to securely store and manage their login credentials for various websites. The application uses the tkinter library for the graphical user interface (GUI) and leverages encryption techniques to protect sensitive data.

## Features
- **Password Generation:** The application provides a built-in password generator that can generate secure passwords for your accounts.

- **Data Encryption:** The passwords and website information are stored in an encrypted format, making it difficult for unauthorized users to access the data.

- **User-Friendly Interface:** The GUI makes it easy for users to add, view, and manage their stored passwords.

## Files
- **main.py:** This is the main script for the password manager application. It contains the code for the GUI and password management functionality. It also uses the "encryption.py" script for encryption and password generation.

- **encryption.py:** This script contains the encryption functions, including key generation, data encryption, and decryption. It also includes a password generator function for creating secure passwords.

- **logo.png** was created using bing bot :) 

## How to Use
1. Run the "main.py" script to open the application.

2. To add a new password entry, provide the following information:
   - Website URL
   - User Name
   - Password

   Click the "Generate password" button to generate a secure password, or enter your own.

3. Enter your "whatPassword" in the corresponding field. This is the main password you will use to access your stored passwords.

4. Click the "Add" button to save the new password entry. Make sure to enter all required information.

5. To view your stored passwords, click the "Show" button. You'll be prompted to enter your "whatPassword."

6. If it's your first time using the application, you'll receive a warning message to remind you to remember your "whatPassword" since it cannot be recovered.

## Security
The application uses strong encryption techniques to protect your data. It's important to remember your "whatPassword" because it is the key to accessing your stored passwords. If you forget it, you won't be able to retrieve your passwords.

## Dependencies
- Python 3.x
- tkinter (for the GUI)
- pandas
- pyperclip
- password_generator
- cryptography

## Disclaimer
This password manager is designed for personal use and should not be considered a replacement for enterprise-level password management solutions. Always use strong, unique passwords for your online accounts and keep your "whatPassword" secure.

## Author
This password manager application was created by Leon Markovich.

