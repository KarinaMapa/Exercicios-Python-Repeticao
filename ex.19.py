quant = int(input('Digite a quantidade de números do conjunto: '))
maior = soma = 0
menor = 1001

for i in range(0, quant):
    n = 1001
    while n > 1000 or n < 0:
        n = int(input('Número: '))
        if n > 1000 or n < 0:
            print('Número inválido')
    if 0 < n < 1000:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n

print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
print('Soma: {}'.format(soma))