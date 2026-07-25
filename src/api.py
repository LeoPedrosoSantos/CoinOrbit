import requests
from src.config import BASE_URL


def buscar_moeda(nome_moeda):
    url = f"{BASE_URL}/coins/{nome_moeda}"

    resposta = requests.get(url)

    dados = resposta.json()

    return {
        "nome": dados["name"],
        "simbolo": dados["symbol"],
        "preco": dados["market_data"]["current_price"]["brl"],
        "variacao": dados["market_data"]["price_change_percentage_24h"],
        "market_cap": dados["market_data"]["market_cap"]["brl"],
}