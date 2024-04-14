#convertendo número inteiro para binário , octal e hexadecimal, de acordo com a escolha do usuário

número = int(input('Digite o número inteiro que queira converter: '))
escolha_usuário = int(input('Escolha qual das 3 opções você quer converter. 1 para binário, 2 para octal e 3 para hexadecimal: '))
binário = bin(número)
octal = oct(número)
hexadecimal = hex(número)

if escolha_usuário == 1:
    print(f'Você digitou o número {número} e escolheu converter ele para binário. Ele em binário fica: {binário} ')

elif escolha_usuário == 2:
    print(f'Você digitou o número {número} e escolheu converter ele para octal. Ele em octal fica: {octal} ')

elif escolha_usuário == 3:
    print(f'Você digitou o número {número} e escolheu converter ele para hexadecimal. Ele em hexadecimal fica: {hexadecimal} ')
