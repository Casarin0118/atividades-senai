class Produto:
    def __init__(self, id, nome, descricao, preco, estoque, foto_url=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.foto_url = foto_url

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "preco": self.preco,
            "estoque": self.estoque,
            "foto_url": self.foto_url
        }