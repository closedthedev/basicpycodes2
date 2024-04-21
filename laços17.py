#praticando for, com várias variáveis

qnt_alunos = int(input('Quantos alunos você quer analisar as notas? '))

maiornota_homem = 0
maiornota_mulher = 0
nomemaior_homem = 0
nomemaior_mulher = 0
idade_homem = 0
idade_mulher = 0

for i in range(1, qnt_alunos + 1):
    print(f'{i}ª aluno')
    sexo = str(input('Sexo. M/F: ')) .strip() .upper()
    nome = str(input('Nome: '))
    idade = int(input('Idade:' ))
    nota = float(input('Nota: '))

    if i == 1 and sexo == 'M':
        maiornota_homem = nota
        nomemaior_homem = nome
        idade_homem = idade

    if sexo == 'M' and nota > maiornota_homem:
        maiornota_homem = nota
        nomemaior_homem = nome
        idade_homem = idade

    if i == 1 and sexo == 'F':
        maiornota_mulher = nota
        nomemaior_mulher = nome
        idade_mulher = idade

    if sexo == 'F' and nota > maiornota_mulher:
        maiornota_mulher = nota
        nomemaior_mulher = nome
        idade_mulher = idade

    

print(f'Você escolheu analisar {qnt_alunos} alunos. O homem com a maior nota se chama {nomemaior_homem}, ele tem {idade_homem} anos e sua nota foi {maiornota_homem:.1f}. A mulher com a maior nota se chama {nomemaior_mulher}, ela tem {idade_mulher} anos e sua nota foi {maiornota_mulher:.1f}')