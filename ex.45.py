acertos = soma = 0
count = 0
maior = menor = alunos = media = 0
continuar = ' '
while continuar not in 'SN':
    continuar = str(input('Deseja digitar um novo gabarito? [S/N] ')).upper()
    if continuar == 'N':
        break
    while continuar == 'S':
        alunos += 1
        while count < 10:
            gabarito = str(input('Opção correta: ')).upper()
            if gabarito in 'ABCDE':
                count += 1
                if count == 1:
                    if gabarito == 'A':
                        acertos += 1
                elif count == 2:
                    if gabarito == 'B':
                        acertos += 1
                elif count == 3:
                    if gabarito == 'C':
                        acertos += 1
                elif count == 4:
                    if gabarito == 'D':
                        acertos += 1
                elif count == 5:
                    if gabarito == 'E':
                        acertos += 1
                elif count == 6:
                    if gabarito == 'E':
                        acertos += 1
                elif count == 7:
                    if gabarito == 'D':
                        acertos += 1
                elif count == 8:
                    if gabarito == 'C':
                        acertos += 1
                elif count == 9:
                    if gabarito == 'B':
                        acertos += 1
                elif count == 10:
                    if gabarito == 'A':
                        acertos += 1
            elif gabarito not in 'ABCDE':
                print('Opção inválida')
        soma += acertos
        if alunos == 1:
            maior = menor = acertos
        else:
            if acertos > maior:
                maior = acertos
            if acertos < menor:
                menor = acertos
        continuar = str(input('Deseja digitar um novo gabarito? [S/N] ')).upper()
        count = 0
        acertos = 0

media = soma/alunos
print('Acertos: {}'.format(soma))
print('Total de alunos: {}'.format(alunos))
print('Maior nota: {}'.format(maior))
print('Menor nota: {}'.format(menor))
print('Média: {:.2f}'.format(media))