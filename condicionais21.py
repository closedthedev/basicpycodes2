#gerenciador de descontos, de acordo com a forma de pagamento desejada

valor_total = float(input('Digite o valor total da compra: R$'))
forma_pagamento = int(input('Digite a forma de pagamento. 1 para dinheiro e 2 para cartão:'))
vezes = int(input('Digite em quantas vezes você deseja parcelar:'))

if forma_pagamento == 1:
    print(f'O valor total da compra, com os desconto de 10% ficou em: R${abs((valor_total * 0.10) - valor_total) :.2f}')

elif forma_pagamento == 1 and vezes >= 2:
     print('Nós não aceitamos parcelamento no dinheiro.')

elif forma_pagamento == 2 and  vezes == 1:
     print(f'O valor total da compra, com os desconto de 5% ficou em: R${abs((valor_total * 0.05) - valor_total) :.2f}')

elif forma_pagamento == 2 and  vezes == 2:
     print(f'Em 2x no cartão nós não damos desconto e nem aplicamos juros. O valor da sua compra ficou em R${valor_total}')

elif forma_pagamento == 2 and vezes > 2:
     print(f'Acima de 2x nós acrescentamos um juros de 20%. Logo, o valor da sua compra ficou em R${valor_total + (valor_total * 0.2)}')


