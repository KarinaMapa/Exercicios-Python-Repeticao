n = int(input('Digite um número: '))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count >= 3:
    print('Número NÃO é primo')
else:
    print('Número primo')