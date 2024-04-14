#alistamento militar

nome = str(input('Digite o seu nome: '))
idade = int(input('Digite a sua idade: '))
alistou = int(input('Você já se alistou? Digite 1 para sim e 2 para não: '))
tempo_certo = 18

if idade < tempo_certo and alistou == 2:
    print(f'Olá, {nome}! Você tem {idade} anos. Ainda faltam {abs(idade - tempo_certo)} anos para você se alistar.')

elif idade < tempo_certo and alistou == 1:
    print(f'Olá, {nome}! Você tem {idade} anos. Então é IMPOSSÍVEL você já ter se alistado.')

elif idade > tempo_certo and alistou == 2:
    print(f'Olá, {nome}! Você já ultrapassou o prazo. O senhor está atrasado em {abs(idade - tempo_certo)} anos.')

elif idade == tempo_certo and alistou == 2:
    print(f'Olá, {nome}! Você se alista esse ano. Te vemos em breve!') 

else: print('Você já se alistou e está em dia com o exército brasileiro!')
    
