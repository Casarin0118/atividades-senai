class aluno:
    def __init__(self, matricula, nome, cpf, telefone):
        self.__matricula = matricula
        self.nome = nome
        self.media = 0
        self.__cpf = cpf
        self.telefone = telefone

    def exibirmatricula(self):
        print(f'matricula {self.__matricula}')

    def exibircpf(self):
        print(f'matricula {self.__cpf}')