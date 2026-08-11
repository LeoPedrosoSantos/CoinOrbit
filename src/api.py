import requests
from src.config import BASE_URL


def buscar_moeda(nome_moeda):
    url = f"{BASE_URL}/coins/{nome_moeda.lower()}"

    resposta = requests.get(url)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    return {
        "nome": dados["name"],
        "simbolo": dados["symbol"],
        "preco": dados["market_data"]["current_price"]["brl"],
        "variacao": dados["market_data"]["price_change_percentage_24h"],
        "market_cap": dados["market_data"]["market_cap"]["brl"],
}

def buscar_top10():
    url = f"{BASE_URL}/coins/markets"

    parametros = {
        "vs_currency": "brl",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    resposta = requests.get(url, params=parametros)

    if resposta.status_code != 200:
        return None

    dados = resposta.json()

    top10 = []

    for moeda in dados:
        top10.append({
            "nome": moeda["name"],
            "simbolo": moeda["symbol"],
            "preco": moeda["current_price"],
            "variacao": moeda["price_change_percentage_24h"],
            "market_cap": moeda["market_cap"]
        })

    return top10