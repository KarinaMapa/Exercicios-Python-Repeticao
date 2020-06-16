n = int(input('Digite um número: '))
count = quantdiv = 0
print('Os números abaixo entre 1 e {} são primos:'.format(n))
while n > 0:
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            quantdiv += 1
        else:
            quantdiv += 1
    if count >= 3:
        False
    else:
        print(n, end=' ')
    n -= 1
    count = 0
print('\nForam feitas {} divisões para encontrá-los'.format(quantdiv))