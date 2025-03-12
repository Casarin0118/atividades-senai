class musica:
    def __init__(self, cantor, nome, duracao, produtora, genero):
        self.cantor = cantor
        self.nome = nome
        self.duracao = duracao
        self.__produtora = produtora
        self.genero = genero

    def __str__(self):
        return f"A musica {self.nome} pertence ao cantor {self.cantor} possuí {self.duracao} foi feita pela produtora {self.__produtora} e é do genero {self.genero}"
    