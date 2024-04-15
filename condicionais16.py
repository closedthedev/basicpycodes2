#calculando média escolar, agora utilizando o elif

nome = input('Digite o seu nome: ')

nota1 = float(input('Digite a sua nota do primeiro bimestre: '))
nota2 = float(input('Digite a sua nota do segundo bimestre: '))
nota3 = float(input('Digite a sua nota do terceiro bimestre: '))
nota4 = float(input('Digite a sua nota do quarto bimestre: '))

média = (nota1 + nota2 + nota3 + nota4) / 4

if média > 10:
    print(f'Pare de mentir, {nome}. É IMPOSSÍVEL a sua média ser maior do que 10.')

elif média >= 7:
    print(f'Parabéns {nome}, você foi aprovado! A sua média foi {média:.1f}.')

elif média >= 5:
    print(f'{nome}, você está em recuperação. Sua média ficou em {média:.1f}. Te vejo na próxima semana!')

else:
    print(f'{nome}, sinto-lhe informar... mas você foi reprovado. Sua média ficou em {média:.1f}. Te vejo no próximo ano! ')