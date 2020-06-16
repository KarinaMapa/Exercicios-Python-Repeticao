soma = 0
termo = int(input('Deseja ver a série até qual termo? '))
print('')
print('S = ', end='')
for i in range(1, termo+1):
    if i == 1:
        print('{}/{}'.format(i,i), end=' + ')
    else:
        n = i+(i-1)
        soma += (i/n)
        print('{}/{}'.format(i, n), end='')
        if i == termo:
            print(end='.')
        else:
            print(end=' + ')

print('\nSoma = {:.2f}'.format(soma + 1))