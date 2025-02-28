import paho.mqtt.client as mqtt

broker = "maqiatto.com"
porta = 1883

topico_tempatual = "josemarcio0araujo@gmail.com/tempatual"
compressor = "josemarcio0araujo@gmail.com/compressor"
parliga = "josemarcio0araujo@gmail.com/parliga"
pardesliga = "josemarcio0araujo@gmail.com/pardesliga"

usuario = "josemarcio0araujo@gmail.com"
password = "Samuel12"

client = mqtt.Client()

client.username_pw_set(usuario, password)

def on_public(topico, msg):
    client.publish(topico, msg)

def on_message(client, userdata, msg):
    global temperatura_atual
    global compressor_status
    global temp_maxima
    global temp_minima

    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode('utf-8')}")

    if msg.topic == topico_tempatual:
        temperatura_atual = msg.payload.decode('utf-8')

    elif msg.topic == compressor:
       compressor_status = msg.payload.decode('utf-8')

    elif msg.topic == parliga:
       temp_maxima = msg.payload.decode('utf-8')

    elif msg.topic == pardesliga:
        temp_minima = msg.payload.decode('utf-8')
        print(str(temp_minima))

    else:
        print("erro nenhum topico encontrado")



def get_temp_minima():
    global temp_minima
    return temp_minima


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT!")
        client.subscribe(topico_tempatual)
        client.subscribe(compressor)
        client.subscribe(parliga)
        client.subscribe(pardesliga)

        #botoes.atualizar_ui(parliga, pardesliga, compressor, topico_tempatual)
    else:
        print(f"Falha na conexão MQTT. Código de retorno: {rc}")

def connect_mqtt():
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(broker, porta, 60)
        client.loop_start()
    except Exception as e:
        print(f"Erro ao conectar ao MQTT: {e}")
