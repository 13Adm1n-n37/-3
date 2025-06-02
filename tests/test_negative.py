import unittest  
from src.controller import TaskController  
from src.model import TaskModel  

class TestNegativeScenarios(unittest.TestCase):  
    def setUp(self):  
        self.model = TaskModel()  
        self.view = MagicMock()  
        self.controller = TaskController(self.model, self.view)  

    def test_add_empty_task(self):  
        task = {  
            "title": "",  # Пустое название  
            "priority": "Высокий",  
            "category": "Работа",  
            "due_date": "2025-06-05",  
            "completed": False  
        }  
        self.controller.add_task(task)  # Ожидается игнорирование/ошибка  
        self.assertEqual(len(self.model.tasks), 0)  # Нет добавления задачи  