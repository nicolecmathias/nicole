def imprimir_informacoes(nome, idade, cidade):
    print(f"Nome: {nome}", end=" - ")
    print(f"Idade: {idade}", end=" - ")
    print(f"Cidade: {cidade}!")

# Exemplo de uso da função
imprimir_informacoes("Nicole", 21, "Rio de Janeiro")
def calcular():
    # Solicita ao usuário que insira os dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    
    # Verifica a operação desejada e calcula o resultado correspondente
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:  # Evita divisão por zero
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return  # Encerra a função se houver divisão por zero
    else:
        print("Erro: Operação inválida!")
        return  # Encerra a função se a operação for inválida
    
    # Imprime o resultado da operação
    print(f"Resultado da operação {num1} {operacao} {num2} = {resultado}")

# Chama a função para realizar o cálculo
calcular()
def lista_de_compras():
    # Pedindo ao usuário para digitar os itens da lista de compras
    entrada = input("Leite,queijo,batata,pão: ")
    
    # Separando os itens da entrada pelo caractere vírgula e removendo espaços em branco extras
    itens = [item.strip() for item in entrada.split(',')]

    # Imprimindo os itens em linhas separadas usando um laço
    print("Itens da lista de compras:")
    for item in itens:
        print(item)

# Chamando a função para testar
lista_de_compras()

def celsius_para_fahrenheit():
    # Pedindo ao usuário para digitar a temperatura em graus Celsius
    celsius = float(input("27°: "))

    # Convertendo Celsius para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprimindo o resultado da conversão
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Chamando a função para testar
 


def celsius_para_fahrenheit():
    # Pedindo ao usuário para digitar a temperatura em graus Celsius
    celsius = float(input("27°: "))

    # Convertendo Celsius para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprimindo o resultado da conversão
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Chamando a função para testar
celsius_para_fahrenheit()
def celsius_para_fahrenheit():
    # Pedindo ao usuário para digitar a temperatura em graus Celsius
    celsius = float(input("20°: "))

    # Convertendo Celsius para Fahrenheit usando a fórmula de conversão
    fahrenheit = (celsius * 9/5) + 32

    # Imprimindo o resultado da conversão
    print("A temperatura em Fahrenheit é:", fahrenheit)

# Chamando a função para testar
celsius_para_fahrenheit()
def solicitar_nomes():
    nomes = []

    # Loop infinito para solicitar nomes até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome ou 'sair' para encerrar: ")
        if nome.lower() == 'sair':
            break  # Sai do loop se 'sair' for digitado
        nomes.append(nome)

    # Imprime todos os nomes digitados
    print("Nomes digitados:")
    for nome in nomes:
        print(nome)

# Chamando a função para testar
solicitar_nomes()
