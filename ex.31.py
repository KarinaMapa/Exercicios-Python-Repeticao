x = float(input('Produto 1 (Para finalizar digite 0): R$ '))
soma = x
quant = 2
while x != 0:
    x = float(input('Produto {} (Para finalizar digite 0): R$ '.format(quant)))
    quant += 1
    soma += x
print('O valor total da compra deu R$ {:.2f}'.format(soma))
troco = ' '
while troco not in 'SN':
    troco = str(input('Precisa de troco? [S/N] ')).upper()
    if troco == 'S':
        nota = float(input('Qual valor você têm? R$ '))
        while nota < soma:
            print('O valor é menor que o total, precisa adicionar mais dinheiro, por favor')
            nota = float(input('Qual valor você têm? R$ '))
        else:
            valorfinal = nota - soma
            print('Seu troco é de R$ {:.2f}'.format(valorfinal))
            print('Obrigado pela compra!')
    elif troco == 'N':
        print('Obrigado pela compra!')