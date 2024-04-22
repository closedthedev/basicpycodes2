#praticando for com várias variáveis dentro dele, dessa vez pegando um número X de pessoas e vendo quem tem o maior Q.I, separando entre homens e mulheres

qnt_pessoas = int(input('Digite quantas pessoas você quer analisar: '))

maiorqihomem = 0
maiorqimulher = 0
nome_maiorhomem = ''
nome_maiormulher = ''
idade_maiorhomem = 0
idade_maiormulher = 0

for i in range(1, qnt_pessoas + 1):
    print(f'{i}ª pessoa')
    nome = str(input('Nome: ')) .title()
    sexo = str(input('Sexo. M/F: '))  .strip() .upper()
    idade = int(input('Idade: '))
    qi = int(input('QI: '))
    
    if sexo == 'M' and qi > maiorqihomem:
        maiorqihomem = qi
        nome_maiorhomem = nome
        idade_maiorhomem = idade
    elif sexo == 'F' and qi > maiorqimulher:
        maiorqimulher = qi
        nome_maiormulher = nome
        idade_maiormulher = idade

print(f'Você escolheu analisar {qnt_pessoas} pessoas. Entre elas, o homem com o maior QI se chama {nome_maiorhomem}, ele tem {idade_maiorhomem} anos de idade e o QI dele é de {maiorqihomem}. A mulher com o maior QI se chama {nome_maiormulher}, ela tem {idade_maiormulher} anos de idade e o seu QI é de {maiorqimulher}.')