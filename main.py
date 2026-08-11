from src.api import buscar_moeda, buscar_top10
from src.utils import formatar_preco, formatar_porcentagem, mostrar_menu

def obter_moeda():
    nome_moeda = input("Digite o nome da criptomoeda: ").lower()

    return buscar_moeda(nome_moeda)

def mostrar_dados(dados):
    if dados: 
        print(f"""
Nome: {dados['nome']}
Símbolo: {dados['simbolo'].upper()}
Preço: {formatar_preco(dados['preco'])}
Variação (24h): {formatar_porcentagem(dados['variacao'])}
Market Cap: {formatar_preco(dados['market_cap'])}              
    """)
    else: 
        print("Criptomoeda não encontrada.")

def mostrar_top10(dados):
    if dados:
        print("\nTop 10 Criptomoedas por Market Cap:")
        print("=" * 40)
        for posicao, moeda in enumerate(dados, start=1):
            print(f"""
{posicao}. Nome: {moeda['nome']}
   Símbolo: {moeda['simbolo'].upper()}
   Preço: {formatar_preco(moeda['preco'])}
   Variação (24h): {formatar_porcentagem(moeda['variacao'])}
Market Cap: {formatar_preco(moeda['market_cap'])}
""")
    else:
        print("Não foi possível obter o Top 10 de criptomoedas.")

while True:
    opcao = mostrar_menu().lower()

    match opcao:
        case "1":
            dados = obter_moeda()  
            mostrar_dados(dados)

        case "2":
            dados = buscar_top10()
            mostrar_top10(dados)
        case "3":
            print("\nObrigado por usar o Crypto Tracker!")
            break

        case _:
            print("Opção inválida. Tente novamente.")