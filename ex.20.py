n = int(input('Digite um número: '))
while True:
    if n > 0 and n <= 16:
        print('~'*85)
        print('FATORIAL DE {}'.format(n))
        print('{}! = '.format(n), end=' ')
        fatorial = 1
        for i in range(n, 0, -1):
            print('{} '.format(i), end=' ')
            fatorial *= (i)
            if i > 1:
                print('x ', end=' ')
            else:
                print('= ', end=' ')
        print(fatorial)
        print('~'*85)
        break
    elif n >= 16:
        while n >= 16:
            print('Valor inválido, valor precisa ser menor que 16')
            n = int(input('Digite um número: '))
    elif n < 0:
        while n < 0:
            print('Valor precisa ser positivo')
            n = int(input('Digite um número: '))
print('Fim')