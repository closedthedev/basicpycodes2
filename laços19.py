#praticando for com várias variáveis, agora medindo a altura de X pessoas e dizendo qual é o maior, e qual é o menor. entre homens e mulheres

qnt_pessoas = int(input('Digite a quantidade de pessoas que quer analisar: '))


maiornome_homem = ''
maioraltura_homem = 0
maioridade_homem = 0

maiornome_mulher = ''
maioraltura_mulher = 0
maioridade_mulher = 0

for i in range(1, qnt_pessoas + 1):
    print(f'{i}ª pessoa')
    nome = input('Nome: ')
    sexo = input('Sexo. M/F: ').strip().upper()
    altura = float(input('Altura: '))
    idade = int(input('Idade: '))

   
    if sexo == 'M' and altura > maioraltura_homem:
        maiornome_homem = nome
        maioraltura_homem = altura
        maioridade_homem = idade

    
    elif sexo == 'F' and altura > maioraltura_mulher:
        maiornome_mulher = nome
        maioraltura_mulher = altura
        maioridade_mulher = idade

print(f'Você quis analisar {qnt_pessoas}. Entre elas: O homem mais alto se chama {maiornome_homem} ele tem {maioridade_homem} anos e tem {maioraltura_homem:.2f}m de altura. A mulher mais alta se chama {maiornome_mulher} ela tem {maioridade_mulher} anos e tem {maioraltura_mulher:.2f}m de altura.')