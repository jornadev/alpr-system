from flask import Flask, render_template, redirect, url_for, request, jsonify
from config import get_db_connection

app = Flask(__name__)

# Rota principal (dashboard)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para listar autorizações
@app.route('/autorizacoes')
def autorizacoes():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM autorizacoes")
    autorizacoes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(autorizacoes)

# Rota para listar histórico de acessos
@app.route('/historico')
def historico():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM historico_acessos ORDER BY horario_entrada DESC")
    historico = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(historico)

# Rota para adicionar nova placa autorizada
@app.route('/adicionar_placa', methods=['POST'])
def adicionar_placa():
    data = request.get_json()
    placa = data.get('placa')
    proprietario = data.get('proprietario')

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO autorizacoes (placa, proprietario) VALUES (%s, %s)", (placa, proprietario))
        conn.commit()
        return jsonify({"status": "success", "message": "Placa adicionada com sucesso!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    finally:
        cursor.close()
        conn.close()

# Rota para remover placa autorizada
@app.route('/remover_placa', methods=['POST'])
def remover_placa():
    data = request.get_json()
    placa = data.get('placa')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM autorizacoes WHERE placa = %s", (placa,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"status": "success", "message": "Placa removida com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
