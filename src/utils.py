import csv

def formatar_preco(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {valor_formatado}"

def formatar_porcentagem(valor):
    return f"{valor:.2f}%"

def mostrar_menu():

    titulo = "CoinOrbit🪙"

    print("=" * 40)
    print(titulo.center(40))
    print("=" * 40)

    print("1 - Buscar Criptomoeda")
    print("2 - Top 10 Criptomoedas")
    print("3 - Exportar Top 10 para CSV")
    print("4 - Analisar Top 10")
    print("5 - Gráfico de Variação")
    print("6 - Sair")

    return input("Escolha uma opção: ")

def exportar_csv(dados):
    if not dados:
        print("Não foi possível exportar os dados.")
        return

    campos = ["nome", "simbolo", "preco", "variacao", "market_cap"]

    with open("data/top10.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(dados)

    print("CSV exportado com sucesso!")