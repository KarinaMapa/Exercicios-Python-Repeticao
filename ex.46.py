nome = str(input('Atleta: ')).capitalize()
lista = []
maior = menor = media = soma = 0
for i in range(1, 6):
    salto = float(input('{}º salto:  '.format(i)))
    lista.append(salto)
    soma += salto
    if i == 1:
        maior = menor = salto
    else:
        if salto > maior:
            maior = salto
        if salto < menor:
            menor = salto
media = (soma - maior - menor) / 3

print(' ')
print('Melhor salto: {} m'.format(maior))
print('Pior salto: {} m'.format(menor))
print('Média dos demais saltos: {:.1f} m'.format(media))
print(' ')
print('''Resultado final:
{} : {:.1f} m'''.format(nome, media))