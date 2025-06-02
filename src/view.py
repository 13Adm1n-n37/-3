from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QComboBox, QDateEdit, QCheckBox  
from PyQt5.QtCore import Qt, QDate  

class TaskView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller  # Ссылка на контроллер
        self.setWindowTitle("Менеджер задач")
        self.init_ui()

    def init_ui(self):
        # Поля ввода
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Введите задачу...")
        # Выбор приоритета
        self.priority_combo = QComboBox(self)
        self.priority_combo.addItems(["Низкий", "Средний", "Высокий"])
        # Выбор категории
        self.category_combo = QComboBox(self)
        self.category_combo.addItems(["Работа", "Личное", "Обучение"])
        # Выбор даты
        self.due_date = QDateEdit(self)
        # Кнопка добавления
        self.add_button = QPushButton("Добавить задачу", self)
        self.add_button.clicked.connect(self.add_task)
        # Список задач
        self.task_list = QListWidget(self)
        # Кнопки редактирования и удаления
        self.edit_button = QPushButton("Редактировать", self)
        self.delete_button = QPushButton("Удалить", self)
        self.edit_button.clicked.connect(self.edit_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.completed_checkbox = QCheckBox("Выполнено", self)
        # Выпадающий список фильтра
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Все", "Выполненные", "Невыполненные"])
        self.filter_combo.currentIndexChanged.connect(self.filter_tasks)

        # Компоновка интерфейса
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Задача:"))
        layout.addWidget(self.title_input)
        layout.addWidget(QLabel("Приоритет:"))
        layout.addWidget(self.priority_combo)
        layout.addWidget(QLabel("Категория:"))
        layout.addWidget(self.category_combo)
        layout.addWidget(QLabel("Срок выполнения:"))
        layout.addWidget(self.due_date)
        layout.addWidget(self.add_button)
        layout.addWidget(QLabel("Список задач:"))
        layout.addWidget(self.task_list)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.completed_checkbox)
        layout.addWidget(QLabel("Фильтр:"))
        layout.addWidget(self.filter_combo)
        self.setLayout(layout)

    def add_task(self):
        task = {
            "title": self.title_input.text(),
            "priority": self.priority_combo.currentText(),
            "category": self.category_combo.currentText(),
            "due_date": self.due_date.date().toString("yyyy-MM-dd"),
            "completed": self.completed_checkbox.isChecked()
        }
        self.controller.add_task(task)
        self.title_input.clear()
        self.completed_checkbox.setChecked(False)

    def edit_task(self):
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            task = self.controller.model.tasks[selected_index]
            self.title_input.setText(task["title"])
            self.priority_combo.setCurrentText(task["priority"])
            self.category_combo.setCurrentText(task["category"])
            self.due_date.setDate(QDate.fromString(task["due_date"], "yyyy-MM-dd"))
            self.completed_checkbox.setChecked(task["completed"])
            # Удаляем задачу из модели и обновляем список
            self.controller.delete_task(selected_index)
            self.controller.update_task_list()

    def delete_task(self):
        selected_index = self.task_list.currentRow()
        if selected_index >= 0:
            self.controller.delete_task(selected_index)

    def filter_tasks(self):
        filter_type = self.filter_combo.currentText()
        filtered_tasks = []
        if filter_type == "Все":
            filtered_tasks = self.controller.model.tasks
        elif filter_type == "Выполненные":
            filtered_tasks = [t for t in self.controller.model.tasks if t["completed"]]
        elif filter_type == "Невыполненные":
            filtered_tasks = [t for t in self.controller.model.tasks if not t["completed"]]
        self.task_list.clear()  # Исправлено: self.task_list вместо self.view.task_list
        for task in filtered_tasks:
            status = "✅" if task["completed"] else "❌"
            text = f"{status} {task['title']} | {task['priority']} | {task['category']} | {task['due_date']}"
            self.task_list.addItem(text)