nome = str(input('Nome: '))
while len(nome) <= 3:
    print('Nome deve ter mais de 3 caracteres')
    nome = str(input('Nome: '))

idade = int(input('Idade: '))
while idade not in range(0,151):
    print('A idade deve estar entre 0 e 150, idade inválida')
    idade = int(input('Idade: '))

salario = float(input('Salário: R$  '))
while salario <= 0:
    print('Salário precisa ser maior que zero.')
    salario = float(input('Salário: R$ '))

sexo = str(input('Sexo [F/M]: ')).upper()
while sexo not in 'FM':
    print('Opção inválida')
    sexo = str(input('Sexo [F/M]: ')).upper()

estado_civil = str(input('Estado civil: [S - SOLTEIRO], [C - CASADO], [V - VIÚVO], [D - DIVORCIADO] ')).upper()
while estado_civil not in 'SCVD':
    print('Opção inválida!')
    estado_civil = str(input('Estado civil: [S - SOLTEIRO], [C - CASADO], [V - VIÚVO], [D - DIVORCIADO] ')).upper()
if estado_civil == 'S':
    estado_civil = 'Solteiro'
elif estado_civil == 'C':
    estado_civil = 'Casado'
elif estado_civil == 'V':
    estado_civil = 'Viúvo'
elif estado_civil == 'D':
    estado_civil = 'Divorciado'

print('')
print('Dados pessoais:')
print('')
print('Nome: %s'%(nome.capitalize()))
print('Idade: %s'%(idade))
print('Salário: R$ {:.2f}'.format(salario))
print('Estado civil: %s'%(estado_civil))