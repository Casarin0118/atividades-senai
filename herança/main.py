from vendedor import vendedor
from gerente import gerente

funcionario1 = vendedor(nome='Vendedor01', email ='vendedor01@gmail.com', salario_base=1414.50, comissao=0.1)
gerente1 = gerente(nome='Gerente01', email='gerente01@gmail.com', salario_base=2500, comissao=0.4)

funcionario1.exibir_detalhes()
gerente1.exibir_detalhes()