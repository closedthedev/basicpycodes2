#fazendo uma tabuada de 0 a 100, multiplicando com o valor solicitado pelo usuário

número = int(input('Digite o número que queira ver a tabuada: '))

print(f'A tabuada do número {número} até o número 20 fica:')
for tabuada in range(0, 101): #fazendo com que comece multiplicando por 0 e finalize multiplicando por 100
    resultado = número * tabuada #criando a variável resultado, que é basicamente o número solicitado sendo multiplicado por tabuada, que nesse caso é o nosso laço.
    print(f'{número} x {tabuada} = {resultado}')