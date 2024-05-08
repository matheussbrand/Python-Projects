from vidstream import ScreenShareClient # Importa a classe ScreenShareClient do módulo vidstream
import threading  # Importa o módulo threading para permitir operações simultâneas

sender = ScreenShareClient(
    "192.168.8.17", 9999
)  # Cria uma instância de ScreenShareClient com o endereço IP '192.168.8.17' e a porta 9999

t = threading.Thread(
    target=sender.start_stream
)  # Cria uma thread com a função target sendo sender.start_stream
t.start()  # Inicia a thread criada

while (
    input("") != "STOP"
):  # Enquanto a entrada do usuário não for 'STOP', continua solicitando entrada
    continue

sender.stop_stream()  # Quando 'STOP' é inserido, a função stop_stream de sender é chamada para encerrar a transmissão
