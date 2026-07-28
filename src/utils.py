def formatar_preco(valor):
    return f"R$ {valor:,.2f}" 

def formatar_porcentagem(valor):
    return f"{valor:.2f}%"

def mostrar_menu():
    titulo = "Crypto Tracker🪙"

    print("=" * 40)
    print(titulo.center(40))
    print("=" * 40)

    print("1 - Buscar Criptomoeda")
    print("2 - Sair")

    return input("Escolha uma opção: ")