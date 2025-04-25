import cv2
import pytesseract
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from database.database import verificar_placa, registrar_entrada  # Importa as funções do banco de dados
from esp32.servoControl import enviar_comando_abrir

pytesseract.pytesseract.tesseract_cmd = "C:\\Tesseract-OCR\\Tesseract.exe" #temoa que passar o executavel do tesseract
# pasta que puxaremos as imagens
image_folder = r"C:\imagensesp32"

# função para processar cada imagem
def processar_imagem(image_path):
    print(f"Processando a imagem: {image_path}")
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    # converte a iamgem para escala de cinza e aplica binarização
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # configurações do OCR: apenas letras e números e modo PSM 6 (ou 11)
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=ABER19'
    resultado = pytesseract.image_to_string(thresh, config=custom_config)
    placa = resultado.strip()
    print(f"Placa reconhecida: {placa}")

    # verificacao da placa reconhecida no banco de dados
    proprietario = verificar_placa(placa)
    if proprietario:
        print(f"Placa {placa} autorizada. Proprietário: {proprietario}. Liberando acesso.")
        registrar_entrada(placa, proprietario)
        enviar_comando_abrir()  # envia o comando ao arduino para abrir o motor
    else:
        print(f"Placa {placa} não autorizada. Acesso negado.")

# classe para manipular eventos de adição de arquivos
class NewImageHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        # verifica se o arquivo é uma imagem JPG
        if event.src_path.endswith(".jpg"):
            processar_imagem(event.src_path)

# configura e inicia o observador
if __name__ == "__main__":
    event_handler = NewImageHandler()
    observer = Observer()
    observer.schedule(event_handler, path=image_folder, recursive=False)
    observer.start()
    print(f"Monitorando a pasta {image_folder} por novas imagens...")

    try:
        while True:
            pass  # mantém o script em execução
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
