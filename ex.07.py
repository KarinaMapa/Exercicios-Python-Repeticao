maior = 0
n = int(input('Número: '))
for i in range(0,4):
    if i == 0:
        maior = n
    n = int(input('Número: '))
    if n > maior:
        maior = n

print('O maior valor digitado foi %s'%(maior))