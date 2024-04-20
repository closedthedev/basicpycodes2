
num = int(input('Quantos integrantes do grupo você quer verificar se são velhos ou novos? '))
jovens = 0
velhos = 0

for i in range(1 , num + 1 , 1):
    ano_nascimento = int(input('Digite o ano de nascimento de um integrante do grupo: '))
    if ano_nascimento < 2000:
        velhos += 1
    else:
        jovens += 1

print(f'Você solicitou {num} integrantes do grupo. Desses integrantes solicitados, {jovens} são jovens e {velhos} são velhos.')