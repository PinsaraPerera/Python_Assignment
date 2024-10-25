
class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class TaskManager:
    def __init__(self):
        self.queue = []

    def add_task(self, title, description, status):
        task = Task(title, description, status)
        self.queue.append(task)

    def get_task_by_status(self, status = "Pending"):
        tasks = []
        for task in self.queue:
            if task.status == status:
                tasks.append(task)
        return tasks
    
    def get_task_by_title(self, title):
        for task in self.queue:
            if task.title == title:
                return task
        return None

    def change_task_status(self, title, status = "Completed"):
        task = self.get_task_by_title(title)
        if task:
            task.status = status
        else:
            print(f"Task with title {title} not found")

    def store_task_in_csv(self):
        with open("tasks.csv", "a") as file:
            for task in self.queue:
                file.write(f"{task.title},{task.description},{task.status}\n")


# Initialize the Task Manager by creating a new object manager
manager = TaskManager()

# Add tasks to the Task queue
manager.add_task("Task 1", "Need to complete python assignment", "Completed")
manager.add_task("Task 2", "Go to grocery store", "Pending")
manager.add_task("Task 3", "Watch new Imax movie Lord of the Rings: Kings Return", "Pending")
manager.add_task("Task 4", "prepare for the interview with Google", "Pending")
manager.add_task("Task 5", "Go to the gym", "Completed")

# Get all the tasks with status "Pending"
pending_tasks = manager.get_task_by_status("Pending")

# Print all the pending tasks
print("\nPending Tasks\n")
for pending_task in pending_tasks:
    print(f"{pending_task.title} - {pending_task.description} - {pending_task.status}")

# Change the status of Task 2 to "Completed"
manager.change_task_status("Task 2", "Completed")
print(f"\nStatus of Task 2 : {[task.status for task in manager.queue if task.title == 'Task 2'][0]}")


# Store all the tasks in a CSV file
manager.store_task_in_csv()
