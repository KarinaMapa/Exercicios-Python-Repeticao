valor = float(input('Preço do pão: R$ '))
print('Tabela de Preços')
for i in range(1, 51):
    print('{}  -  R$ {:.2f}'.format(i, (i*valor)))