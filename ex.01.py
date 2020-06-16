nota = int(input('Digite uma nota entre 0 e 10: '))
while nota not in range(0,11):
    print('Nota inválida!')
    nota = int(input('Digite uma nota entre 0 e 10: '))
print('Nota %s'%(nota))