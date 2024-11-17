import sys
import os
import json

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QAbstractListModel
from PySide6.QtGui import QImage

from MainWindow import Ui_QMainWindow

basedir = os.path.dirname(__file__)
tick = QImage(os.path.join(basedir, 'tick.png'))

class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text
        
        if role == Qt.DecorationRole:
            status, text = self.todos[index.row()]
            if status:
                return tick
    
    def rowCount(self, index):
        return len(self.todos)

class MainWindow(QtWidgets.QMainWindow, Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel()
        self.load()
        self.todo_view.setModel(self.model)

        self.button_add_todo.pressed.connect(self.add)
        self.button_delete.pressed.connect(self.delete)
        self.button_complete.pressed.connect(self.complete)

    def add(self):
        text = self.todo_edit.text()
        text = text.strip()
        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todo_edit.setText('')
            self.save()

    def delete(self):
        indexes = self.todo_view.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todo_view.clearSelection()
            self.save()

    def complete(self):
        indexes = self.todo_view.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)

            self.model.dataChanged.emit(index, index)
            self.todo_view.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.todos = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.json', 'w') as f:
            data = json.dump(self.model.todos, f)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.setStyle('Fusion')
app.exec()