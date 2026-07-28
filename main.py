from src.api import buscar_moeda
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
    
while True:
    opcao = mostrar_menu().lower()

    match opcao:
        case "1":
            dados = obter_moeda()  
            mostrar_dados(dados)

        case "2":
            print("\nObrigado por usar o Crypto Tracker!")
            break

        case _:
            print("Opção inválida. Tente novamente.")