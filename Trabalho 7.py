def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

# Exemplo de uso:
numeros = [1, 2, 3, 4]
soma, media = calcular_soma_e_media(numeros)
print("Soma:", soma)
print("Média:", media)
def substituir_palavra(lista, palavra_antiga, palavra_nova):
    nova_lista = [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]
    return nova_lista

# Exemplo de uso:
lista_palavras = ["árvore", "computador", "casa"]
palavra_antiga = "computador"
palavra_nova = "teclado"
nova_lista = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
print(nova_lista)
def imprimir_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print("*" * i)

# Exemplo de uso:
n = 5
imprimir_triangulo(n)


