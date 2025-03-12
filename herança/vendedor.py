from funcionario import funcionario

class vendedor(funcionario):
    def __init__(self, nome, email, salario_base, comissao):
        super().__init__(nome, email, salario_base)
        self.comissao = comissao

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f'A comissão do vendedor é {self.comissao}')