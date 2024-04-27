#praticando while, criando uma tabuada. quando o número solicitado for negativo, o programa será encerrado
n = int(input('Digite um número para fazer a tabuada: '))
max = int(input('Até qual número deseja fazer a tabuada: '))
cont = 1

while cont != max + 1:
   
    
    print(f'{n} x {cont} = {n*cont}')
    cont +=1
   
    if n < 0:
        print('Não aceitamos valores negativos. Programa encerrado!')
        break
   
   

    