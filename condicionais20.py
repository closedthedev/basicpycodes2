#validador de senha bem básico, pois ainda não utilizo funções

senha = str(input('Digite a senha desejada:'))
comp_senha = len(senha)

if comp_senha < 8:
    print(f'O mínimo para criarmos uma senha são 8 caracteres, sua senha tem apenas {comp_senha}. Dito isso, sua senha não foi aceita.')

elif comp_senha <= 15:
    print('Sua senha foi aceita, iremos concluir o cadastro!')

else: print(f'O nosso único requisito é ter no mínimo 8 caracteres, mas FUCKING {comp_senha} caracteres é muita coisa. Você está digitando uma senha ou a biblia 2? ')

