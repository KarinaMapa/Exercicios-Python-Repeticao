eleitores = int(input('Número total de eleitores: '))
cand1 = cand2 = cand3 = 0
for i in range(0, eleitores):
    voto = int(input('''Vote em um dos candidatos abaixo:
                    1 - José
                    2 - Antonio
                    3 - Estevão
                     '''))
    while voto != 1 and voto != 2 and voto != 3:
        print('Opção inválida, escolhe entre 1, 2 ou 3')
        voto = int(input('''Vote em um dos candidatos abaixo:
                            1 - José
                            2 - Antonio
                            3 - Estevão
                             '''))
    if voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    else:
        cand3 += 1
print('''VOTOS:
CANDIDATO 1 - JOSÉ -> {} VOTOS,
CANDIDATO 2 - ANTONIO -> {} VOTOS
CANDIDATO 3 - ESTEVÃO -> {} VOTOS
'''.format(cand1, cand2, cand3))
