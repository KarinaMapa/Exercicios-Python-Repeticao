count1 = count2 = count3 = count4 = 0
n = 0
while n>=0:
    n = int(input('Digite um número positivo (Para parar digite um número negativo): '))
    if n in range(0,26):
        count1 += 1
    elif n in range(26, 51):
        count2 += 1
    elif n in range(51, 76):
        count3 += 1
    elif n in range(76, 101):
        count4 += 1
print('')
print('Intervalo 0-25 -  {} números digitados.'.format(count1))
print('Intervalo 26-50 -  {} números digitados.'.format(count2))
print('Intervalo 51-75 -  {} números digitados.'.format(count3))
print('Intervalo 76-100 -  {} números digitados.'.format(count4))