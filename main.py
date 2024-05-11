from flask import Flask, request, jsonify
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500"]}})

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
    valor_nota = request.form.get('nota')
    ra_aluno_fkey = request.form.get('raAluno')
    cod_disciplina_fkey = request.form.get('disciplina')
    ra_professor_fkey = request.form.get('raProfessor')

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
    data = request.form

    ra_aluno = data.get('raAluno')
    cod_disciplina = data.get('disciplina')
    ra_professor = data.get('raProfessor')
    valor_nota = data.get('nota')

    conn = connect_to_db()
    cur = conn.cursor()

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
