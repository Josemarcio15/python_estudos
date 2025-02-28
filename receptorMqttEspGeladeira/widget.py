# pyside6-uic form.ui -o ui_form.py
import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from conexao_mqtt import connect_mqtt
from botoes import Botoes  # Importa a classe de botões

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.botoes = Botoes(self.ui)  # Inicializa os botões
        connect_mqtt()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
