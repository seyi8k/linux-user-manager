# Linux User Manager

A simple command-line tool built with Python for basic Linux user management. This script allows you to add, delete, and check for the existence of users on your Linux system through an interactive menu.

## Features

- **Add User**: Create a new Linux user account.
- **Delete User**: Remove an existing Linux user account, including their home directory.
- **Check User Existence**: Verify if a specific user account already exists on the system.
- **Root Privilege Check**: Ensures the script is run with necessary root permissions.
- **Interactive Menu**: Provides an easy-to-use menu for performing user operations.
- **Colored Output**: Enhances readability with colored messages for success, warnings, and errors.

## Requirements

- Linux OS
- Python 3
- Root privileges (for adding and deleting users)

## Installation Steps

1.  **Clone the repository:**
    git clone https://github.com/seyi8k/linux-user-manager.git

2.  **Navigate to the project directory:**
    cd linux-user-manager

3.  **Make the script executable:**
    chmod +x user-manager.py

## Usage

To run the user management script, you must execute it with root privileges:
**sudo python3 user-manager.py**

Once executed, an interactive menu will appear:

--- User Management Menu ---
1. Add a user
2. Delete a user
3. Check if user exists
4. Exit
Enter your choice (1-4):
Follow the prompts to perform the desired user management operation.

**Important Notes:**
**When adding a new user, remember to set a password for your new user after creation using the passwd command: sudo passwd (new user)**

# Contributions
Please feel free to fork the repository, open issues, or submit pull requests to improve this project.