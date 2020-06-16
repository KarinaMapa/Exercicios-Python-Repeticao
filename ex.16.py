anterior = 0
proximo = 1
resultado = 0
print('')
print('SEQUENCIA DE FIBONACCI: ')
print('0 1', end=' ')
while resultado <= 500:
    resultado = anterior + proximo
    anterior = proximo
    proximo = resultado
    print(resultado, end=' ')
print('')
