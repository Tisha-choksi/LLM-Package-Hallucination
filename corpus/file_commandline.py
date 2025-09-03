import commands

def show_tasks():
    tasks = commands.getoutput('cat todo.txt')  # Assumes a todo.txt file exists
    print("Current To-Do List:")
    print(tasks)

def add_task(task):
    with open('todo.txt', 'a') as f:
        f.write(f"{task}\n")

if __name__ == "__main__":
    while True:
        action = input("Enter 'add' to add a task, 'show' to view tasks, or 'exit' to quit: ")
        if action == 'add':
            task = input("Enter the task: ")
            add_task(task)
        elif action == 'show':
            show_tasks()
        elif action == 'exit':
            break
        else:
            print("Invalid action.")
