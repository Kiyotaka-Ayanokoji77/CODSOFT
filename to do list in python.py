# To-Do List Program

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append({"task": task, "status": "pending"})
        print(f"Task '{task}' added!")

    def view_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['task']} ({task['status']})")

    def update_task(self):
        task_num = int(input("Enter the task number to update: "))
        if task_num > 0 and task_num <= len(self.tasks):
            task = self.tasks[task_num - 1]
            print(f"Current task: {task['task']} ({task['status']})")
            new_task = input("Enter the new task: ")
            new_status = input("Enter the new status (pending/done): ")
            task["task"] = new_task
            task["status"] = new_status
            print(f"Task {task_num} updated!")
        else:
            print("Invalid task number!")

    def delete_task(self):
        task_num = int(input("Enter the task number to delete: "))
        if task_num > 0 and task_num <= len(self.tasks):
            del self.tasks[task_num - 1]
            print(f"Task {task_num} deleted!")
        else:
            print("Invalid task number!")

    def mark_done(self):
        task_num = int(input("Enter the task number to mark as done: "))
        if task_num > 0 and task_num <= len(self.tasks):
            task = self.tasks[task_num - 1]
            task["status"] = "done"
            print(f"Task {task_num} marked as done!")
        else:
            print("Invalid task number!")

def main():
    todo_list = ToDoList()
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            todo_list.mark_done()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
