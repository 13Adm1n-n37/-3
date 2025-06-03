import sys
sys.path.append("src")

import unittest
from PyQt5.QtWidgets import QApplication
from src.view import TaskView
from src.controller import TaskController
from src.model import TaskModel

app = QApplication(sys.argv) 

class TestTaskView(unittest.TestCase):
    def setUp(self):
        self.model = TaskModel()
        self.view = TaskView(controller=None)
        self.controller = TaskController(self.model, self.view)  # Реальный контроллер
        self.view.controller = self.controller

    def test_delete_task(self):
        """Тест удаления задачи по индексу"""
        test_task = {
            "title": "Удалить",
            "priority": "Средний",
            "category": "Работа",
            "due_date": "2025-01-01",
            "completed": False
        }
        self.model.tasks = [test_task]
        
        # Обновляем список
        self.controller.update_task_list()  
        self.assertEqual(self.view.task_list.count(), 1)  # Проверяем заполнение
        
        # Выбираем и удаляем
        self.view.task_list.setCurrentRow(0)
        self.view.delete_task()
        
        # Проверяем результат
        self.assertEqual(len(self.model.tasks), 0)  # Модель пуста
        self.assertEqual(self.view.task_list.count(), 0)  # Список пуст

    def test_edit_task(self):
        """Тест редактирования задачи"""
        original_task = {
            "title": "Старое название",
            "priority": "Средний",
            "category": "Работа",
            "due_date": "2025-01-01",
            "completed": False
        }
        self.model.tasks = [original_task]
        
        # Обновляем список
        self.controller.update_task_list()  
        self.assertEqual(self.view.task_list.count(), 1)  # Проверяем заполнение
        
        # Выбираем и редактируем
        self.view.task_list.setCurrentRow(0)
        self.view.edit_task()  # Заполняет поля формы
        
        # Меняем данные и сохраняем
        self.view.title_input.setText("Новое название")
        self.view.priority_combo.setCurrentText("Низкий")
        self.view.add_task()  # Сохраняем
        
        # Проверяем результат
        self.assertEqual(len(self.model.tasks), 1)  # Осталась одна задача
        new_task = self.model.tasks[0]
        self.assertEqual(new_task["title"], "Новое название")
        self.assertEqual(new_task["priority"], "Низкий")
        self.assertEqual(self.view.task_list.count(), 1)  # Список обновлен

if __name__ == "__main__":
    unittest.main()