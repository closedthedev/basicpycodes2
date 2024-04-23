#praticando while, dessa vez com um menu de interação gigantesco

escolha = 0


while escolha != 5:
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    escolha = int(input('>>>>>>Qual é a sua opção? '))
    
    if escolha == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')

    elif escolha == 2:
        multiplicação = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {multiplicação}')

    elif escolha == 3:
        print(f'Entre {n1} e {n2}, o maior número é o', max(n1, n2))

    elif escolha == 4: 
        print('Escolha os números novamente')

    elif escolha == 5:
        print('Programa finalizado.')