import matplotlib.pyplot as plt # importando a biblioteca, plt forma padrao
import numpy as np

# linspace() cria um espaco vetorial
x = np.linspace(0, 5, 11)

y = x*x
#fig, ax = plt.subplots() # subplots cria a figura e o eixo unico
# ax e uma lista de eixos

#ax.plot(x, x**3, 'b--')
#ax.plot(x, x**4, 'g--')

#ax.set_xlabel('x')
#ax.set_ylabel('y')

#ax.set_title('Titulo')


# ------------------ Melhorando a visualizacao -----------
#fig1, ax1 = plt.subplots(nrows=5, ncols=5)

# Melhora a visualizacao
#plt.tight_layout()

#plt.show()


# Metodo figsize(): permite definir o tamanho da figura
# depi: permite definir a resolucao da figura
#fig2 = plt.figure(figsize = (8,4), dpi=100)

fig, axes = plt.subplots(figsize=(12,3))

# Adicionando um legenda
# parametro: label = 'nome legenda'
# metodo axes.legend()
axes.plot(x, y, 'r--', label='x^2')
axes.plot(y, x, 'g--', label='x^1/2')

# parametro loc = numero: especifica onde a legenda ficara posicionada
axes.legend(loc=0)

axes.set_title('Titulo')

plt.show()
axes.legend()
# Salvando a figura
#fig.savefig('imagem.jpg')



