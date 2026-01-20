tasks = []
menu = ["add", "view", "delete", "exit"]

while True:
    # show menu
    for i, option in enumerate(menu, start=1):
        print(f"{i}. {option}")

    # add task
    choice = input("what do you want to do: ").lower()
    if choice == "add":
        while True:
            task = input("enter a task(press enter to stop): ")
            if task == "":
                break
            tasks.append(task)

        # view tasks
        print("These are your tasks: ")
        for i, a_task in enumerate(tasks, start=1):
            print(f"{i}. {a_task}")
    elif choice == "delete":
        number = int(input("Enter task number to delete: "))
        index = number-1
        tasks.pop(index)
        if number =="":
         print("you didnt select any task to delete")
        for i, index in enumerate(tasks, start=1):
            print("Here are your current tasks:"f"{i}. {index}")
    elif choice == "exit":
        exit = input("press enter to exit")
        if exit == "":
            break
    elif choice.lower() == "view":
        print("These are your tasks:")
        for i, a_task in enumerate(tasks, start=1):
            print(f"{i}. {a_task}")

