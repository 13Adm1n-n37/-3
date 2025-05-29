from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel, QComboBox, QDateEdit
from PyQt5.QtCore import Qt

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

        self.setLayout(layout)

    def add_task(self):
        # Сбор данных из полей ввода
        task = {
            "title": self.title_input.text(),
            "priority": self.priority_combo.currentText(),
            "category": self.category_combo.currentText(),
            "due_date": self.due_date.date().toString("yyyy-MM-dd"),
            "completed": False
        }
        # Передача задачи в контроллер
        self.controller.add_task(task)
        self.title_input.clear()