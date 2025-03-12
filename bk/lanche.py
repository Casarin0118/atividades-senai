class Lanche:
    def __init__(self, nome, ingredientes, valor):
        self.nome = nome
        self.__ingredientes = ingredientes
        self.valor = valor
    def __str__(self):
        return f"O lanche {self.nome} é feito com: \n {self.__ingredientes} \n e custa: --- R${self.valor}---"