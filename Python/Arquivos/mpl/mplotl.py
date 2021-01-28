# matplotlib: biblioteca de visualizacao de dados

import matplotlib.pyplot as plt # importando a biblioteca, plt forma padrao
import numpy as np

# linspace() cria um espaco vetorial
x = np.linspace(0, 5, 11)

y = x*x

# --------------- plot de um grafico -----------------------
# Funcional
# color = 'cor'. Permite mudar a cor da reta
#plt.plot(x, y, color = 'r')

# Nomeando os eixos
#plt.xlabel('Eixo x')
#plt.ylabel('Eixo y')

# Colocando um titulo no grafico
#plt.title('Titulo')

#plt.show() # Mostra o grafico

# --------------- plot de dois graficos ---------------------
# Metodo plt.subplot(nrows = qtd_de_linhas_grafico, ncols = qtd_de_colunas_grafico, elementos)
# * nrows: especifica a quantidade de linhas que o grafico tera
# * ncols: especifica a quantidade de colunas que o grafico tera
# * o terceiro parametro indica com qual parte da figura se esta trabalhando

# plotando varios graficos

# Plotando na primeira parte da imagem
#plt.subplot(1, 2, 1)
#plt.plot(x, y, 'r--')

# Plotando na segunda parte da imagem
#plt.subplot(1, 2, 2)
#plt.plot(y, x, 'g*-')

#plt.show()

# -------------------- trabalhando com objetos do plt -------
fig = plt.figure()  # Cria uma figura

# metodo fig.add_axes()
# parametro lista, itens da lista
# 1* percentual de posicionamento relativo a esquerda da figura
# 2*  |||                                  a parte inferior da figura
# 3* largura
# 4* altura
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # Adiciona um eixo
axes.plot(x, y)
axes.set_xlabel('Eixo x')
axes.set_title('Titulo')

axes2 = fig.add_axes([0.2, 0.5, 0.3, 0.3]) # Adiciona um eixo
axes2.plot(y, x)
axes2.set_xlabel('Eixo x')
axes2.set_title('Titulo')

plt.show()
















