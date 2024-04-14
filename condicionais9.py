#conferindo se os segmentos recebidos podem ser um triângulo
a = float(input('Digite o valor de um segmento: '))
b = float(input('Digite o valor de um segmento: '))
c = float(input('Digite o valor de um segmento: '))

if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima podem formar um triângulo!')

else: print('Os segmentos acima não podem formar um triângulo.')

