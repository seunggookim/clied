import os

# Initialize an empty to-do list
todo_list = []

def display_menu():
    """Displays the main menu options."""
    print("\n--- To-Do List Manager ---")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Save To-Do List")
    print("5. Load To-Do List")
    print("6. Exit")

def view_todo_list():
    """Displays the current to-do list."""
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    """Adds a new task to the to-do list."""
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task():
    """Removes a task from the to-do list."""
    view_todo_list()
    try:
        task_number = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def save_todo_list(filename="todo_list.txt"):
    """Saves the to-do list to a file."""
    with open(filename, 'w') as file:
        for task in todo_list:
            file.write(f"{task}\n")
    print(f"To-Do list saved to {filename}.")

def load_todo_list(filename="todo_list.txt"):
    """Loads the to-do list from a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            global todo_list
            todo_list = [line.strip() for line in file]
        print(f"To-Do list loaded from {filename}.")
    else:
        print(f"No saved to-do list found in {filename}.")

def main():
    """Main function to run the To-Do List Manager."""
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            save_todo_list()
        elif choice == '5':
            load_todo_list()
        elif choice == '6':
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
