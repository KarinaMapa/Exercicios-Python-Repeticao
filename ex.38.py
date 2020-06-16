salario = float(input('Salário em 1996: R$ '))
reaj = 1.5
salario1996 = salario*(1+(reaj/100))
salario_atual = salario1996
reaj_atual = reaj
ano = int(input('Ano atual: '))
for i in range(1997, ano+1):
    reaj_atual *= 2
    salario_atual *= (1+(reaj_atual/100))

print('Em {} seu salário é de R$ {:.2f}'.format(ano, salario_atual))