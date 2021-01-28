import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
plt.style.use('ggplot') # Definindo o estilo dos graficos
# Possiveis
# ggplot, bmh, dark_background


df1 = pd.read_csv('df1')
df2 = pd.read_csv('df2')
df3 = pd.read_csv('df3')

# Pandas possui metodos para visualizacao de dados

# --- histograma ----
#df1['A'].hist()
#df1['A'].plot.hist(bins = 50)


# --- Areas ---
# alpha altera a transparencia do grafico
#df2.plot.area(alpha=0.4)

# --- barras ---
#df2.plot.bar()
#df2.plot.bar(stacked=True) # Colocando tudo em uma barra so

# --- linha ---
#df1.plot.line(x = df1.index, y = 'B')

# --- scatter plot ---
# Grafico com pontos
# Parametro
# c: modifica a cor a partir de uma terceira variavel
# s: Altera o tamanho a partir de uma terceira variavel
#df1.plot.scatter(x = 'A', y = 'B', s = df1['C']*30)


# --- box plot ---
#df1.plot.box()

# ---- hexagonal ---
# Parametro
# gridsize: aumenta o tamanho dos hexagonos
#df = pd.DataFrame(np.random.rand(1000, 2), columns=['A', 'B'])
#df.plot.hexbin(x = 'A', y = 'B', gridsize=20)

# --- KDE ---
df2.plot.kde()

plt.show()