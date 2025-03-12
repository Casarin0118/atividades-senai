class funcionario:
    def __init__(self, nome, email, salario_base):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base

    def exibir_detalhes(self):
        print(f'O funcionario {self.nome} \ntem o edereço de email {self.email} e \nseu salário base é {self.salario_base}')
