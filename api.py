#objetivo:Criar um api de disponibiliza a consulta, 
#criação, edição e exclusão de livros.

#URL BASE: LOCAL HOST

#ENDPOINTS:
    #- localhost/livros(get)
    #- localhost/livros/id(get)
    #- localhost/livros/id(put)
    #- localhost/livros/id(delete)

#RECURSOS:
    #livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'game of thrones',
        'autor': 'george r. r. martin',
    },
    {
        'id': 2,
        'titulo': 'o senhor dos aneis',
        'autor': 'j. r. r. tolkien',
    },
    {
        'id': 3,
        'titulo': '1984',
        'autor': 'george orwell',
    }
]

#Consultar(todos os livros)
@app.route('/livros', methods=['GET']) #Get é o método que indica que queremos consultar algo, ou seja, obter informações.
def obter_livros():
    return jsonify(livros)


#Consultar por id
@app.route('/livros/<int:id>', methods=['GET']) #para indicar que o id é um inteiro, usamos <int:id>, e assim, o flask entende que o id é um parâmetro que será passado na url.
def obter_id_livro(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#Editar por id
@app.route('/livros/<int:id>', methods=['PUT']) #para indicar que o id é um inteiro, usamos <int:id>
def editar_livro(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#Criar
@app.route('/livros', methods=['POST']) #Post é o método que indica que queremos criar algo, ou seja, enviar informações.
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#excluir por id
@app.route('/livros/<int:id>', methods=['DELETE']) #Delete é o método que indica que queremos excluir algo, ou seja, remover informações.
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)