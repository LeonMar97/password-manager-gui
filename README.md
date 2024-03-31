# Password Manager Application

## Overview
This Python application is a simple password manager that allows users to securely store and manage their login credentials for various websites. The application features a **GUI** built with **tkinter** and utilizes encryption techniques to protect sensitive data. It communicates with a **FastAPI** server acting as the backend for the package, which includes built-in **OpenAPI documentation** accessible at `localhost:8000/documentation`.

## Features
- **Password Generation:** The application provides a built-in password generator that can generate secure passwords for your accounts.
- **Data Encryption:** The passwords and website information are stored in an encrypted format, ensuring protection against unauthorized access.
- **FastAPI Backend:** Utilizes FastAPI framework to establish REST operations with built-in OpenAPI documentation for routes at `localhost:8000/documentation`.
- **User-Friendly Interface:** The GUI makes it easy for users to add, view, and manage their stored passwords.

## Files
- **main.py:** This is the main script for the password manager application. It contains the code for the GUI and password management functionality. It also utilizes the "encryption.py" script for encryption and password generation.
- **encryption.py:** This script contains the encryption functions, including key generation, data encryption, and decryption. It also includes a password generator function for creating secure passwords.
- **logo.png:** The logo for the application - > created using bing ai :) .
- **Database Class:** Defines a foundation for database operations with abstract methods for connecting to the database, registering users, adding passwords, etc.
- **GitHub Workflow (linter.yml):** Ensures linting checks are performed on pull requests targeting the main or master branches before they are merged.

## How to Use
1. **Installation:**
   - Ensure you have **Python 3.x** installed on your system.
   - Run ```poetry install``` to install dependencies using Poetry.

2. **Run the Application:**
   - Execute ```make run``` to start the GUI example.
   - To start the FastAPI backend server, run ```make run-server``` in a separate terminal.

3. **Adding Password Entry:**
   - Provide the Website URL, User Name, and Password in the corresponding fields.
   - Click the "Generate password" button to create a secure password or enter your own.
   - Enter your **whatPassword** in the corresponding field.
   - Click the "Add" button to save the new password entry.

4. **Viewing Stored Passwords:**
   - Click the "Show" button to view stored passwords.
   - Enter your **whatPassword** when prompted.

5. **Security Note:**
   - Remember your **whatPassword** as it's crucial for accessing stored passwords.
   - If forgotten, stored passwords cannot be retrieved.

## Linting and Formatting
- Use ```make lint``` to check linting issues.
- To attempt fixing linting issues, run ```make lint-fix```.

## Author
This password manager application was created by Leon Markovich.
