#utilizando o elif


nome = str(input('Digite o seu nome: ')).upper() .strip()

if nome == 'LUIZ OTAVIO' or nome == 'RAFAELA':
    print(f'Que nome lindo. Tenha um bom dia, {nome.title()}!')

elif nome == 'JOSÉ' or nome == 'MARIA' or nome == 'JOÃO' or  nome == 'ANA' or nome == 'ANTÔNIO' or nome == 'JULIANA':
    print(f'Seu nome está entre os nomes mais populares do Brasil. Tenha um bom dia, {nome.title()}!')

else: print(f'Seu nome é normal. Tenha um bom dia, {nome.title()}!')