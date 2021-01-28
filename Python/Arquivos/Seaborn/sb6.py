# -------------------- Estilos e cores --------------

import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# --- Alterando o fundo ----
# Metodo set_style
# Possiveis
# darkgrid, white, ticks, whitegrid, dark
#sns.set_style('ticks')

# --- Alterando o tamanho da figura ---
# Biblioteca baseada no matplot lib
#plt.figure(figsize=(12,4))


#sns.countplot(x = 'sex', data = tips)

# --- Bordas ---
# Retirando as bordas
# Metodo despine()
# Por default retira a borda de cima e esquerda.
#sns.despine()

#plt.show()

# ---- setcontext ---
# Define o contexto e deixa um tamanho pre configurado
# Modifica conforme a definicao se sera utilizado em um poster, notbook, etc
# font_scale = tam_fonte, permite alterar o tamanho da fonte

#sns.set_context('poster')

#sns.lmplot(x = 'total_bill', y = 'tip', data = tips, size = 2, aspect=4)

#plt.show()

# --- Alterando a paleta de cores ---
# Referencia: https://matplotlib.org/examples/color/colormaps_reference.html
# Atributo palette
# Possiveis: coolwarm

#sns.lmplot(x = 'total_bill', y = 'tip', data = tips, size = 2, aspect=4, hue='sex', palette='plasma')

#plt.show()





