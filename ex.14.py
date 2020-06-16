countpar = countimpar = 0
for i in range(1,11):
    n = int(input('Número inteiro: '))
    if n % 2 == 0:
        countpar += 1
    else:
        countimpar += 1
print('Foram digitados {} números PARES e {} números ÍMPARES.'.format(countpar, countimpar))
