class Onibus:
    def __init__(self, nome, empresa, rota, frequencia, tipo):
        self.nome = nome
        self.empresa = empresa
        self.rota = rota
        self.frequencia = frequencia
        self.tipo = tipo

    def __str__(self):
        return f"O onibus {self.nome} pertence a empresa {self.empresa} faz a rota {self.rota} com a frequencia de {self.frequencia} e é do tipo {self.tipo}"