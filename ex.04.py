a = 80000
b = 200000
tx_a = 0.03
tx_b = 0.015

crescimento_a = a + (a * tx_a)
crescimento_b = b + (b * tx_b)
count = 1

while crescimento_a <= crescimento_b:
    crescimento_b += (crescimento_b*tx_b)
    crescimento_a += (crescimento_a*tx_a)
    count += 1

print('Mantidas as taxas de crescimento, o país A vai demorar %s anos para igualar/ultrapassar a população do país B.'%(count))
