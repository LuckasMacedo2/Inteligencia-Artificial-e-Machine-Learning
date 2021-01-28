# -------------- Exercicios ----------------------
import seaborn as sns
import matplotlib.pyplot as plt


sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

#print(titanic.head())

# --- 1 ---
# joinplot
#sns.jointplot(x = 'fare', y = 'age', data=titanic)

# --- 2 ---
# grafico de distribuicao
#sns.distplot(titanic['fare'], kde=False, color='red')

# --- 3 ---
# boxplot
# dados categoricos
#sns.boxplot(x = 'class', y = 'age', data=titanic, palette='rainbow')

# --- 4 ---
# swarplot
#sns.swarmplot(x='class', y = 'age', data=titanic, palette='rainbow')

# --- 5 ---
# countplot
#sns.countplot(x = 'sex', data=titanic)

# --- 6 ---
# plot matricial com correlacoes entre as variaveis numericas

# Correlacao entre todas as variaveis numericas
#corr = titanic.corr()
#sns.heatmap(corr, cmap='coolwarm')

# Colocando titulo no mapa
#plt.title('Titanic.corr()')

# --- 7 ---
# facetgrid
# Distribuicoes separadas em categorias

# Definindo a variavel como referencia ao facetgrid
g = sns.FacetGrid(data=titanic, col = 'sex')
g.map(plt.hist, 'age')

plt.show()



