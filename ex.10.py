num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

while num2 < num1:
    print('Valor do segundo precisa ser maior que do primeiro')
    num2 = int(input('Segundo número: '))

for i in range(num1,(num2+1)):
    print(i, end=' ')