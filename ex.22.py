n = int(input('Digite um número: '))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count +=1
if count >= 3:
    print('O número {} não é primo'.format(n))
    print('Ele é divisível pelos números:', end= ' ')
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=' ')
else:
    print('O número {} \033[31mé primo'.format(n))