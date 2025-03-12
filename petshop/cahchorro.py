from animais import Animais
class Cachorro (Animais):
    def __init__(self, raca, cor, idade, nome, enfeite):
        super().__init__(raca, cor, idade, nome)
        self.enfeite = enfeite

    def exibir_cachorro (self):
        print(f'O cachorro {self.raca} é da cor {self.cor}, tem {self.idade}, chama {self.nome}e vai usar {self.enfeite}')
