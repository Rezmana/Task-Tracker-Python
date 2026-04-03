from tasks import add_task, completed_task, complete_task, get_tasks, delete_task
def main():
    print("Welcome to the Task Manager!")
    while True:
        print("1.Add Task\n")
        print("2.View Tasks\n")
        print("3.Mark Task as Completed\n")
        print("4.Mark All Tasks as Completed\n")
        print("5.Delete Task\n")
        print("6.Exit\n")
        choice = input("Enter Choice:")
        if choice == "1":
            task = input("Enter Task:")
            add_task(task)
        elif choice == "2":
            tasks = get_tasks()
            for task in tasks:
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{task['id']}. {task['title']} - {status}")
        elif choice == "3":
            task_id = int(input("Enter Task ID to Mark as Completed:"))
            complete_task(task_id)
        elif choice == "4":
            completed_task()
        elif choice == "5":
            task_id = int(input("Enter Task ID to Delete:"))
            delete_task(task_id)
        elif choice == "6":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid Choice. Please Try Again.")
if __name__ == "__main__":
    main()
    