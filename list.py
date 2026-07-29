def add_task(task):
    tasks["pending"].append(task)
    print(f"Task '{task}' added.")

def view_list():
    print("Pending tasks:")
    for task in tasks["pending"]:
        print(f"- {task}")
    print("Done tasks:")
    for task in tasks["done"]:
        print(f"- {task}")

def mark_task_done(task):
    if task in tasks["pending"]:
        tasks["pending"].remove(task)
        tasks["done"].append(task)
        print(f"Task '{task}' marked as done.")
    else:
        print(f"Task '{task}' not found in pending tasks.")

def remove_task(task):
    if task in tasks["pending"]:
        tasks["pending"].remove(task)
        print(f"Task '{task}' removed from pending tasks.")
    elif task in tasks["done"]:
        tasks["done"].remove(task)
        print(f"Task '{task}' removed from done tasks.")
    else:
        print(f"Task '{task}' not found in the list.")


def quit():
    print("Exiting the task manager. Goodbye!")
    exit()



actions=['a', 'm', 'r', 'v', 'q']

done_tasks = []
pending_tasks = []

tasks = {"pending": pending_tasks,
        "done": done_tasks} #create a dictionary to store tasks

file_path= "tasks.txt"
try:
    with open(file_path, "r") as file: # open the file in read mode
        lines = file.readlines()
        current_section = None
        for line in lines:
            line = line.strip()
            if line == "Pending tasks:":
                current_section = "pending"
            elif line == "Done tasks:":
                current_section = "done"
            elif line.startswith("-"):
                task = line[2:]  # Remove the "- " prefix
                if current_section == "pending":
                    tasks["pending"].append(task)
                elif current_section == "done":
                    tasks["done"].append(task)
except FileNotFoundError:
    file = open(file_path, "w") # create the file if it doesn't exist

print("LIGHTNING MCQUEEN'S TO-DO LIST")
print("\nWelcome to Lightning McQueen's To-Do List! ")

while True:
    print("\nChoose the action you want to perform: (a)dd,(m)ark a task done, (r)emove, (v)iew, (q)uit")
    action = input("Enter your choice: ")
    action = action.lower() # in case user enters uppercase letters
    if action == 'a':
        task = input("Enter the task to add: ")
        add_task(task)
    elif action == 'm':
        task = input("Enter the task to mark as done: ")
        mark_task_done(task)
    elif action == 'r':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif action == 'v':
        view_list()
    elif action == 'q':
        quit()
    else:
        print("Invalid choice. Please try again.")
    with open("tasks.txt", "w") as file:
        file.write("Pending tasks:\n") # write the tasks to the file
        for task in tasks["pending"]:
            file.write(f"- {task}\n")
        file.write("Done tasks:\n")
        for task in tasks["done"]:
            file.write(f"- {task}\n")