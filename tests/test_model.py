import json
from model import TaskModel

def test_add_task():
    model = TaskModel(filename="test_tasks.json")
    model.add_task({"title": "Test", "completed": False})
    assert len(model.tasks) == 1

def test_delete_task():
    model = TaskModel(filename="test_tasks.json")
    model.delete_task(0)
    assert len(model.tasks) == 0