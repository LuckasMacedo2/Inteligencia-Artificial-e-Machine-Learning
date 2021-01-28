# ---------------------- Plots Matriciais -------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Baixando os data sets
flights = sns.load_dataset('flights') # Base de dados de voos
tips = sns.load_dataset('tips')

# Dados na forma matricial
# Colunas e indices relacionados

# --------- heap map, mapa de calor -------------

#crr = tips.corr() # Calcula as correlacoes de todas os dados numericos do dataset

#sns.heatmap(crr, cmap='coolwarm', annot=True) # Mapa de calor
# Quanto mais escuro maior o calor
# cmap, define a paleta de cores
# annot = True, mostra o valor de cada quadrado

#plt.show()

# ------- pivot_table --------
# --- voos ----

# Metodo pivot_table
# Transforma em uma tabela com os dados especificados pelos parametros
# Parametros
# values = valores
# index = indice
# colums = coluna

pf = flights.pivot_table(values = 'passengers', index='month', columns='year')

#sns.heatmap(pf, linecolor='white', linewidths=1)
# linecolor = 'cor', especifica a cor das divisorias
# linewidthns = tam, especifica o tamanho das divisorias

#plt.show()

# -------- cluster -----------
# Busca agrupar os dados em sonjunto
# Metodo clustermap
# Busca reconhecer os padroes de dadoss

sns.clustermap(pf, standard_scale=1)

plt.show()







