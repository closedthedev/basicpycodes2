#praticando while, com uma forca bem simples

palavra_escolhida = ''
tentativas = 0

print('TENTE ACERTAR A PALAVRA ESCOLHIDA PELO PROGRAMA')

while palavra_escolhida != 'ARROZ':
   

   palavra_escolhida = str(input('Tente acertar a palavra: ')) .upper() .strip()
   tentativas += 1
   if palavra_escolhida != 'ARROZ':
    print(f'Você errou {tentativas} vezes. Tente de novo!')
    
if palavra_escolhida == 'ARROZ':
     print(f'Na sua {tentativas}ª tentativa você acertou. Parabéns!!')
