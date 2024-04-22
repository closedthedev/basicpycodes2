#praticando while

nome = ''
tentativas = 0

while nome != 'Luiz':
    nome = str(input('Digite seu nome: ')) .title() .strip()
    tentativas += 1

print(f'Você teve {tentativas} tentativas até acertar o nome.')