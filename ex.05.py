a = int(input('Qual o tamanho da população da cidade A ? '))
while a <= 0:
    print('Opção inválida')
    a = int(input('Qual o tamanho da população da cidade A ? '))

b = int(input('Qual o tamanho da população da cidade B? '))
while b <=0:
    print('Opção inválida')
    b = int(input('Qual o tamanho da população da cidade B? '))

tx_a = int(input('Qual a taxa de crescimento da cidade A? '))
while tx_a not in range(0,101):
    print('Opção inválida')
    tx_a = int(input('Qual a taxa de crescimento da cidade A?'))

tx_b = int(input('Qual a taxa de crescimento da cidade B? '))
while tx_b not in range(0,101):
    print('Opção inválida')
    tx_b = int(input('Qual a taxa de crescimento da cidade B?'))

crescimento_a = a + (a * (tx_a/100))
crescimento_b = b + (b * (tx_b/100))
count = 1

while crescimento_a <= crescimento_b:
    crescimento_b += (crescimento_b*(tx_b/100))
    crescimento_a += (crescimento_a*(tx_a/100))
    count += 1

print('Mantidas as taxas de crescimento, o país A vai demorar %s anos para igualar/ultrapassar a população do país B.'%(count))
