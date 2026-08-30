class TodoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, priority="Low"):
        if priority not in ["High", "Medium", "Low"]:
            raise ValueError("Invalid priority")
        task = {
            "id": self.next_id,
            "title": title,
            "priority": priority
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        tasks = sorted(self.tasks, key=lambda x: ("High", "Medium", "Low").index(x["priority"]))
        return tasks

    def remove_task(self, task_id):
        if task_id in [task["id"] for task in self.tasks]:
            self.tasks = [task for task in self.tasks if task["id"] != task_id]
            return True
        else:
            return False

if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Buy groceries")
    todo.add_task("Write research paper")
    
    print("Current Tasks:")
    for t in todo.list_tasks():
        print(f"[{t['id']}] {t['title']}")
