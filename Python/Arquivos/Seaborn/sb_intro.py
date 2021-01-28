# Seaborn biblioteca de visualizacao estatistica de dados
# Integra bem com o pandas
# Referencia: https://seaborn.pydata.org/

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips') # dataset, base de dados
# Acima base de dados de gorjeta

# ------------ displots --------------------------------------
# displots(), faz um histograma dos dados e plota uma curva
# kde, que e a estimativa de densidade da funcao.

#sns.distplot(tips['total_bill'], kde = False)

#plt.show() # Permite visualizar o grafico

# ------------ jointplots --------------------------------------
# jointplots(), cria uma curva de duas variaveis ao mesmo tempo
# Busca fazer graficos de distribuicao conjunta
# Parametros 3 obrigatorios
# 1*) O valor do eixo x (x)
# 2*) O valor do eixo y (y)
# 3*) O local em que se esta retirando os dados (data)

#sns.jointplot(x = 'total_bill', y = 'tip', data = tips, kind='hex' )
# kind = 'hex', faz um mapa de calor com os dados, quanto maior o conjunto de
# dados mais forte e a cor

#plt.show()

# ------------ pairplots --------------------------------------
# Parametro o dataset
# Pega todas as variaveis numericas e realiza jointplots de cada uma delas
# Faz uma matriz de graficos

# Parametro hue = 'parametro'
# Da cor para dados categoricos, permite adicionar mais informacoes

# Parametro palette = 'paleta_cor'
# Permite mudar a paleta de cores

#sns.pairplot(tips, hue = 'sex')

#plt.show()

# ------------ rugplot --------------------------------------
# Menos util, quando aplicado sozinho
# Adiciona tracos em locais que possuem dados
# Util para criar um kde

# KDE forma nao parametrica de estimar funcos de distribuicao de probabilidade
# de uma variavel aleatoria.
# Ou seja, nao envolve parametros, dados que nao possuem certeza sobre sua distribuicao.

#sns.rugplot(tips['total_bill'])

#plt.show()

# ------------ kdeplot --------------------------------------
sns.kdeplot(tips['total_bill'])

plt.show()
