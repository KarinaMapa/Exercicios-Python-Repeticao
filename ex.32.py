n = int(input('Número que deseja saber o fatorial: '))
print('{}! = '.format(n), end=' ')
fatorial = 1
for i in range((n), 0, -1):
    print(i, end='')
    if i > 1:
        print(' . ', end=' ')
    else:
        print(' = ', end=' ')
    fatorial *= i
print(fatorial)