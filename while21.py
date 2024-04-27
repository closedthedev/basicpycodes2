#praticando while, perguntando pro usuário o nome e valor de produtos que ele acabou de comprar, fazendo uma análise depois e dizendo qual é o produto mais barato
produtos = total = maisdemil = 0
maisbarato = float('inf')
nome_mais_barato = ''

while True:
    produto = input('Nome do produto: ')
    valor = float(input('Valor: '))
    
    produtos += 1
    total += valor
    
    if valor > 1000:
        maisdemil += 1 

    if valor < maisbarato:
        maisbarato = valor
        nome_mais_barato = produto

    continuar = input('Tem mais algum produto? S/N: ').strip().upper()

    if continuar == 'N':
        break

print(f'Você comprou {produtos} produtos, totalizando no valor de R${total:.2f}. Entre esses produtos, {maisdemil} passam de R$1000.00 reais, e o produto mais barato é o {nome_mais_barato} com o valor de R${maisbarato:.2f}.')
    
