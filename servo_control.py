import serial
import time

arduino_port = "COM6"
  
baud_rate = 9600
arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
time.sleep(2)  # aguarda o Arduino inicializar

def enviar_comando_abrir():
    arduino.write(b'A')  # 'A' representa o comando de "abrir"
    print("Comando enviado ao Arduino para abrir o portão")
