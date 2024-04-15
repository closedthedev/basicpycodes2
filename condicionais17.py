#de acordo com a idade do usuário ele terá uma classificação diferente


from datetime import date

data_atual = date.today().year
nascimento = int(input('Em qual ano você nasceu? '))
idade = abs(data_atual - nascimento)

if idade <= 9:
    print('Você está na categoria mirim.')

elif idade <= 14:
    print('Você está na categoria infantil.')

elif idade <= 19:
    print('Você está na categoria júnior.')

elif idade > 23:
    print('Você está na categoria sênior.')

else: print('Você está na categoria master.')