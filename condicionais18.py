#descobrindo se o triângulo é equilátero, isósceles, escaleno ou se simplesmente não é um triângulo

a = float(input('Digite o primeiro segmento : '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a == b == c:
    tipo = 'equilátero'
elif a == b and a != c or a == c and a != b or b == c and b != a:
    tipo = 'isósceles'
elif a != b != c:
    tipo = 'escaleno'
if a < b + c and b < a + c and c < a + b:
    print(f'Os segmentos acima podem formar um triângulo {tipo}')
else:
    print('Os segmentos acima não podem formar um triângulo')