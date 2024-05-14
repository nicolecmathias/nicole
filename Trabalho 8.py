def bombom(dinheiro,preco):
    return float(dinheiro)/preco, dinheiro%preco
def maisbombom(dinheiro,preco):
    return preco - bombom(dinheiro,preco)[1]
def numeros_pares(numero):
    return list(range(2, numero + 1, 2))

# Exemplo de uso:
numero = 10
print(numeros_pares(numero))  # Saída: [2, 4, 6, 8, 10]