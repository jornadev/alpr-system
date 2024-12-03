# alpr_system

Sistema Automático de Acesso Veicular

Projeto desenvolvido durante o quarto semestre do curso de Ciencia da Computação.

O sistema tem como objetivo fazer o reconhecimento de placas veiculares com imagens obtidas através de uma ESP32, essas
imagens são processadas e tratadas pela biblioteca OpenCV, após devidos tratamentos, a iamgens passa pelo reconhecimento
óptico de caracteres com a biblioteca Pytesseract, ambas da linguagem Python. Com os caracteres extraídos, é realizada uma
consulta no banco de dados MySQL. 



