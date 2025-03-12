from pessoas import Pessoas


class Professores(Pessoas):
    def __init__(self, nome, cpf, nascimento, telefone, materia):
        super().__init__(nome, cpf, nascimento, telefone)
        self.materia = materia

    def exibir_professor(self):
        print(f'O professor {self.nome} do cpf {self.cpf}, seu numero de telefone é {self.telefone}'
              f'esta dando aula na materia de {self.materia}')
