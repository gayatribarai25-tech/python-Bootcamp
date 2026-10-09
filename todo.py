tasks = []

while True:
    print("List Homework")
    print("1. enter a task")
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
elif            


   