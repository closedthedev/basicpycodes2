#pedra, papel e tesoura

import random

escolhas = ['Pedra' , 'Papel' , 'Tesoura']
escolha_usuário = str(input('Pedra, Papel ou Tesoura. Qual você escolhe? ')).strip() .title()

escolha_programa = random.choice(escolhas)

if escolha_programa == escolha_usuário:
    print(f'Empate! Você e o programa escolheram {escolha_programa}!')

elif escolha_programa == 'Tesoura' and escolha_usuário == 'Papel':
    print(f'O programa venceu. Ele escolheu {escolha_programa} e você escolheu {escolha_usuário}.')

elif escolha_programa == 'Pedra' and escolha_usuário == 'Tesoura':
    print(f'O programa venceu. Ele escolheu {escolha_programa} e você escolheu {escolha_usuário}.')

elif escolha_programa == 'Papel' and escolha_usuário == 'Pedra':
    print(f'O programa venceu. Ele escolheu {escolha_programa} e você escolheu {escolha_usuário}.')

else: print(f'Você ganhou!! O programa escolheu {escolha_programa} e você escolheu {escolha_usuário}. Parabéns!!')