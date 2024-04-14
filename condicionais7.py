#aumento de salário

salário = float(input('Digite o seu salário: R$'))
saláriosuperior = ((10 * salário) // 100) + salário
saláriomenorrigual = ((15 * salário) // 100) + salário

if salário > 1250:
    print(f'Seu salário vai aumentar em 10%, passando de R${salário:.2f} para R${saláriosuperior:.2f} ')

else: print(f'Seu salário vai aumentar em 15%, passando de R${salário:.2f} para R${saláriomenorrigual:.2f} ')