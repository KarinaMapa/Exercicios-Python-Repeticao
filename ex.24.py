quant = int(input('Quantos números deseja digitar? '))
soma = 0
for i in range(0, quant):
    n = int(input('Digite os números desejados para saber a média aritmética: '))
    soma += n
media = soma / quant
print('A média aritmética dos números digitados é {:.2f}'.format(media))