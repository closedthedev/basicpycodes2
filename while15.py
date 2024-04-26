#praticando while 

import random 

números = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

num1 = random.choice(números)
num2 = random.choice(números)
resultado = 1
multiplicação = num1 * num2
tentativas = 0
print(multiplicação)
print('O PROGRAMA IRÁ SORTEAR 2 NÚMEROS DE 1 A 10 E MULTIPLICAR ELES. PODE SER O MESMO NÚMERO. TENTE ACERTAR O RESULTADO DA MULTIPLICAÇÃO DESSES 2 NÚMEROS')

while resultado != multiplicação:
    resultado = int(input('Tente acertar o resultado. : '))
    tentativas += 1

    if resultado == multiplicação:
        print(f'Na sua {tentativas}ª tentativa, você acertou. O resultado é {resultado}, proveniente de uma multiplicação entre {num1} e {num2} ')
