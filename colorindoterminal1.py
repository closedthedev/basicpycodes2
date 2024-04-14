#primeira coloração no terminal

class cor:
    RESET = '\033[0m'
    VERMELHO = '\033[91m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIANO = '\033[96m'

# Exemplo de uso
print(cor.VERMELHO + "Texto em vermelho" + cor.RESET)
print(cor.VERDE + "Texto em verde" + cor.RESET)
print(cor.AZUL + "Texto em azul" + cor.RESET)