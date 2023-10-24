# TO-DO LIST

tasks = {}

while True:
    # displaying the menu
    print("\nMenu:")
    print("1. Add an task")
    print("2. Update an task")
    print("3. Delete an task ")
    print("4. View all task")
    print("5. Exit")
    print()

    # get the user's choice
    choice = int(input("Enter the choice:\n"))
    print()

    # for adding a task

    if choice == 1:
        task_id = input("Enter task ID: ")
        task_title = input("Enter title of task: ")
        description = input("Enter task description: ")
        deadline = input("Enter deadline: ")
        tasks[task_id] = {"Task title": task_title,
                          "Description": description, "deadline": deadline}

    # for updating a task

    elif choice == 2:
        task_id = input("Enter task ID: ")
        if task_id in tasks:
            task_title = input("Enter title of task: ")
            description = input("Enter task description: ")
            deadline = input("Enter deadline: ")
            tasks[task_id] = {"Task title": task_title,
                              "Description": description, "Deadline": deadline}

        else:
            print("ID is not found")  # if the task id does not exist

    # for deleting a task

    elif choice == 3:
        task_id = input("Enter task ID: ")
        if task_id in tasks:
            del tasks[task_id]
        else:
            print("ID not found")

    # to get the track all the tasks

    elif choice == 4:
        if tasks:
            for task_id, j in tasks.items():
                print(f"Task ID: {task_id}")
                print(f"Description: {j['Description']}")
                print(f"Task Title: {j['Task title']}")
                print(f"Deadline: {j['deadline']}\n")
        else:
            print("No task found")

    # to exit the appllication
    elif choice == 5:
        print("Exits Application.\n")
        break

    else:
        print("Enter appropriate info")
