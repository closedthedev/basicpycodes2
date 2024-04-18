#colocando 6 números inteiros e selecionando todos os pares e somando eles, ignorando os ímpares

soma = 0 
cont = 0

for c in range(1, 7,): #fazendo com que pergunte um número ao usuário 6 vezes
    c = int(input('Digite um valor: '))
    cont += 1 #irá adicionar 1 a cada vez que for acionada, como o for irá rodar 6 vezes, o valor da contagem ficará em 6
    if c % 2 == 0: #fazendo com que todos os números múltiplos de 2 (pares) vão se somando, conforme sendo solicitados.
        soma += c
        

print(f'Você digitou {cont} valores, e a soma deles (apenas dos pares, os ímpares deixamos de lado) ficou em: {soma}')
        
        
