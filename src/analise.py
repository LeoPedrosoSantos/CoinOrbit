import pandas as pd

def analisar_top10():
    dados = pd.read_csv("data/top10.csv")

    print("\nResumo dos dados:")
    print(dados)

    print("\nPreço médio:")
    print(dados["preco"].mean())

    print("\nMaior Market Cap:")
    print(dados["market_cap"].max())