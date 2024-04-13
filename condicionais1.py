#primeiro uso de condicionais

import string

nome = str(input('Digite o seu nome completo: '))
nomecompleto = nome.upper()
nomecompleto1 = ''.join(nomecompleto.split())

if nomecompleto1 == 'MICHAELJACKSONDASILVA':
    print('HEE HEE. Você é insano, Michael. AUUU')
else:
    print('Saia daqui, você não é o Michael.')
    