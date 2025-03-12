class Cidade:
    def __init__(self, nome, estado_pais, populacao, pontos_turisticos,clima):
        self.nome = nome
        self.estado_pais = estado_pais
        self.__populacao = populacao
        self.pontos_turisticos = pontos_turisticos
        self.clima = clima

    def __int__(self):
        return f"A cidade {self.nome} pertence ao estado de {self.estado_pais} contem {self.__populacao} habitantes, possui um clima bem {self.clima} e os pontos turisticos sao {self.pontos_turisticos}"