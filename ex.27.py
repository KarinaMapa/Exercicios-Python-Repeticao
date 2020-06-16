import math
turmas = int(input('Quantidade de turmas: '))
soma = 0
for i in range(1,turmas+1):
    alunos = int(input('Quantidade de alunos na turma {}: '.format(i)))
    while alunos > 40:
        print('As turmas devem ter menos de 40 alunos cada')
        alunos = int(input('Quantidade de alunos na turma {}: '.format(i)))
    if alunos <= 40:
        soma += alunos
media = soma // turmas
math.ceil(media)
print('A média de alunos por turma é {}'.format(media))