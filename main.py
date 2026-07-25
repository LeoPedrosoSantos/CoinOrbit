from src.api import buscar_moeda
from src.utils import formatar_preco, formatar_porcentagem

print("=" * 40)
print("      Crypto Tracker")
print("=" * 40)

moeda = input("Digite o nome da moeda: ").lower()

dados = buscar_moeda(moeda)

print(f"""
Nome: {dados["nome"]}
Símbolo: {dados["simbolo"].upper()}
Preço: {formatar_preco(dados["preco"])}
Variação 24h: {formatar_porcentagem(dados["variacao"])}
Market Cap: {formatar_preco(dados["market_cap"])}
""")