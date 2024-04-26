#praticando while

cont = 1
multiplicação = 1
tentativas = 0

print('A cada número que você digitar, vou multiplicar ele pelo próximo. Vamos ver em quantas tentativas você consegue chegar em 10000.')

while multiplicação <= 10000:
    num = int(input('Digite um número: '))
    multiplicação = multiplicação * num
    tentativas += 1 
    print(f'A multiplicação está em: {multiplicação}')

if multiplicação >= 10000:
    print(f'Você ultrapassou os 10mil com {tentativas} tentativas!')