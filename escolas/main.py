from professores import Professores
from alunos import Alunos

aluno1 = Alunos(nome='pedro', cpf='12345678900', nascimento='2007', telefone='1998765678', ano='3°B')
aluno2 = Alunos(nome='Gabriel', cpf='0987654311', nascimento='2007', telefone='1987654567', ano='3°B')

professores1 = Professores(nome='Alessandro', cpf='67865478298', nascimento='1980', telefone='1977864567', materia='matematica')
professores2 = Professores(nome='fabio', cpf='56743256788', nascimento='1979', telefone='1955678987', materia='historia')

aluno1.exibir_aluno()
aluno2.exibir_aluno()
professores1.exibir_professor()
professores2.exibir_professor()