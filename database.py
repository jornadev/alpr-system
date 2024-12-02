import mysql.connector

# função para conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",       
        user="root",    
        password="1203",   
        database="sistema_acesso"
    )

# função para verificar se a placa está no banco de dados e retornar o nome do proprietário
def verificar_placa(placa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT proprietario FROM autorizacoes WHERE placa = %s", (placa,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0]  # retorna o nome do proprietário
    return None  # se a placa nao estiver autorizada

# função para registrar entrada
def registrar_entrada(placa, proprietario):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO historico_acessos (placa, proprietario, horario_entrada)
        VALUES (%s, %s, NOW())
    """, (placa, proprietario))
    conn.commit()
    conn.close()
    print(f"Entrada registrada: {placa} - {proprietario}")


