n = int(input('Digite um número: '))
count = 0
print('')
print('Os valores abaixo entre 1 e {} são primos: '.format(n))
while n > 0:
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count >= 3:
        False
    else:
        print('{}'.format(n),end=', ')
    n -= 1
    count = 0