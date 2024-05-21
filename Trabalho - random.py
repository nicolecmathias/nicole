import random

def lancar_dado():
    resultado = random.randint(1, 6)  # Gera um número aleatório entre 1 e 6
    return resultado

# Exemplo de uso da função
resultado_do_lancamento = lancar_dado()
print("O resultado do lançamento do dado é:", resultado_do_lancamento)
