soma = count = 0
for i in range(0,5):
    num = int(input('Digite um número: '))
    count += 1
    soma += num
media = soma/count
print('De acordo com os números digitados a soma foi {} e a média foi {}'.format(soma, media))
