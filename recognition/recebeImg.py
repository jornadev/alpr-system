import cv2
import requests
import time
from datetime import datetime
import os

# URL do feed de imagem da ESP32-CAM
esp32_url = ""  
save_folder = ""

# cria a pasta se ela não existir
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

while True:
    try:
        # captura a imagem da URL
        response = requests.get(esp32_url, stream=True)
        if response.status_code == 200:
            # nomeia a foto baixada de acordo com a data e hora (para que sejam unicos)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(save_folder, f"foto_{timestamp}.jpg")

            # salva a imagem na pasta local
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Imagem salva em {filename}")
        else:
            print("Falha ao capturar imagem da ESP32-CAM")

    except Exception as e:
        print(f"Erro: {e}")

    # aguarda ??? segundos antes de capturar a próxima imagem
    time.sleep(0.8)
    
