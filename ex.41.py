divida = float(input('Valor da dívida: R$ '))
juros = 0
print('{:^15}  {:>15}  {:>22}   {:>16}'.format('Valor da Dívida', 'Valor dos Juros', 'Quantidade de Parcelas', 'Valor da Parcela'))
for i in [1, 3, 6, 9, 12]:
    valor_juros = divida*(juros/100)
    valor_divida = divida + valor_juros
    valor_parcela = valor_divida/i
    if i == 1:
        juros = 10
    else:
        juros += 5
    print('R${:^15.2f} R${:^15.2f}  {:^22} R${:^16.2f}'.format(valor_divida, valor_juros, i, valor_parcela))