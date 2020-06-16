anterior = 0
proximo = 1
result = 0
termo = int(input('Digite até qual termo deseja ver a sequencia de Fibonacci: '))
while termo <= 0:
    print('O termo deve ser positivo')
    termo = int(input('Digite até qual termo deseja ver a sequencia de Fibonacci: '))
print('')
print('SEQUENCIA DE FIBONACCI:', end=' ')
print('0 1', end=' ')
for i in range(1, termo-1):
    result = anterior + proximo
    anterior = proximo
    proximo = result
    print('{}'.format(result), end=' ')
print('')
