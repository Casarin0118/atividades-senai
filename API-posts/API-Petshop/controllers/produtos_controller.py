from models.produtos import Produto

produtos_lista = [
    Produto(1, "Coleira", "Coleira para cachorro de pequeno porte", 23.90, 26, ""),
    Produto(2, "Ração para cães adultos", "Ração premium para cães adultos de médio porte", 119.90, 40, ""),
    Produto(3, "Areia para gatos", "Areia higiênica com controle de odor para gatos", 35.00, 60, ""),
    Produto(4, "Brinquedo de borracha", "Brinquedo mordedor em formato de osso", 15.00, 75, ""),
    Produto(5, "Comedouro duplo", "Comedouro e bebedouro acoplado para cães e gatos", 29.90, 30, ""),
    Produto(6, "Tapete higiênico", "Tapete absorvente para cães", 39.90, 45, ""),
    Produto(7, "Shampoo para cães", "Shampoo neutro para cães com pele sensível", 22.50, 50, ""),
    Produto(8, "Antipulgas", "Medicamento antipulgas em comprimido para cães", 89.00, 20, ""),
    Produto(9, "Caixa de transporte", "Caixa de transporte tamanho médio", 150.00, 12, ""),
    Produto(10, "Osso de couro", "Osso natural para mastigação", 9.90, 80, ""),
    Produto(11, "Cama para cachorro", "Cama acolchoada tamanho G", 120.00, 18, ""),
    Produto(12, "Ração para gatos filhotes", "Ração específica para crescimento saudável", 92.00, 34, ""),
    Produto(13, "Bebedouro automático", "Fonte com filtro para cães e gatos", 99.90, 22, ""),
    Produto(14, "Escova de pelos", "Escova com cerdas macias para remoção de pelos mortos", 18.90, 55, ""),
    Produto(15, "Brinquedo de pelúcia", "Brinquedo com apito para cães", 25.00, 48, ""),
    Produto(16, "Coleira peitoral", "Coleira tipo peitoral para cães médios", 35.00, 27, ""),
    Produto(17, "Ração para roedores", "Alimento completo para hamster e porquinho da índia", 19.90, 38, ""),
    Produto(18, "Areia sílica para gatos", "Areia higiênica de sílica com alta absorção", 42.00, 32, ""),
    Produto(19, "Pente para pulgas", "Pente de aço para remoção de pulgas e ovos", 14.90, 44, ""),
    Produto(20, "Bolinha de tênis", "Brinquedo resistente para cães", 12.00, 70, ""),
    Produto(21, "Ração para cães filhotes", "Ração específica para cães em fase de crescimento", 110.00, 37, ""),
    Produto(22, "Coleira com plaquinha", "Coleira com plaquinha de identificação gravável", 28.50, 29, ""),
    Produto(23, "Petisco dental", "Snack para limpeza dos dentes", 20.00, 65, ""),
    Produto(24, "Toca para gatos", "Toca de tecido para gatos dormirem confortavelmente", 95.00, 16, ""),
    Produto(25, "Roupinha para cachorro", "Roupa de frio tamanho P", 45.00, 35, ""),
    Produto(26, "Limpador de patas", "Copo com cerdas para lavar as patas dos cães", 30.00, 28, ""),
    Produto(27, "Tesoura para unhas", "Tesoura especial para cortar unhas de pets", 17.90, 50, ""),
    Produto(28, "Coleira refletiva", "Coleira com fita refletiva para segurança noturna", 32.00, 23, ""),
    Produto(29, "Ração úmida para gatos", "Sachê com pedaços de carne em molho", 4.90, 100, ""),
    Produto(30, "Desinfetante pet", "Desinfetante seguro para uso em ambientes com animais", 24.90, 40, ""),
    Produto(31, "Shampoo para gatos", "Shampoo seco para higiene de gatos", 27.00, 33, ""),
    Produto(32, "Arranhador pequeno", "Arranhador de papelão reciclável", 59.00, 21, ""),
    Produto(33, "Escova dental", "Escova dupla para higiene bucal de cães e gatos", 13.50, 46, ""),
    Produto(34, "Mordedor com corda", "Brinquedo resistente com corda para puxar", 19.00, 36, ""),
    Produto(35, "Porta petiscos", "Brinquedo dispenser de petiscos", 49.90, 27, ""),
    Produto(36, "Fonte para gatos", "Fonte elétrica com filtro para gatos beberem mais água", 135.00, 14, ""),
    Produto(37, "Casinha plástica", "Casinha para cães pequenos", 180.00, 10, ""),
    Produto(38, "Spray educador", "Spray para evitar xixi fora do lugar", 34.90, 24, ""),
    Produto(39, "Tapete gelado", "Tapete refrescante para dias quentes", 79.90, 19, ""),
    Produto(40, "Luva removedora de pelos", "Luva que remove pelos soltos durante o carinho", 21.90, 42, ""),
    Produto(41, "Bolsa para transporte", "Bolsa acolchoada para gatos e cães de pequeno porte", 99.00, 13, ""),
    Produto(42, "Cinto de segurança", "Cinto que prende o pet no carro com segurança", 36.00, 25, ""),
    Produto(43, "Colônia pet", "Colônia com fragrância suave para pets", 26.00, 30, ""),
    Produto(44, "Cortador elétrico de pelos", "Máquina para tosa caseira de cães e gatos", 199.00, 9, ""),
    Produto(45, "Brinquedo interativo", "Jogo de inteligência para cães e gatos", 89.00, 18, ""),
    Produto(46, "Guia retrátil", "Guia extensível para passeios", 59.90, 31, ""),
    Produto(47, "Ração para peixe beta", "Ração específica para peixes ornamentais", 8.90, 50, ""),
    Produto(48, "Termômetro aquático", "Termômetro para controle da temperatura em aquários", 12.00, 20, ""),
    Produto(49, "Filtro para aquário", "Filtro de carvão ativado para aquários", 45.00, 15, ""),
    Produto(50, "Luz UV para aquário", "Iluminação e esterilização para aquários", 72.00, 11, ""),

]

def get_produtos_ctrl():
    return [produto.to_json() for produto in produtos_lista]


def get_produto_by_id_ctrl(produto_id):
    for produto in produtos_lista:
        if produto.id == produto_id:
            return produto.to_json()
    return None


def get_produtos_ordenados_ctrl(ordenacao):
    produtos = [produto.to_json() for produto in produtos_lista]
    if not produtos:
        return []

    if ordenacao == 'asc':
        return sorted(produtos, key=lambda x: x['preco'])
    elif ordenacao == 'desc':
        return sorted(produtos, key=lambda x: x['preco'], reverse=True)

    return produtos


def get_produtos_filtrados_ctrl(termo):
    return [produto.to_json() for produto in produtos_lista
            if termo.lower() in produto.descricao.lower()]


def adicionar_produto_ctrl(novo_produto):
    novo_id = max([p.id for p in produtos_lista], default=0) + 1
    produto = Produto(
        id=novo_id,
        nome=novo_produto['nome'],
        descricao=novo_produto['descricao'],
        preco=novo_produto['preco'],
        estoque=novo_produto['estoque'],
        foto_url=novo_produto.get('foto_url', '')
    )
    produtos_lista.append(produto)
    return produto.to_json()
