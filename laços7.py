#fazendo uma progressão aritmética com for, descobrindo os números de uma p.a aleatória, baseada nas informações passadas pelo usuário

n1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
n_usuário = int(input('Digite até qual número quer: '))
numero_elementos = n1 + (n_usuário - 1) * r #fórmula para saber o 

for c in range(n1, n_usuário + r , r):
    print(c , end=' ')
