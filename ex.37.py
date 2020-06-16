magro = gordo = 0
maior = menor = 0
codmagro = codgordo = codmaior = codmenor = 0
somap = soma_alt = 0
count = 0
codigo = ''
while codigo != 0:
    codigo = int(input('Código (Para parar digite 0): '))
    if codigo == 0:
        break
    else:
        count += 1
        altura = float(input('Altura: '))
        soma_alt += altura
        peso = float(input('Peso: '))
        somap += peso
        if count == 1:
            menor = maior = altura
            magro = gordo = peso
            codmaior = codmenor = codigo
            codgordo = codmagro = codigo
        else:
            if altura >= maior:
                maior = altura
                codmaior = codigo
            elif altura <= menor:
                menor = altura
                codmenor = codigo

            if peso <= magro:
                magro = peso
                codmagro = codigo
            elif peso >= gordo:
                gordo = peso
                codgordo = codigo
mediap = somap / count
media_alt = soma_alt / count
print('')
print('Maior aluno: {} m - Código {}'.format(maior, codmaior))
print('Menor aluno {} m - Código {}'.format(menor, codmenor))
print('Menor peso {} Kg - Código {}'.format(magro, codmagro))
print('Maior peso {} Kg - Código {}'.format(gordo, codgordo))
print('Média de peso {:.1f} Kg'.format(mediap))
print('Média de altura {:.2f} m'.format(media_alt))
