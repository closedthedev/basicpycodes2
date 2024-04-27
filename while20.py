#praticando while, agora analisando dados de várias pessoas

homem = mulher = 0
mulhernova = 0
adulto = 0

while True:
    sexo = str(input('Sexo M/F: ')) .strip() .upper()
    idade = int(input('Idade: '))
    if sexo == 'M':
        homem += 1 
    if sexo == 'F':
        mulher += 1
    if sexo == 'F' and idade < 20:
        mulhernova += 1
    if idade >= 18:
        adulto += 1 

    continuar = str(input('Quer continuar? S/N ')) .strip() .upper()
    if continuar == 'N':
        break

print(f'Você digitou os dados de {homem} homens, {mulher} mulheres e {adulto} são adultos. Nos dados passados, {mulhernova} mulheres têm menos de 20 anos de idade.')

    