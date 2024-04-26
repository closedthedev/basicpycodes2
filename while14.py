#praticando while, agora com uma forca melhorada

import random

palavras = ['GATO' , 'CACHORRO' , 'PÁSSARO' , 'RAPOSA' , 'BALEIA' , 'URSO']
palavra_usuário = ''
tentativas = 0

palavra_selecionada = random.choice(palavras)
print('O programa selecionará uma das 6 palavras seguintes e você tentará acertar qual palavra é. Máximo de 2 tentativas')
print(' , '.join(palavras))

while palavra_usuário != palavra_selecionada and tentativas < 2:
    palavra_usuário = str(input('Tente acertar qual palavra o programa sorteou: ')) .upper() .strip()
    tentativas += 1

    if palavra_usuário == palavra_selecionada:
        print(f'Com {tentativas} tentativa(s), você acertou!!')
        break

if tentativas == 2 and palavra_usuário != palavra_selecionada:
    print('Você ultrapassou o limite de tentativas.')


       
