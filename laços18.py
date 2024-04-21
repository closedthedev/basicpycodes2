#praticando for, com várias variáveis. Agora comparando carros, para ver qual é mais rápido e qual é o menos rápido.

qnt_carros = int(input('Digite a quantidade de carros que quer analisar: '))

for i in range(1, qnt_carros + 1):
    print(f'{i}ª carro')
    modelo = str(input('Digite o modelo do carro: '))
    marca = str(input('Digite a marca do carro: '))
    velocidade_max = float(input('Digite a velocidade máxima do carro: '))

    if i == 1:
        modelo_maisrapido = modelo
        marca_maisrapida = marca
        maisrapido = velocidade_max
        modelo_menosrapido = modelo
        marca_menosrapida = marca
        menosrapido = velocidade_max
    else:
        if velocidade_max > maisrapido:
            modelo_maisrapido = modelo
            marca_maisrapida = marca
            maisrapido = velocidade_max

        if velocidade_max < menosrapido:
            modelo_menosrapido = modelo
            marca_menosrapida = marca
            menosrapido = velocidade_max

print(f'Você escolheu analisar {qnt_carros} carros diferentes. Entre eles, o mais rápido é o {modelo_maisrapido} da marca {marca_maisrapida}. Ele consegue chegar em até {maisrapido:.2f} km/h. Enquanto o menos rápido é o {modelo_menosrapido} da marca {marca_menosrapida} que só consegue chegar até {menosrapido:.2f} km/h')