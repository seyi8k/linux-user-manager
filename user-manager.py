import subprocess
import sys
import os

COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_END = "\033[0m" 

def print_message(message, color=COLOR_END):
    print(f"{color}{message}{COLOR_END}")

def check_root():
    if os.geteuid() != 0:
        print_message("This script must be run with root privileges.", COLOR_RED)
        sys.exit(1) 

def user_exists(username):
    print_message(f"Checking if user '{username}' exists...", COLOR_YELLOW)
    try:
        result = subprocess.run(
            ["id", username],
            capture_output=True,
            text=True,
            check=False 
        )
        if result.returncode == 0:
            print_message(f"User '{username}' found.", COLOR_GREEN)
            return True
        else:
            print_message(f"User '{username}' not found.", COLOR_YELLOW)
            return False
    except FileNotFoundError:
        print_message("Error: 'id' command not found. Is it in your PATH?", COLOR_RED)
        return False
    except Exception as e:
        print_message(f"An unexpected error occurred while checking user: {e}", COLOR_RED)
        return False

def add_user(username):
    if user_exists(username):
        print_message(f"User '{username}' already exists. Skipping addition.", COLOR_YELLOW)
        return

    print_message(f"Attempting to add user: {username}...", COLOR_YELLOW)
    try:
        result = subprocess.run(
            ["useradd", "-m", username],
            capture_output=True,
            text=True,
            check=True
        )
        print_message(f"User '{username}' added successfully.", COLOR_GREEN)
        print_message("Remember to set a password for the new user using 'sudo passwd {}'".format(username), COLOR_YELLOW)
    except subprocess.CalledProcessError as e:
        print_message(f"Failed to add user '{username}'. Error: {e.stderr.strip()}", COLOR_RED)
    except FileNotFoundError:
        print_message("Error: 'useradd' command not found. Is it in your PATH?", COLOR_RED)
    except Exception as e:
        print_message(f"An unexpected error occurred while adding user: {e}", COLOR_RED)

def delete_user(username):
    if not user_exists(username):
        print_message(f"User '{username}' does not exist. Skipping deletion.", COLOR_YELLOW)
        return

    print_message(f"Attempting to delete user: {username}...", COLOR_YELLOW)
    try:
        result = subprocess.run(
            ["userdel", "-r", username],
            capture_output=True,
            text=True,
            check=True
        )
        print_message(f"User '{username}' deleted successfully.", COLOR_GREEN)
    except subprocess.CalledProcessError as e:
        print_message(f"Failed to delete user '{username}'. Error: {e.stderr.strip()}", COLOR_RED)
    except FileNotFoundError:
        print_message("Error: 'userdel' command not found. Is it in your PATH?", COLOR_RED)
    except Exception as e:
        print_message(f"An unexpected error occurred while deleting user: {e}", COLOR_RED)



def main():
    """Main function to run the user management script."""
    check_root()

    while True:
        print("\n--- User Management Menu ---")
        print("1. Add a user")
        print("2. Delete a user")
        print("3. Check if user exists")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            username = input("Enter the username to add: ")
            add_user(username)
        elif choice == '2':
            username = input("Enter the username to delete: ")
            delete_user(username)
        elif choice == '3':
            username = input("Enter the username to check: ")
            if user_exists(username):
                print_message(f"User '{username}' exists on the system.", COLOR_GREEN)
            else:
                print_message(f"User '{username}' does NOT exist on the system.", COLOR_YELLOW)
        elif choice == '4':
            print_message("Exiting script. Goodbye!", COLOR_GREEN)
            break
        else:
            print_message("Invalid choice. Please enter a number between 1 and 4.", COLOR_RED)

if __name__ == "__main__":
    main()