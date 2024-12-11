
'''
To-Do List
Author: Zachary Watson
Date: 12/2/2024 - 12/11/2024
Description: A To-Do list with various functions such as the ability to store multiple items, print currently stored
items, remove stored items, and clear the list. Also features the ability to save/load data.
'''
from examples import myList

# Variables
to_do_list = []
# File name
fName = "data.txt"

def save_to_file():
    """Saves the current to-do list to a file."""
    with open(fName, "w") as file:
        for item in to_do_list:
            file.write(item + "\n")


def load_from_file():
    """Loads the to-do list from a file."""
    try:
        with open(fName, "r") as file:
            for line in file:
                to_do_list.append(line.strip())
    except FileNotFoundError:
        # Handles error with no previous data.txt file
        print("No previous data found. Starting with an empty list.")

def add_item(item):

    to_do_list.append(item)
    print(f'Item "{item}" has been added to the list.')

def remove_item():
    if not to_do_list: 
        print("The list is currently empty.")
        return

    print("\nCurrent To-Do List:")
    # Starts the list at one, and basically assigns the number 1 to task1 etc...
    for i, task in enumerate(to_do_list, start=1):
        print(f"{i}. {task}")

    choice = input("\nEnter the number of the task to remove or 'q' to cancel: ")
    if choice.lower() == 'q':
        print("Canceled.")
        return
# Handles numeric numbers
    if choice.isdigit():
        index = int(choice) - 1
        # Counts the number of items in the list
        if 0 <= index < len(to_do_list):
            removed = to_do_list.pop(index)
            print(f'Item "{removed}" has been removed from the list.')
        else:
            print("Invalid task number.")
    else:
        print("Invalid input. Please enter a valid task number.")

def reset_list():
    # Clears the list
    to_do_list.clear()
    print("The list has been cleared.")

def print_list():
    # Handles situation where the list is empty
    if not to_do_list:
        print("The list is currently empty.")
    # Starts the list at one, and prints whatever tasks are currently in the list with 1 = task1 etc...
    else:
        print("\nCurrent To-Do List:")
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")

def show_menu():
    '''Has no parameter and returns nothing. Used to display the options that the user can select.'''
    print("\nTo-Do List Menu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Print List")
    print("4. Reset List")
    print("5. Quit")
    return input("Enter your choice (1-5): ")



def main():
    # Takes in inputs & repeatedly displays the menu after each action
    print("Welcome to the To-Do List")
    while True:
        choice = show_menu()
        if choice == '1':
            task = input("Enter a task to add: ")
            add_item(task)
        elif choice == '2':
            remove_item()
        elif choice == '3':
            print_list()
        elif choice == '4':
            reset_list()
        elif choice == '5':
            print("Goodbye!")
            break
        # Handles situations where an unlisted number is inputted
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")





if __name__ == "__main__":
    main()
