def somar(memoria):
    numero = float(input("Digite um número: "))
    memoria += numero
    print("Novo estado da memória:", memoria)
    return memoria

def subtrair(memoria):
    numero = float(input("Digite um número: "))
    memoria -= numero
    print("Novo estado da memória:", memoria)
    return memoria

def multiplicar(memoria):
    numero = float(input("Digite um número: "))
    memoria *= numero
    print("Novo estado da memória:", memoria)
    return memoria

def dividir(memoria):
    numero = float(input("Digite um número: "))
    if numero != 0:
        memoria /= numero
        print("Novo estado da memória:", memoria)
    else:
        print("Não é possível dividir por zero.")
    return memoria

def limpar_memoria(memoria):
    memoria = 0
    print("Estado da memória limpo.")
    return memoria

memoria = 0

while True:
    print("Estado da memória:", memoria)
    print("Opções:")
    print("(1) Somar")
    print("(2) Subtrair")
    print("(3) Multiplicar")
    print("(4) Dividir")
    print("(5) Limpar memória")
    print("(6) Sair do programa")

    opcao = int(input("Qual opção você deseja? "))

    if opcao == 1:
        memoria = somar(memoria)
    elif opcao == 2:
        memoria = subtrair(memoria)
    elif opcao == 3:
        memoria = multiplicar(memoria)
    elif opcao == 4:
        memoria = dividir(memoria)
    elif opcao == 5:
        memoria = limpar_memoria(memoria)
    elif opcao == 6:
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")