#praticando while, agora com uma p.a que ja foi feita com for e mais avançada que a anterior, colocando mais números


n_usuário = int(input('Digite qual termo da p.a quer saber: '))
 #fórmula para saber o 

print('Digite o primeiro número, a razão e o termo da p.a que quer saber. Digite 0 para finalizar o programa.')
while n_usuário != 0:
    
    n1 = int(input('Digite o valor do primeiro termo da P.A: '))
    r = int(input('Digite a razão da P.A: '))
    numero_elementos = n1 + (n_usuário - 1) * r
    print(f'O primeiro termo da P.A é {n1}, a razão é {r} e o {n_usuário}ª termo da p.a é: {numero_elementos}.')
    mais_números = int(input('Qual outro termo você quer ver? Caso não queira ver mais nenhum, digite 0: '))
    numero_elementos2 = n1 + (mais_números - 1) * r
    print(f'O {mais_números}ª é {numero_elementos2}')
