soma = somaacid_maior = somaacid_menor = 0
count = 0
for i in range(1,6):
    cod = int(input('Código da Cidade: '))
    veic_passeio = int(input('Número de veículos de passeio (em 1999): '))
    soma += veic_passeio
    acid_maior = int(input('Maior número de acidentes de trânsito com vítimas (em 1999): '))
    acid_menor = int(input('Menor número de acidentes de trânsito com vítimas (em 1999): '))
    if veic_passeio < 2000:
        somaacid_maior += acid_maior
        somaacid_menor += acid_menor
        count += 1

media = soma/5
media_acid = (somaacid_maior + somaacid_menor)/count
print('Média de veículos nas cinco cidades juntas: {:.0f}'.format(media))
print('Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {:.0f}'.format(media_acid))
