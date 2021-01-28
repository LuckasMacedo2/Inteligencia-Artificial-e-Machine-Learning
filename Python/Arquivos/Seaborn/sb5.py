# PairGrids
# Permite a constucao de graficos mais eficientes
# Basta passar a funcao e a regiao a ser mapeada

# Cria graficos de dispersao utilizando todas as variaveis
# numericas possiveis

import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

#g = sns.PairGrid(iris)
#g.map(plt.scatter) # plotando scatter em todos
#g.map_diag(plt.hist) # plotando histogramas na diagonal
#g.map_lower(sns.kdeplot) # Abaixo da diagonal principal
#g.map_upper(plt.scatter) # A cima da diagonal principal

# --- pairplot ---
# Metodo pairplot
# PairGrid plotado de forma padrao

#sns.pairplot(iris, hue='species')

# --- FacetGrid ----

tips = sns.load_dataset('tips')

# col e rows sao valores categoricos
g1 = sns.FacetGrid(tips, col = 'time', row='smoker')
g1.map(plt.hist, 'total_bill')

plt.show()