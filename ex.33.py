temperatura = float(input('Temperatura: '))
soma = maior = menor = temperatura
count = 1
continuar = ' '
while continuar not in 'SN':
    continuar = str(input('Deseja continuar? [S/N] ')).upper()
    while continuar == 'S':
        temperatura = float(input('Temperatura: '))
        soma += temperatura
        count += 1
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
media = soma/count
print('')
print('Média das temperaturas: {:.1f}ºC.'.format(media))
print('Menor temperatura: {} ºC'.format(menor))
print('Maior temperatura: {} ºC'.format(maior))