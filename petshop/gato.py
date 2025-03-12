from animais import Animais


class Gato(Animais):
    def __init__(self, raca, cor, idade, nome, coleira):
        super().__init__(raca, cor, idade, nome)
        self.coleira = coleira

    def exibir_cachorro(self):
        print(
            f'O cachorro {self.raca} é da cor {self.cor}, tem {self.idade}, chama {self.nome}e vai usar {self.coleira}')
