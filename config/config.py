import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",  # Seu host
        user="root",  # Usuário do MySQL
        password="1203",  # Senha do MySQL
        database="sistema_acesso"  # Nome do seu banco de dados
    )
    return conn
