n = int(input('Montar a tabuada do número: '))
c = int(input('Começar a tabuada no número: '))
f = int(input('Terminar a tabuada no número: '))
while c > f:
    print('Valor inválido, o valor inicial deve ser menor que o final')
    print('Digite novamente')
    c = int(input('Começar a tabuada no número: '))
    f = int(input('Terminar a tabuada no número: '))
else:
    print('')
    print('Tabuada do número {} começando pelo número {} e terminando no número {}'.format(n, c, f))
    for i in range(c, f+1):
        print('{} x {} = {}'.format(n, i, (n*i)))
