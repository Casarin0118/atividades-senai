from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from controllers.produtos_controller import (
    get_produtos_ctrl,
    get_produto_by_id_ctrl,
    get_produtos_ordenados_ctrl,
    get_produtos_filtrados_ctrl,
    adicionar_produto_ctrl
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'Corinthians'
jwt = JWTManager(app)


@app.route('/login', methods=['POST'])
def login():
    token = create_access_token(identity='usuario')
    return jsonify({'token': token})


@app.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    preco_asc = request.args.get('preco_asc', '').lower() == 'true'
    preco_desc = request.args.get('preco_desc', '').lower() == 'true'
    descricao = request.args.get('description_part', '')

    if preco_asc and preco_desc:
        return jsonify({'erro': 'Use apenas um parâmetro: preco_asc=true OU preco_desc=true'}), 400

    if preco_asc:
        return jsonify(get_produtos_ordenados_ctrl('asc'))

    if preco_desc:
        return jsonify(get_produtos_ordenados_ctrl('desc'))

    if descricao:
        return jsonify(get_produtos_filtrados_ctrl(descricao))

    return jsonify(get_produtos_ctrl())


@app.route('/products/<int:produto_id>', methods=['GET'])
@jwt_required()
def get_product_by_id(produto_id):
    produto = get_produto_by_id_ctrl(produto_id)
    if produto:
        return jsonify(produto)
    return jsonify({'erro': 'Produto não encontrado'}), 404


@app.route('/products', methods=['POST'])
@jwt_required()
def create_product():
    dados = request.get_json()
    campos_obrigatorios = ['nome', 'descricao', 'preco', 'estoque']
    if not dados or not all(campo in dados for campo in campos_obrigatorios):
        return jsonify({'erro': 'Dados do produto inválidos ou incompletos'}), 400

    novo_produto = adicionar_produto_ctrl(dados)
    return jsonify(novo_produto), 201


if __name__ == '__main__':
    app.run(debug=True)
