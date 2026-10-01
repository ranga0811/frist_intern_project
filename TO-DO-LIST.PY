# To-Do List Application

tasks = []


def add_task():
    description = input("Enter task description: ")

    task = {
        "description": description,
        "completed": False
    }

    tasks.append(task)

    print("Task added successfully!")


def view_tasks():

    if len(tasks) == 0:
        print("No tasks available.")

    else:
        print("\n========== YOUR TASKS ==========")

        for i, task in enumerate(tasks, start=1):

            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(f"{i}. {task['description']} - {status}")


def complete_task():

    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    task_number = int(input("\nEnter task number to complete: "))

    if task_number >= 1 and task_number <= len(tasks):

        tasks[task_number - 1]["completed"] = True

        print("Task marked as completed!")

    else:
        print("Invalid task number.")


# Main Program

while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")