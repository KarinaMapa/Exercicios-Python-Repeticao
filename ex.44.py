print('{:^10}  {:>10}'.format('VOTO', 'CANDIDATO'))
print('{:^10}   {:^10}'.format(1, 'JOSÉ'))
print('{:^10}   {:^10}'.format(2, 'JOÃO'))
print('{:^10}   {:^10}'.format(3, 'MARIA'))
print('{:^10}   {:^10}'.format(4, 'ANTONIO'))
print('{:^10}   {:^10}'.format(5, 'VOTO NULO'))
print('{:^10}   {:^10}'.format(6, 'VOTO EM BRANCO'))
print(' ')
count1 = count2 = count3 = count4 = count5 = count6 = soma = 0
voto = ' '
while voto != 0:
    voto = int(input('Voto: '))
    if voto < 1 or voto > 6:
        print('Valor inválida, digite uma das opções mencionadas')
        soma -= 1
    elif voto == 1:
        count1 += 1
    elif voto == 2:
        count2 += 1
    elif voto == 3:
        count3 += 1
    elif voto == 4:
        count4 += 1
    elif voto == 5:
        count5 += 1
    elif voto == 6:
        count6 += 1
    soma += 1
print('''Total de votos:
      1 - JOSÉ -> {} VOTOS
      2 - JOÃO -> {} VOTOS
      3 - MARIA -> {} VOTOS
      4 - ANTONIO -> {} VOTOS
      5 - VOTO NULO -> {} VOTOS
      6 - VOTO EM BRANCO -> {} VOTOS
        '''.format(count1, count2, count3, count4, count5, count6))
perc_nulos = (count5 / soma)*100
perc_brancos = (count6/ soma)*100
print('PERCENTUAL VOTOS NULOS: {:.2f} %'.format(perc_nulos))
print('PERCENTUAL VOTOS BRANCOS: {:.2F} %'.format(perc_brancos))