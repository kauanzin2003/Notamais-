from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'database': 'programa_nota',
    'user': 'postgres',
    'password': '2003',
    'port': '5432'
}

# Função para conectar ao banco de dados
def connect_to_db():
    return psycopg2.connect(**db_config)

# Rota para obter todas as notas
@app.route('/notas', methods=['GET', 'POST'])
def get_notas():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM notas;')
    notas = cur.fetchall()
    conn.close()
    return jsonify({'notas': notas})

# Rota para criar uma nova nota
@app.route('/crianota', methods=['POST'])
def create_nota():
    data = request.get_json()
    valor_nota = data['valor_nota']
    ra_aluno_fkey = data['ra_aluno']
    cod_disciplina_fkey = data['cod_disciplina']
    ra_professor_fkey = data['ra_professor']

    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO notas (valor_nota, ra_aluno, cod_disciplina, ra_professor) VALUES (%s, %s, %s, %s);',
                (valor_nota, ra_aluno_fkey, cod_disciplina_fkey, ra_professor_fkey))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Nota criada com sucesso!'})

# Rota para editar uma nota existente
@app.route('/editar/<int:id_nota>', methods=['PUT'])
def edit_nota(id_nota):
    data = request.get_json()

    ra_aluno = data.get('ra_aluno')
    cod_disciplina = data.get('cod_disciplina')
    ra_professor = data.get('ra_professor')
    valor_nota = data.get('valor_nota')

    conn = connect_to_db()
    cur = conn.cursor()

    # Atualiza apenas os campos que foram fornecidos no JSON
    cur.execute(
        'UPDATE notas SET ra_aluno = %s, cod_disciplina = %s, ra_professor = %s, valor_nota = %s WHERE id_nota = %s;',
        (ra_aluno, cod_disciplina, ra_professor, valor_nota, id_nota))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Nota atualizada com sucesso!'})

# Rota para deletar uma nota existente
@app.route('/excluir/<int:id_nota>', methods=['DELETE'])
def delete_nota(id_nota):
    conn = connect_to_db()
    cur = conn.cursor()

    try:
        cur.execute('DELETE FROM notas WHERE id_nota = %s;', (id_nota,))
        conn.commit()
        return jsonify({'message': 'Nota deletada com sucesso!'})
    except Exception as e:
        conn.rollback()
        return jsonify({'error': f'Erro ao deletar a nota: {str(e)}'}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run()
