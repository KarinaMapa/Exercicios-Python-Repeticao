idade = int(input('Qual sua idade? '))
soma = idade
c = 1
continuar = ' '
while continuar not in 'SN':
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    while continuar == 'S':
        idade = int(input('Digite a sua idade: '))
        c += 1
        soma += idade
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    else:
        if continuar == 'N':
            break
media = soma / c
print('A média das idades é {:.1f}'.format(media))
if 0 <= media <= 25:
    print('Você pertence a uma turma JOVEM!')
elif 26 <= media <= 60:
    print('Você pertence a uma turma ADULTA.')
else:
    print('Você pertence a uma turma IDOSA.')