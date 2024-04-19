#descobrindo se o número é primo,  utilizando o for

numero = int(input("Digite um número inteiro positivo maior que 1: "))

# Verificar se o número é menor ou igual a 1
if numero <= 1:
    print(f"O  {numero} número não é primo.")
else:
    # Flag para verificar se o número é primo
    primo = True
    
    # Verificar se o número é divisível por algum número de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            # Se for divisível, não é primo
            primo = False
            break 
    
    # Imprimir o resultado
    if primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")