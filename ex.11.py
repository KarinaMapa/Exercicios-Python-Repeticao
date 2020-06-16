soma = 0

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

while num2 < num1:
    print('Valor do segundo precisa ser maior que do primeiro')
    num2 = int(input('Segundo número: '))

print('Os valores entre os números digitados foram: ')
for i in range(num1+1,(num2)):
    print((i), end=' ')
    soma += i
print('\nA soma dos algarismos é {}'.format(soma))
