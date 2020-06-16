quant = int(input('Quantidade de itens comprados: '))
print('TABELA DE PREÇOS')
for i in range(1, 51):
    print('{}  -   R$ {:.2f}'.format(i, (i*1.99)))
print('Valor total a pagar: R$ {:.2f}'.format(quant*1.99))