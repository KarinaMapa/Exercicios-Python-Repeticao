n = int(input('Informe um número entre 1 a 10 para ver sua tabuada: '))
while n not in range(1,11):
    print('Número inválido')
    n = int(input('Informe um número entre 1 a 10 para ver sua tabuada: '))
for i in range(1,11):
    print('{} x {} = {}'.format(i, n, (i*n)))
