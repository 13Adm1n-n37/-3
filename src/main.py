import sys
from PyQt5.QtWidgets import QApplication
from model import TaskModel
from view import TaskView
from controller import TaskController

def main():
    app = QApplication(sys.argv)
    
    model = TaskModel()
    view = TaskView(None)
    controller = TaskController(model, view)
    view.controller = controller  # Передача контроллера в вид
    
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()