import sys
sys.path.append("src")

from PyQt5.QtCore import QDate
import unittest
from PyQt5.QtWidgets import QApplication
from src.view import TaskView
from src.controller import TaskController
from src.model import TaskModel
import os

app = QApplication(sys.argv) 

class TestNegativeScenarios(unittest.TestCase):
    def setUp(self):
        # Удаляем файл tasks.json перед каждым тестом, чтобы начать с чистой модели
        try:
            os.remove("src/tasks.json")
        except FileNotFoundError:
            pass
        self.model = TaskModel()
        self.view = TaskView(controller=None)
        self.controller = TaskController(self.model, self.view)
        self.view.controller = self.controller

    def test_add_task_empty_title(self):
        """Проверка добавления задачи с пустым названием (тест под текущую логику)"""
        self.view.title_input.setText("")
        self.view.priority_combo.setCurrentText("Средний")
        self.view.category_combo.setCurrentText("Работа")
        self.view.due_date.setDate(QDate.currentDate())
        self.view.completed_checkbox.setChecked(False)
        
        initial_count = len(self.model.tasks)
        self.view.add_task()
        
        # Проверяем, что задача всё же добавлена (соответствует текущей логике)
        self.assertEqual(len(self.model.tasks), initial_count + 1)
        new_task = self.model.tasks[-1]
        self.assertEqual(new_task["title"], "")  # Проверяем, что title пустой

    def test_add_task_missing_priority(self):
        """Проверка добавления задачи без приоритета (тест под текущую логику)"""
        self.view.title_input.setText("Тестовая задача")
        self.view.priority_combo.clear()  # Удаляем варианты приоритета
        self.view.category_combo.setCurrentText("Работа")
        self.view.due_date.setDate(QDate.currentDate())
        self.view.completed_checkbox.setChecked(False)
        
        initial_count = len(self.model.tasks)
        self.view.add_task()
        
        # Проверяем, что задача всё же добавлена
        self.assertEqual(len(self.model.tasks), initial_count + 1)
        new_task = self.model.tasks[-1]
        self.assertEqual(new_task["priority"], "")  # Приоритет пустой

if __name__ == "__main__":
    unittest.main()