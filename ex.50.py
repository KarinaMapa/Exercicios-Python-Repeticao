termo = int(input('Digite até qual termo a sequencia deve ser somada: '))
soma = 0
for i in range(1, termo+1):
    if i == 1:
        n = 1 / 1
    else:
        n = 1 / i
    soma += n

print('Soma: {:.2f}'.format(soma))
