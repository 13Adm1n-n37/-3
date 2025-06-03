import unittest  
from src.model import TaskModel  # Импорт из src/  

class TestTaskModel(unittest.TestCase):  
    def test_add_task(self):  
        model = TaskModel()  
        task = {  
            "title": "Test Task",  
            "priority": "Высокий",  
            "category": "Работа",  
            "due_date": "2025-06-02",  
            "completed": False  
        }  
        model.add_task(task)  
        self.assertIn(task, model.tasks)  # Проверка добавления  

    def test_delete_task(self):  
        model = TaskModel()  
        task = {  
            "title": "Delete Task",  
            "priority": "Средний",  
            "category": "Личное",  
            "due_date": "2025-06-03",  
            "completed": True  
        }  
        model.add_task(task)  
        initial_length = len(model.tasks)  
        model.delete_task(0)  # Удаление по индексу  
        self.assertEqual(len(model.tasks), initial_length - 1)  # Проверка удаления  