class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)
        self.update_task_list()

    def update_task_list(self):
        self.view.task_list.clear()
        for task in self.model.tasks:
            text = f"{task['title']} | {task['priority']} | {task['category']} | {task['due_date']}"
            self.view.task_list.addItem(text)