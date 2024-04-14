#um programa simulando parcela de um emprestimo se ele for aceito. a parcela nao pode exceder 30% do salário


nome = str(input('Digite o seu nome: '))
salário = float(input('Digite o seu salário: R$'))
valor_empréstimo = float(input('Digite o valor do empréstimo: '))
qnt_parcelas = int(input('Digite em quantas parcelas você quer realizar o pagamento do empréstimo: '))
valor_prestação = valor_empréstimo / qnt_parcelas
salário_requisito = 0.3 * salário

if salário_requisito < valor_prestação:
    print(f'Olá, {nome}! Infelizmente o seu empréstimo foi negado. A prestação não pode ultrapassar 30% do salário. 30% do seu salário correspondem a R${salário_requisito:.2f} e a prestação é R${valor_prestação:.2f}. ')

else: print(f'Olá, {nome}! Seu empréstimo foi aprovado. Consulte o seu gerente para dar continuidade. Tenha um bom dia! ')