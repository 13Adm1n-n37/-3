import unittest  
from PyQt5.QtWidgets import QApplication  
from src.view import TaskView  
from src.controller import TaskController  
from src.model import TaskModel  

app = QApplication([])  # Инициализация QApplication  

class TestTaskView(unittest.TestCase):  
    def setUp(self):  
        self.model = TaskModel()  
        self.view = TaskView(controller=None)  
        self.controller = TaskController(self.model, self.view)  
        self.view.controller = self.controller  # Связь контроллера и представления  

    def test_filter_tasks(self):  
        # Добавление тестовых задач  
        task1 = {"title": "Task1", "completed": True}  
        task2 = {"title": "Task2", "completed": False}  
        self.model.add_task(task1)  
        self.model.add_task(task2)  

        # Установка фильтра "Выполненные"  
        self.view.filter_combo.setCurrentText("Выполненные")  
        self.view.filter_tasks()  # Вызов метода фильтрации  
        self.assertEqual(self.view.task_list.count(), 1)  # Ожидается 1 задача  