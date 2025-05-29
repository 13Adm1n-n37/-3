import json

class TaskModel:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()