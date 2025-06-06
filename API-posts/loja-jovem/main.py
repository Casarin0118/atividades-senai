from filtros import filtrar_por_cor, filtrar_por_marca, filtrar_por_tamanho, filtrar_por_preco
from flask import Flask, jsonify, request

app = Flask(__name__)

sapatos = [
    {"id": 1, "marca": "Nike", "modelo": "Air Max 90", "tamanho": 39, "cor": "branco", "preco": 599.90, "estoque": 15},
    {"id": 2, "marca": "Adidas", "modelo": "Superstar", "tamanho": 40, "cor": "preto", "preco": 449.90, "estoque": 8},
    {"id": 3, "marca": "Vans", "modelo": "Old Skool", "tamanho": 38, "cor": "vermelho", "preco": 329.90, "estoque": 12},
    {"id": 4, "marca": "Nike", "modelo": "Air Force 1", "tamanho": 41, "cor": "branco", "preco": 699.90, "estoque": 5},
    {"id": 5, "marca": "Puma", "modelo": "Suede Classic", "tamanho": 42, "cor": "azul", "preco": 349.90, "estoque": 7},
    {"id": 6, "marca": "Converse", "modelo": "All Star", "tamanho": 37, "cor": "preto", "preco": 279.90, "estoque": 20},
    {"id": 7, "marca": "Nike", "modelo": "Jordan 1", "tamanho": 43, "cor": "vermelho", "preco": 999.90, "estoque": 3},
    {"id": 8, "marca": "Adidas", "modelo": "Stan Smith", "tamanho": 39, "cor": "verde", "preco": 399.90, "estoque": 10},
    {"id": 9, "marca": "Mizuno", "modelo": "Wave Rider", "tamanho": 40, "cor": "prata", "preco": 549.90, "estoque": 6},
    {"id": 10, "marca": "Asics", "modelo": "Gel-Kayano", "tamanho": 41, "cor": "azul", "preco": 599.90, "estoque": 4},
    {"id": 11, "marca": "Nike", "modelo": "Dunk Low", "tamanho": 38, "cor": "rosa", "preco": 499.90, "estoque": 9},
    {"id": 12, "marca": "Adidas", "modelo": "Ultraboost", "tamanho": 42, "cor": "preto", "preco": 799.90, "estoque": 7},
    {"id": 13, "marca": "New Balance", "modelo": "574", "tamanho": 39, "cor": "cinza", "preco": 449.90, "estoque": 11},
    {"id": 14, "marca": "Nike", "modelo": "Blazer", "tamanho": 40, "cor": "branco", "preco": 429.90, "estoque": 8},
    {"id": 15, "marca": "Puma", "modelo": "RS-X", "tamanho": 41, "cor": "amarelo", "preco": 479.90, "estoque": 5},
    {"id": 16, "marca": "Reebok", "modelo": "Classic Leather", "tamanho": 37, "cor": "branco", "preco": 349.90, "estoque": 13},
    {"id": 17, "marca": "Nike", "modelo": "Pegasus", "tamanho": 42, "cor": "azul", "preco": 549.90, "estoque": 6},
    {"id": 18, "marca": "Adidas", "modelo": "NMD_R1", "tamanho": 43, "cor": "preto", "preco": 699.90, "estoque": 4},
    {"id": 19, "marca": "Vans", "modelo": "Sk8-Hi", "tamanho": 38, "cor": "preto", "preco": 379.90, "estoque": 10},
    {"id": 20, "marca": "Nike", "modelo": "React Element", "tamanho": 39, "cor": "branco", "preco": 599.90, "estoque": 7},
    {"id": 21, "marca": "Fila", "modelo": "Disruptor", "tamanho": 36, "cor": "rosa", "preco": 299.90, "estoque": 9},
    {"id": 22, "marca": "Adidas", "modelo": "Gazelle", "tamanho": 40, "cor": "verde", "preco": 429.90, "estoque": 8},
    {"id": 23, "marca": "Nike", "modelo": "Air Max 270", "tamanho": 41, "cor": "preto", "preco": 649.90, "estoque": 5},
    {"id": 24, "marca": "Puma", "modelo": "Cali", "tamanho": 37, "cor": "branco", "preco": 399.90, "estoque": 12},
    {"id": 25, "marca": "Asics", "modelo": "Gel-Lyte", "tamanho": 42, "cor": "vermelho", "preco": 499.90, "estoque": 6},
    {"id": 26, "marca": "Nike", "modelo": "Air Max 97", "tamanho": 43, "cor": "prata", "preco": 799.90, "estoque": 3},
    {"id": 27, "marca": "Adidas", "modelo": "Continental 80", "tamanho": 38, "cor": "branco", "preco": 399.90, "estoque": 10},
    {"id": 28, "marca": "Vans", "modelo": "Era", "tamanho": 39, "cor": "azul", "preco": 299.90, "estoque": 15},
    {"id": 29, "marca": "Nike", "modelo": "Air Max Plus", "tamanho": 40, "cor": "preto", "preco": 699.90, "estoque": 4},
    {"id": 30, "marca": "Puma", "modelo": "Future Rider", "tamanho": 41, "cor": "laranja", "preco": 449.90, "estoque": 8},
    {"id": 31, "marca": "Converse", "modelo": "Chuck Taylor", "tamanho": 36, "cor": "vermelho", "preco": 279.90, "estoque": 18},
    {"id": 32, "marca": "Nike", "modelo": "Air Max 2090", "tamanho": 42, "cor": "branco", "preco": 749.90, "estoque": 5},
    {"id": 33, "marca": "Adidas", "modelo": "ZX 2K 4D", "tamanho": 43, "cor": "cinza", "preco": 899.90, "estoque": 2},
    {"id": 34, "marca": "New Balance", "modelo": "997", "tamanho": 37, "cor": "azul", "preco": 599.90, "estoque": 7},
    {"id": 35, "marca": "Nike", "modelo": "Air VaporMax", "tamanho": 38, "cor": "preto", "preco": 849.90, "estoque": 4},
    {"id": 36, "marca": "Reebok", "modelo": "Club C", "tamanho": 39, "cor": "branco", "preco": 349.90, "estoque": 11},
    {"id": 37, "marca": "Puma", "modelo": "Smash", "tamanho": 40, "cor": "preto", "preco": 279.90, "estoque": 14},
    {"id": 38, "marca": "Nike", "modelo": "Air Max 720", "tamanho": 41, "cor": "rosa", "preco": 899.90, "estoque": 3},
    {"id": 39, "marca": "Adidas", "modelo": "Ozweego", "tamanho": 42, "cor": "bege", "preco": 549.90, "estoque": 6},
    {"id": 40, "marca": "Vans", "modelo": "Authentic", "tamanho": 36, "cor": "preto", "preco": 249.90, "estoque": 20},
    {"id": 41, "marca": "Nike", "modelo": "Air Max 95", "tamanho": 43, "cor": "cinza", "preco": 799.90, "estoque": 4},
    {"id": 42, "marca": "Asics", "modelo": "Gel-Quantum", "tamanho": 37, "cor": "roxo", "preco": 649.90, "estoque": 5},
    {"id": 43, "marca": "Puma", "modelo": "Thunder Spectra", "tamanho": 38, "cor": "branco", "preco": 499.90, "estoque": 9},
    {"id": 44, "marca": "Nike", "modelo": "Air Max 98", "tamanho": 39, "cor": "azul", "preco": 849.90, "estoque": 3},
    {"id": 45, "marca": "Adidas", "modelo": "Yeezy Boost 350", "tamanho": 40, "cor": "branco", "preco": 1199.90, "estoque": 2},
    {"id": 46, "marca": "New Balance", "modelo": "990", "tamanho": 41, "cor": "cinza", "preco": 899.90, "estoque": 4},
    {"id": 47, "marca": "Nike", "modelo": "Air Max Scorpion", "tamanho": 42, "cor": "preto", "preco": 1099.90, "estoque": 1},
    {"id": 48, "marca": "Vans", "modelo": "Slip-On", "tamanho": 37, "cor": "xadrez", "preco": 329.90, "estoque": 12},
    {"id": 49, "marca": "Puma", "modelo": "Clyde", "tamanho": 38, "cor": "preto", "preco": 399.90, "estoque": 8},
    {"id": 50, "marca": "Nike", "modelo": "Air Max 200", "tamanho": 39, "cor": "branco", "preco": 549.90, "estoque": 6}
]

@app.route('/sapatos', methods=['GET'])
def listar_sapatos():

    marca = request.args.get('marca')
    cor = request.args.get('cor')
    tamanho = request.args.get('tamanho', type=int)

    if marca and cor:
        lista_marca = filtrar_por_marca(sapatos, marca)
        lista_marca_cor = filtrar_por_cor(lista_marca, cor)
        lista_marca_cor_tamanho = filtrar_por_tamanho(lista_marca_cor, tamanho='')
        return lista_marca_cor_tamanho

    if marca:
        lista_marca = filtrar_por_marca(sapatos, marca)
        return lista_marca

    if cor:
        lista_cor = filtrar_por_cor(sapatos, cor)
        return lista_cor

    if tamanho:
        lista_tamanho = filtrar_por_tamanho(sapatos, tamanho='')
        return  lista_tamanho


@app.route('/sapatos/baratos', methods=['GET'])
def listar_sapato_por_preco_max():
    preco = request.args.get('preco', type=float)

    if preco:
        lista_preco_max = filtrar_por_preco(sapatos, preco_maximo=preco)
        return jsonify(lista_preco_max)





if __name__ == '__main__':
    app.run(debug=True)

