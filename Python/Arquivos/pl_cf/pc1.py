import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando funcoes offline
from plotly.offline import download_plotlyjs, plot, iplot, init_notebook_mode

import cufflinks as cf

init_notebook_mode(connected=True) # Conectar com o notebook

cf.go_offline()

df = pd.DataFrame(np.random.rand(100, 4), columns='A B C D'.split())

df2 = pd.DataFrame({'Categoria':['A', 'B', 'C'], 'Valores':[32, 43, 50]})

# Metodos com pandas
#df.plot(kind='scatter', x = 'A', y = 'B')

# Metodos com plotly
#df.iplot(kind='scatter', x = 'A', y = 'B', mode='markers')

#df2.iplot(kind='bar', x = 'Categoria', y = 'Valores')

# ---- graficos 3D ---

df3 = pd.DataFrame({'x':[1, 2, 3, 4, 5], 'y':[10, 20, 30, 40, 50], 'z':[5, 4, 3, 2, 1]})

df3.iplot(kind='surface')

plt.show()