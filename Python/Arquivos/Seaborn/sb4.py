# Plots de regressao
# Seabron para construcao de modelos lineares
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Regressa entre o total da conta e a gorjeta

# Metodo lmplot()
# Parametros
# eixo x
# exio y
# dados

# Parametros a mais hue

#sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex')

# Modificando o estilo dos pontos
# Parametro
# markers = []

#sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', markers=['o', 'v'])

# Separando os plots
# Parametro
# col = 'str' ou row = 'str', separa em coluna e em linha respectivamente

sns.lmplot(x = 'total_bill', y = 'tip', data = tips, hue = 'sex', col='sex', row = 'time')

plt.show()