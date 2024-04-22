#primeiro uso de while, validando login e senha

login = ''
senha = ''

while login != 'luiz1234' and senha != 'Luiz312#':
    login = str(input('Digite o login: '))
    senha = str(input('Digite a senha: '))

print('Seja bem-vindo!')