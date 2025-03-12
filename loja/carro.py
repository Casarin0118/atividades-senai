from veiculos import Veiculos
class Carro (Veiculos):
    def __init__(self, rodas, assentos, valor, km, nome, potencia, ano):
        super().__init__(rodas, assentos, valor, km, potencia, ano)
        self.nome = nome

    def exibir_dados(self):
        print(f'o veiculo {self.nome} possui {self.rodas} rodas, {self.assentos} assentos, por apenas R${self.valor}, e possui {self.km}km rodados')