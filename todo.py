tasks = []

while True:
    print("List Homework")
    print("1. Enter a task")
    print("2. Delete a task by index")
    print("3. Remove the last task")
    print("4. Sort the list")
    print("5. Print the list")
    print("6. Exit the app")

    choice = input("Choose an option: ")

    if choice == "1":
        while True:
            task = input("Enter a task (-1 to go back): ")

            if task == "-1":
                break

            tasks.append(task)
            print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available!")
        else:
            print(tasks)
            position = int(input("Enter the index to delete: "))

            if 0 <= position < len(tasks):
                tasks.pop(position)
                print("Task deleted successfully!")
                print(tasks)
            else:
                print("Invalid index!")

    elif choice == "3":
        if tasks:
            tasks.pop()
            print(tasks)
        else:
            print("No tasks available!")

    elif choice == "4":
        tasks.sort()
        print(tasks)

    elif choice == "5":
        print(tasks)

    elif choice == "6":
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid option! Please choose 1-6.") 