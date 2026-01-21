tasks = []
menu = ["add", "view", "delete", "exit"]


def showTasks():
    if not tasks:
        print("no tasks yet \n")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


while True:
    # show menu
    print("This is your to-do app \n menu: ")
    for option in menu:
        print(f"- {option}")
    choice = input("what do you want to do: ").strip().lower()
    # add tasks

    if choice == "add":
        while True:
            task = input("input a task(press enter to stop): ")
            if task == "":
                break
            tasks.append(task)
    elif choice == "view":
        showTasks()

    elif choice == "delete":
        showTasks()
        if not tasks:
            continue

        num = input("input task number to delete: ")
        if not num.isdigit():
            print("invalid number")
            continue

        index = int(num)-1
        if index < 0 or index > len(tasks):
            print("task number is out of range")
            continue
        tasks.pop(index)
        print("task number ", num, " was deleted")

    elif choice == "exit":
        print("Good, go touch grass")
        break
