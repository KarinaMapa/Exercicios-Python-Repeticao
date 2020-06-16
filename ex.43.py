print('Tabela de preços:')
print('{:^15}  {:>6}   {:>5}'.format('Especificação', 'Código', 'Preço'))
print('{:^15}  {:^6}   R${:^5}'.format('Cachorro-quente', 100, 1.20))
print('{:^15}  {:^6}   R${:^5}'.format('Bauru Simples', 101, 1.30))
print('{:^15}  {:^6}   R${:^5}'.format('Bauru com ovo', 102, 1.50))
print('{:^15}  {:^6}   R${:^5}'.format('Hambúrguer', 103, 1.20))
print('{:^15}  {:^6}   R${:^5}'.format('Cheeseburguer', 104, 1.30))
print('{:^15}  {:^6}   R${:^5}'.format('Refrigerante', 105, 1.00))
print('~'*30)
valor = valor_total = quant = codigo = produto = preco = 0
continuar = ' '
while continuar not in 'SN':
    continuar = str(input('Deseja alguma opção? [S/N] ')).upper()
    if continuar == 'N':
        break
    while continuar == 'S':
        codigo = int(input('Qual código deseja? '))
        quant = int(input('Qual quantidade desja? '))
    #
        if codigo == 100:
            produto = 'Cachorro-quente'
            preco = 1.20
            valor = quant * preco
        elif codigo == 101:
            produto = 'Bauru Simples'
            preco = 1.30
            valor = quant*preco
        elif codigo == 102:
            produto = 'Bauru com ovo'
            preco = 1.50
            valor = quant*preco
        elif codigo == 103:
            produto == 'Hambúrguer'
            preco = 1.20
            valor = quant*preco
        elif codigo == 104:
            produto = 'Cheeseburguer'
            preco = 1.30
            valor = quant*preco
        elif codigo == 105:
            produto = 'Refrigerante'
            preco = 1.00
            valor = quant*preco
        valor_total+= valor
        print('~'*45)
        print('Pedido -> {} {} x R$ {} = {:.2f}'.format(quant, produto, preco, valor))
        print('~'*45)
        continuar = str(input('Deseja alguma opção? [S/N] ')).upper()

print('~'*50)
print('Valor total: R$ {:.2f}'.format(valor_total))
print('~'*50)