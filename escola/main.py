from aluno import aluno
aluno1 = aluno(matricula="001", nome='Pedro', media=9.0, cpf='112.234.556-98', telefone='11334-9988')
aluno2 = aluno(matricula='002', nome='Nicolas', media=6.0, cpf='123.456.789-00', telefone='1223-4456')

print(f'\nO aluno {aluno1.nome} está aprovado com média {aluno1.media}')

aluno1.exibirmatricula()
aluno1.exibircpf()

print(f'\nO aluno{aluno2.nome} está reprovado com média {aluno2.media}')
aluno2.exibirmatricula()
aluno2.exibircpf()