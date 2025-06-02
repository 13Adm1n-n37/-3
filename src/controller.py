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
            status = "✅" if task["completed"] else "❌"
            text = f"{status} {task['title']} | {task['priority']} | {task['category']} | {task['due_date']}"
            self.view.task_list.addItem(text)
            
    def delete_task(self, index):
        self.model.delete_task(index)
        self.update_task_list()