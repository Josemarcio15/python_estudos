from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from decimal import Decimal, InvalidOperation

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.input_valor = QLineEdit()
        self.botao = QPushButton("Converter")
        self.resultado = QLabel("Valor convertido aparecerá aqui")

        layout = QVBoxLayout()
        layout.addWidget(self.input_valor)
        layout.addWidget(self.botao)
        layout.addWidget(self.resultado)
        self.setLayout(layout)

        self.botao.clicked.connect(self.converter_valor)

    def converter_valor(self):
        texto = self.input_valor.text()
        texto_formatado = texto.replace(",", ".")
        try:
            valor_decimal = Decimal(texto_formatado)
            self.resultado.setText(f"Valor convertido: R$ {valor_decimal:.2f}")
        except InvalidOperation:
            self.resultado.setText("Valor inválido! Use formato 10,50")

if __name__ == "__main__":
    app = QApplication([])
    janela = Janela()
    janela.show()
    app.exec()
