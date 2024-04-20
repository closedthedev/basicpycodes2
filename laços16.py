#praticando for, dessa vez com várias variáveis

qntd_pessoas = int(input('Digite a quantidade de pessoas que queira formar um grupo: '))
somaidade = 0
maior_homem = 0
nomevelho = ''
mulhermenosde20 = 0


for g in range(1, qntd_pessoas + 1, 1):
    print(f'{g}ª pessoa')
    nome = str(input('Digite o primeiro nome da pessoa: '))
    idade = int(input('Digite a idade dessa pessoa: '))
    sexo = str(input('Digite o sexo dessa pessoa. M/F: ')).upper() .strip()
    somaidade += idade
    
    if g == 1 and sexo == 'M':
        maior_homem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maior_homem:
        maior_homem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenosde20 += 1 
        

    média_idade = somaidade / qntd_pessoas

print(f'Você escolheu passar as informações de {qntd_pessoas} integrantes do grupo. A média de idade deles é de {média_idade}. O homem mais velho se chama {nomevelho} e possui {maior_homem} anos de idade. O grupo tem {mulhermenosde20} mulheres com menos de 20 anos.')
