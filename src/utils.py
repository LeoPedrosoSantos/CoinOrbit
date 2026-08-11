def formatar_preco(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {valor_formatado}"

def formatar_porcentagem(valor):
    return f"{valor:.2f}%"

def mostrar_menu():
    titulo = "Crypto Tracker🪙"

    print("=" * 40)
    print(titulo.center(40))
    print("=" * 40)

    print("1 - Buscar Criptomoeda")
    print("2 - Top 10 Criptomoedas")
    print("3 - Sair")

    return input("Escolha uma opção: ")