nome = str(input('Atleta: ')).capitalize()
lista = []
maior = menor = soma = media = 0
for i in range(1, 8):
    nota = float(input('Nota {}: '.format(i)))
    soma += nota
    if i == 1:
        maior = menor = nota
    else:
        if nota > maior:
            maior = nota
        if nota < menor:
            menor = nota
media = (soma - maior - menor)/ 5
print(' ')
print('Resultado final:')
print('Atleta: {}'.format(nome))
print('Melhor nota: {}'.format(maior))
print('Pior nota: {}'.format(menor))
print('Média: {:.1f}'.format(media))