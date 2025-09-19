import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo CSV com pandas
    df = pd.read_csv("boilerplate-sea-level-predictor-main\epa-sea-level.csv")

    # Cria o gráfico de dispersão (scatter plot)
    # Eixo X → coluna "Year"
    # Eixo Y → coluna "CSIRO Adjusted Sea Level"
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Cria a primeira linha de tendência geral dos dados (regressão linear) usando TODOS os dados
    # slope = inclinação da linha
    # intercept = ponto onde a linha cruza o eixo Y
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"]) # Os _ significam valores que não serão usados
    years_extended = range(1880, 2051)  # Intervalo dos anos de 1880 até 2050
    # years_extended será o X
    # intercept + slope * pd.Series(years_extended) será o Y (fórmula da reta)
    plt.plot(years_extended, intercept + slope * pd.Series(years_extended), "r") # "r" significa que a linha será vermelha

    # Cria a segunda linha de tendência geral usando SOMENTE dados de 2000 em diante
    # Isso mostra a tendência mais recente de crescimento do nível do mar
    df_recent = df[df["Year"] >= 2000] # Filtro para incluir apenas os anos a partir de 2000
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)  # Intervalo dos anos de 2000 até 2050
    plt.plot(years_recent, intercept_recent + slope_recent * pd.Series(years_recent), "g") # "g" significa que a linha será verde

    # Define os rótulos dos eixos e o título do gráfico
    # xlabel → nome do eixo X
    # ylabel → nome do eixo Y
    # title → título do gráfico
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Define os valores fixos que devem aparecer no eixo X
    # Isso é importante porque os testes esperam esses valores específicos
    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    # Salva o gráfico como arquivo PNG e retorna o objeto do gráfico para os testes
    plt.savefig("sea_level_plot.png")
    return plt.gca()
