#utilizando um randomizador para dizer qual a altura do usuário com algums comentarios 

import random

nome = str(input('Digite seu nome e o programa vai dizer a sua altura: '))
altura_randomizada = random.uniform(1.60 , 2.10)

if altura_randomizada >= 1.90:
    print(f'LOOK AT HIM, {nome}. Fuckings {altura_randomizada:.2f}m. Quem você pensa que é, rapaz?! Chris Bumstead?! O CBUM?!')
elif altura_randomizada >= 1.70:
    print(f'{nome}, sua altura é normal, nada demais. {altura_randomizada:.2f}m é bem padrão e sem graça.')
else:
    print(f'{altura_randomizada:.2f}m? Parabéns, {nome}, você acaba de receber o título de anão bombado!')
