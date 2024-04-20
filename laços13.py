#aprendendo mais sobre o laço for, agora invertendo uma string e vendo se ela ao contrário é a mesma coisa que o norma, sendo  um palíndromo.

frase = str(input('Digite uma frase: ')).lower() .replace(' ' , '')
frase_invertida = ''

for char in reversed(frase):
    frase_invertida += char

if frase == frase_invertida:
    print(f'A frase solicitada é: {frase}. Ela ao contrário é: {frase_invertida}. Ela é um palíndromo')

else: print(f'A frase solicitada é: {frase}. Ela ao contrário é: {frase_invertida}. Ela não é um palíndromo')