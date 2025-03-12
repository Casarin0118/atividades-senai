class Filme:
    def __init__(self, titulo, duracao, ano):
        self.titulo = titulo
        self.__duracao = duracao
        self.ano = ano
    def __str__(self):
        return f"O filme {self.titulo} tem duração de {self.__duracao} e é do ano de {self.ano}"