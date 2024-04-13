#praticando condicionais, dessa vez dizendo se o aluno foi aprovado ou reprovado de ano, de acordo com suas notas.

nome= str(input('Digite seu nome completo: '))

nota1 = float(input('Digite sua nota do primeiro bimestre: '))
nota2 = float(input('Digite sua nota do segundo bimestre: '))
nota3 = float(input('Digite sua nota do terceiro bimestre: '))
nota4 = float(input('Digite sua nota do quarto bimestre: '))

notas = (nota1 + nota2 + nota3 + nota4) // 4 

if notas >= 6: 
    print(f'Olá, {nome}. Sua média foi {notas}. Você foi aprovado!')

else: print(f'Olá {nome}. Sua média foi {notas}. Você foi reprovado, te vejo no próximo ano!')