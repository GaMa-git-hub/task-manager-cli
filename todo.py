# todo.py

# List to store tasks
tasks = []

# Function to add a task
def add_task(description):
    task = {'description': description, 'status': '❌ Incomplete'}
    tasks.append(task)
    print(f"✅ Task '{description}' added!")

# Function to view all tasks
def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['description']} - {task['status']}")

# Function to mark a task as complete
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['status'] = '✅ Complete'
        print(f"🎉 Task '{tasks[task_index]['description']}' marked as complete!")
    else:
        print("⚠️ Invalid task index.")

# Function to delete a task
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        print(f"🗑️ Task '{tasks[task_index]['description']}' deleted!")
        tasks.pop(task_index)
    else:
        print("⚠️ Invalid task index.")

# Menu
def show_menu():
    print("\n-- 📋 To-Do List App --")
    print("1️⃣ Add Task")
    print("2️⃣ View Tasks")
    print("3️⃣ Mark Task Complete")
    print("4️⃣ Delete Task")
    print("5️⃣ Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to mark as complete: ")) - 1
            complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter task number to delete: ")) - 1
            delete_task(task_index)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
