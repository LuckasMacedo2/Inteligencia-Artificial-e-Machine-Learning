#  Plots categoricos
# Dados categoricos contem textos e sao relativamente discretos
# possuem pouca possibilidade de  valores

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# -------- barplot -----

# Metodo barplot(x, y, data)
# Parametros
# eixo x (x)
# eixo y (y)
# dados (data)

# estimator = funcao, permite definir uma funcao a ser aplicada nos dados

#sns.barplot(x = 'sex', y = 'total_bill', data=tips)

#sns.barplot(x = 'sex', y = 'total_bill', data=tips, estimator = np.std)

#plt.show()

# -------- countplot -----
# O estimador e um contador
# Realiza a contagem dos elementos no eixo

#sns.countplot(x = 'sex', data = tips)

#plt.show()

# -------- boxplot -----
# Plota percentis dos dados. 25%, 50%, 75%, 100%, e outliers (pontos que nao pertencem a distribuicao)

#sns.boxplot(x = 'day', y = 'total_bill', data = tips)

# Parametro hue = 'categoria'
# Permite 'quebrar' os plots em diferentes categorias, ex: sex

#sns.boxplot(x = 'day', y = 'total_bill', data = tips, hue = 'sex')

# Colocando o boxplot na horizontal
# Parametro orient = 'h' ou 'v'
# Sem especificar os dados pega todos os dados numericos da base de dados

#sns.boxplot(data = tips, orient='h')

#plt.show()

# ----------- violinplot ----------------------------------------------
# Cria baseado no KDE, cria um grafico simetrico.

#sns.violinplot(x = 'day', y = 'tip', data = tips)

# Tambem possue o parametro hue

#sns.violinplot(x = 'day', y = 'tip', data = tips, hue = 'sex')

# Retirando a simetria do grafico
# Parametro split = True ou False

#sns.violinplot(x = 'day', y = 'tip', data = tips, hue = 'sex', split = True)

#plt.show()

# ----------- stripplot -------------------------------------------
# Grafico com pontinhos

#sns.stripplot(x = 'day', y = 'total_bill', data = tips)

# Parametro
# jitter = True ou False
# Coloca os pontos mais dispersos

#sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True)

# Tambem o parametro hue, split

#sns.stripplot(x = 'day', y = 'total_bill', data = tips, jitter = True, hue = 'sex', split=True)

#plt.show()

# --- swarmplot ---
# Lida mal com grandes quantidades de dados, e os dados podem se sobrepor

#sns.swarmplot(x = 'day', y = 'total_bill', data = tips)

#plt.show()

# --- swarm e violin ---
# Interessante
#sns.swarmplot(x = 'day', y = 'total_bill', data = tips, color = 'black')
#sns.violinplot(x = 'day', y = 'total_bill', data = tips)

#plt.show()

# ----------- factorplot -------------------------------------------
# Cria qualquer plot anterior
# Parametro kind = 'tipo_plot', especifica a forma que o mesmo tomara
# ex: bar
sns.factorplot(x = 'day', y = 'total_bill', data = tips, kind = 'violin')

plt.show()