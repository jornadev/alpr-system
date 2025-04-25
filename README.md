# 🚗 alpr_system  
**Sistema Automático de Acesso Veicular**

Projeto desenvolvido durante o quarto semestre do curso de Ciência da Computação.

## 📌 Descrição

Este projeto tem como objetivo automatizar o controle de acesso veicular utilizando tecnologias de visão computacional e inteligência artificial. O sistema realiza o reconhecimento de placas veiculares através de imagens capturadas por uma **ESP32-CAM**. As imagens são processadas e analisadas em um servidor utilizando bibliotecas da linguagem Python.

## 🔧 Tecnologias Utilizadas

- 📷 **ESP32-CAM**: Captura de imagens das placas dos veículos.
- 🐍 **Python**
  - 🧠 **OpenCV**: Tratamento e pré-processamento das imagens.
  - 🔤 **Pytesseract**: Reconhecimento óptico de caracteres (OCR) nas placas.
- 🗃️ **MySQL**: Armazenamento e verificação das placas cadastradas.
- 💻 **Flask (opcional)**: Interface web para monitoramento ou gerenciamento (caso tenha sido usado).
  
## ⚙️ Funcionamento

1. A **ESP32-CAM** captura a imagem de um veículo que se aproxima do portão.
2. A imagem é enviada para o servidor onde o **OpenCV** faz o tratamento da imagem (conversão para escala de cinza, binarização, etc.).
3. O **Pytesseract** realiza o reconhecimento dos caracteres da placa.
4. O sistema realiza uma consulta no banco de dados **MySQL** para verificar se a placa está cadastrada e autorizada.
5. Se a placa for autorizada, o sistema envia o sinal para liberar o acesso (ex: abrir o portão).

## 💾 Requisitos

- Python 3.x  
- OpenCV  
- Pytesseract  
- MySQL Server  
- (Opcional) Flask  
- Bibliotecas da ESP32 instaladas no Arduino IDE

## 👨‍💻 Autor

Desenvolvido por **[Henrique Jornada]**, estudante de Ciência da Computação.  
Entre em contato: [LinkedIn](https://linkedin.com/in/henriquejornada)
