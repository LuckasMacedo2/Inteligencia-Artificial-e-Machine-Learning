import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)

y = x*x

#fig, ax = plt.subplots(figsize = (8, 5))

# Outra maneira de modificar a cor do grafico
# parametro color = 'nome_cor', ou em hexadecimal

# Parametro lw ou linewidth = tamanho_linha
# permite alterar a grossura da linha

# Parametro alpha =  transparencia_linha
# permite alterar a transparencia da linha

# Parametro linestyle = estilo_fonte
# permite alterar o estilo da linha

#ax.plot(x, x**2, color = 'green', linewidth = 10, alpha = 0.5)
#ax.plot(x, x**3, color = 'black', linestyle = '--')

# Definindo o limite em x e y
# Metodo ax.set_xlim([lista_com_intervalo_inicial_e_final])
# Metodo ax.set_ylim([lista_com_intervalo_inicial_e_final])

#ax.set_xlim([0,2])
#ax.set_ylim([0,10])

#plt.show()

# ---------------------------- Plotagens Especiais ----------

# --- Plotando os pontos ---
# Metodo plt.scatter(x,y)

#plt.scatter(x,y)

# --- Plotando histogramas ---
# Metodo: plt.hist(data)

#from random import  sample
#data = sample(range(1,1000), 100)
#plt.hist(data)

# --- Plotando boxplot ---
# Metodo:

data = [np.random.normal(0, std, 100) for std in range (1,4)]
plt.boxplot(data, vert=True,patch_artist=True)















plt.show()