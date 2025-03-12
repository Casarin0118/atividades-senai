from pessoas import Pessoas

class Alunos (Pessoas):
    def __init__(self, nome, cpf, nascimento, telefone, ano):
        super().__init__(nome, cpf, nascimento, telefone)
        self.ano = ano

    def exibir_aluno(self):
        print(f'O aluno {self.nome} do cpf {self.cpf}, seu numero de telefone é {self.telefone}'
              f'esta no ano {self.ano}')
