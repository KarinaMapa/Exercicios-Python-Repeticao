maior = menor = 0
num_maior = num_menor = 0
for i in range(1,11):
    n = int(input('Número do aluno: '))
    altura = float(input('Altura do aluno: '))
    if i == 1:
        maior = menor = altura
        num_maior = num_menor = n
    else:
        if altura > maior:
            maior = altura
            num_maior = n
        elif altura < menor:
            menor = altura
            num_menor = n
print('Maior aluno {} - Código {}'.format(maior, num_maior))
print('Menor aluno {} - Código {}'.format(menor, num_menor))