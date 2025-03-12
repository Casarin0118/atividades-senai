class Receita:
    def __init__(self, nome, ingredientes, tempo, dificuldade, porcoes):
        self.nome = nome
        self.__ingredientes = ingredientes
        self.tempo = tempo
        self.dificuldade = dificuldade
        self.porcoes = porcoes
    def __str__(self):
        return f"A receita {self.nome} leva os seguintes ingredientes \n {self.__ingredientes} \n tempo de preparo: {self.tempo} serve {self.porcoes} porções e é de dificuldade {self.dificuldade}"