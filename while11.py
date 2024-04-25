#praticando while, agora fazendo uma sequência de fibonacci

t1 = 0
t2 = 1
n = int(input('Qual termo da Fibonacci você quer saber? '))

cont = 3
print(f'{t1} → {t2}' , end = '')
while cont <= n:
    t3 = t1 + t2
    cont += 1
    print(f'→ {t3}', end = '')
    t1 = t2
    t2 = t3
    