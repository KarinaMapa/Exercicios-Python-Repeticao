quant = int(input('Quantidade de CDs comprada: '))
soma = 0
count = 0
for i in range(0, quant):
    valor = float(input('Valor pago pelo CD: R$ '))
    soma += valor
invest = soma
media = soma / quant
print('Valor médio pago em cada CD: R$ {:.2f}'.format(media))
print('Valor total investido: R$ {:.2f} '.format(invest))