#praticando while, dessa vez com um simulador de caixa eletrônico


valor = int(input('Qual valor você deseja sacar: '))


total = valor
cédula = 50 #representa a denominação da cédula atual
totalcédula = 0 #representa o número total de cédulas que serão entregues


while True:
    
    if total >= cédula: #verifica se ainda é possível sacar a cédula atual
       
        total -= cédula  #reduz o valor total a ser sacado pelo valor da cédula atual
        
        totalcédula += 1 #adiciona valor no  contador de cédulas
    else: 
        # Quando não for mais possível sacar a cédula atual
        # Verifica se alguma cédula foi sacada

        # Atualiza a denominação da cédula para a próxima
        if cédula == 50:
            cédula = 20

        elif cédula == 20:
            cédula = 10

        elif cédula == 10:
            cédula = 1

        if totalcédula > 0: #para não aparecer "total de 0 cédulas de tal valor"
           
            print(f'Total de {totalcédula} cédulas de R${cédula}') 

       
        if total == 0:  #verifica se todo o valor foi sacado
            break


print(f'Você sacou R${valor}. Sendo dividido em um total de {totalcédula} cédulas.')