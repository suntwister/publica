# 2, 13, 17

# @title 2. To-Do List Application

my_task = {
    "Task": [],
    "Mark": []

}

def add_task(task):
    my_task["Task"].append(task)
    my_task["Mark"].append(" ")
    print(f"your new task '{task}' is added successfuly\n")
    print(my_task)


def rem_task(task):
    if task in my_task["Task"]:
        index = my_task["Task"].index(task)
        my_task["Task"].pop(index)
        my_task["Mark"].pop(index)
        print(f"Task '{task}' is remove successfuly\n")
    else:
        print("Task not in list.\n")


def mark_task(task):
    if task in my_task["Task"]:
        index = my_task["Task"].index(task)
        my_task["Mark"][index] = "-"
        print(f"Task '{task}' marked as succesfuly\n")
    else:
        print("Task not in list.\n")

def open_tasks():
    print("\nThis is your To-Do List:")
    print('--' * 20)
    for i, task in enumerate(my_task["Task"]):
        print(f"{i+1}.\t[{my_task['Mark'][i]}]\t{task}")
    print('--' * 20)


        
print('--' * 20)
print("Welcome to To-Do List Application")
print('--' * 20)
while True:
    choice = int(input(f"What will you like to perform (select from 1,2 and 3)\n\t1. Add Task\n\t2. Remove Task\n\t3. Mark Task \n "))
    if choice == 1:
        user_task = input("Which task will you like to add: ")
        add_task(user_task)
    elif choice == 2:
        user_task = input("Which task will you like to remove: ")
        rem_task(user_task)
    elif choice == 3:
        user_task = input("Enter task to mark: ")
        mark_task(user_task)
    elif choice == "4":
        open_tasks()
    else:
        print("Invalid choice. Try again.\n")
        break
    open_tasks()
    choice_2 = input("will you like to perform another operation (y/n): ").lower()
    if choice_2 !="y":
        break
    else:
        continue