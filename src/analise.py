import pandas as pd
from src.utils import formatar_porcentagem, formatar_preco
import matplotlib.pyplot as plt
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
    "CoinOrbit.App"
)

plt.rcParams["toolbar"] = "None"

def analisar_top10():
    dados = pd.read_csv("data/top10.csv")

    maior_preco = dados.loc[dados["preco"].idxmax()]

    print("\nMoeda com maior preço:")
    print(
        f"{maior_preco['nome']} "
        f"({maior_preco['simbolo'].upper()}) "
        f"{formatar_preco(maior_preco['preco'])}"
    )

    maior_valorizacao = dados.loc[dados["variacao"].idxmax()]

    print("\nMoeda com maior valorização em 24h:")
    print(
        f"{maior_valorizacao['nome']} "
        f"({maior_valorizacao['simbolo'].upper()}): "
        f"{formatar_porcentagem(maior_valorizacao['variacao'])}"
    )

    maior_queda = dados.loc[dados["variacao"].idxmin()]

    print("\nMoeda com maior queda em 24h:")
    print(
        f"{maior_queda['nome']} "
        f"({maior_queda['simbolo'].upper()}): "
        f"{formatar_porcentagem(maior_queda['variacao'])}"
    )

def grafico_variacao(dados):
    dataframe = pd.DataFrame(dados)

    cor_fundo = "#121212"
    cor_grafico = "#1e1e1e"
    cor_laranja = "#f7931a"
    cor_texto = "#e5e7eb"
    cor_grade = "#4b5563"

    cores = ["#22c55e" if valor >= 0 else "#ef4444"
             for valor in dataframe["variacao"]]

    ax = dataframe.plot(
        x="simbolo",
        y="variacao",
        kind="bar",
        legend=False,
        figsize=(10, 7),
        color=cores
    )

    ax.figure.set_facecolor(cor_fundo)
    ax.set_facecolor(cor_grafico)
    ax.figure.canvas.manager.set_window_title("CoinOrbit")

    gerenciador = plt.get_current_fig_manager()

    gerenciador.window.iconbitmap(
    "assets/coinorbit-icon.ico"
)

    ax.tick_params(
        axis="both",
        colors=cor_texto,
        labelsize=10
    )

    plt.title(
        "CoinOrbit | Variação das Top 10 Criptomoedas em 24h",
        fontsize=15,
        fontweight="bold",
        pad=15,
        color=cor_laranja
    )

    plt.xlabel(
        "Criptomoedas",
        color=cor_laranja,
        fontweight="bold"
    )

    plt.ylabel(
        "Variação (%)",
        color=cor_laranja,
        fontweight="bold"
    )

    plt.xticks(rotation=45)

    ax.grid(
        axis="y",
        color=cor_grade,
        linestyle="--",
        alpha=0.3
    )

    ax.set_axisbelow(True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(cor_grade)
    ax.spines["bottom"].set_color(cor_grade)

    ax.axhline(
        y=0,
        color=cor_laranja,
        linewidth=1.2
    )

    ax.margins(y=0.12)

    for barra in ax.patches:
        valor = barra.get_height()

        ax.text(
            barra.get_x() + barra.get_width() /2,
            valor,
            f"{valor:.2f}%",
            ha="center",
            va="bottom" if valor >= 0 else "top",
            color=cor_texto,
            fontweight="bold"
        )

    plt.tight_layout()
    plt.show()