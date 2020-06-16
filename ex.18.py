quant = int(input('Digite a quantidade de números do conjunto: '))
maior = menor = soma = 0
for i in range(1, quant+1):
    n = int(input('Número {}: '.format(i)))
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
print('Soma: {}'.format(soma))