import unittest
from unittest.mock import MagicMock, PropertyMock
from src.controller import TaskController  

class TestTaskController(unittest.TestCase):
    def setUp(self):
        self.model_mock = MagicMock()
        self.view_mock = MagicMock()
        self.controller = TaskController(self.model_mock, self.view_mock)

        # Настройка модели: tasks должен возвращать список задач
        type(self.model_mock).tasks = PropertyMock(return_value=[])  

    def test_add_task(self):
        task = {
            "title": "Test Task",
            "priority": "Высокий",
            "category": "Работа",
            "due_date": "2025-06-02",
            "completed": False
        }

        # Настройка модели: имитируем, что задача добавлена
        self.model_mock.add_task.return_value = None  
        # Указываем, что после добавления tasks содержит новую задачу
        type(self.model_mock).tasks = PropertyMock(return_value=[task])  

        self.controller.add_task(task)
        
        # Проверяем, что модель вызвала add_task
        self.model_mock.add_task.assert_called_once_with(task)
        
        # Проверяем, что view.task_list.clear() был вызван
        self.view_mock.task_list.clear.assert_called_once() 
        
        # Проверяем, что addItem вызван хотя бы один раз
        self.view_mock.task_list.addItem.assert_called() 

    def test_delete_task(self):
        index = 0
        self.controller.delete_task(index)
        
        # Проверяем удаление в модели
        self.model_mock.delete_task.assert_called_once_with(index)
        
        # Проверяем очистку списка в view
        self.view_mock.task_list.clear.assert_called_once() 

if __name__ == '__main__':
    unittest.main()