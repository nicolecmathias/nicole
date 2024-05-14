def gravar_nome_arquivo():
    nome_arquivo = "nomes.txt"
    nome = input("Nicole: ")
    
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(nome)

    print("Nome gravado com sucesso no arquivo", nome_arquivo)

# Chamada da função
gravar_nome_arquivo()
def imprimir_conteudo_arquivo():
    nome_arquivo = input("PDF: ")
    
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()

    print("Conteúdo do arquivo", nome_arquivo + ":")
    print(conteudo)

# Chamada da função
imprimir_conteudo_arquivo()
def copiar_arquivo(origem, destino):
    with open(origem, "r") as arquivo_origem:
        conteudo = arquivo_origem.read()
    
    with open(destino, "w") as arquivo_destino:
        arquivo_destino.write(conteudo)

# Chamada da função
nome_arquivo_origem = "arquivo_origem.txt"
nome_arquivo_destino = "arquivo_destino.txt"
copiar_arquivo(nome_arquivo_origem, nome_arquivo_destino)
def encontrar_nome_por_numero(numero_procurado):
    nome_arquivo = "arquivo_exemplo.txt"
    
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(",")
            if partes[0] == numero_procurado:
                print("O nome correspondente ao número", numero_procurado, "é:", partes[1])
                return
    
    print("Número não encontrado no arquivo.")

# Chamada da função
numero_procurado = input("Por favor, digite um número: ")
encontrar_nome_por_numero(numero_procurado)
