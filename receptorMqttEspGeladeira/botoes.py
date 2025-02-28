from enum import Enum
from conexao_mqtt import on_public
import conexao_mqtt

class Comandos(Enum):
    SOLICITAR = "13.0"

class Botoes:
    def __init__(self, ui):
        self.ui = ui
        self.conectar_botoes()

    def conectar_botoes(self):
        self.ui.solicitar_dados.clicked.connect(self.solicitar_dados)

    def solicitar_dados(self):
        on_public("josemarcio0araujo@gmail.com/solicitar", Comandos.SOLICITAR.value)
        self.atualizar_ui()
    def atualizar_ui(self):
        tmin = conexao_mqtt.get_temp_minima()
         #max = conexao_mqtt.temp_maxima
         #compressor = conexao_mqtt.compressor_status
         #tempatual = conexao_mqtt.temperatura_atual
        print(tmin)
        self.ui.parminima.setText(str(tmin))
         #self.ui.parminima.setText(max)
         #self.ui.parminima.setText(compressor)
         #self.ui.parminima.setText(tempatual)
