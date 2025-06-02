import unittest  
from unittest.mock import MagicMock  
from src.controller import TaskController  
from src.model import TaskModel  

class TestTaskController(unittest.TestCase):  
    def setUp(self):  
        self.model = TaskModel()  
        self.view = MagicMock()  # Мок-объект для представления  
        self.controller = TaskController(self.model, self.view)  

    def test_add_task_updates_view(self):  
        task = {  
            "title": "Integration Test",  
            "priority": "Низкий",  
            "category": "Обучение",  
            "due_date": "2025-06-04",  
            "completed": False  
        }  
        self.controller.add_task(task)  
        self.view.update_task_list.assert_called_once()  # Проверка вызова обновления списка  

    def test_delete_task(self):  
        self.model.add_task({"title": "Test Task"})  
        self.controller.delete_task(0)  # Удаление через контроллер  
        self.assertEqual(len(self.model.tasks), 0)  # Проверка удаления в модели  