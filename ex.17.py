n = int(input('Digite um número: '))
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