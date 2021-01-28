import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

USA_Housing = pd.read_csv('USA_Housing.csv')

print (USA_Housing.info())

# ---
# Vendo o graficos de distribuicao
#sns.pairplot(USA_Housing)

#plt.show()

# --------------------------------------------------------------------
# Tentativa de usar as demais variaveis para predizer o valor da casa
# Verificar o grafico.
# X = Parametros, o que vai predizer o modelo, Variaveis explicativas
# Y = O que sera predito pelo modelo
# --------------------------------------------------------------------

#sns.heatmap(USA_Housing.corr())

#plt.show()
# ---

print (USA_Housing.columns)

# --- Tratamento de dados ---
# Variaveis peditorias
# X = Todo mundo menos o preco e o endereco, o preco deve ser predito
X = USA_Housing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]


# O que sera preditor, o preco neste caso
y = USA_Housing['Price']
# ------

# Importando o scikit o metodo de split
# train_test_split, separa os dados X e Y em treino e teste
from sklearn.model_selection import train_test_split

# -- train_test_split
# Divide os dados em duas partes, o ponto de corte e igual
# Divisao baseado em um algoritmo aleatorio
# Retorna uma tupla de 4 elementos, na seguinte ordem (train = treino, test = teste)
# random_state: garante que recebamos a mesma divisão toda vez que executarmos o codigo
X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.4, random_state= 101)

# Importando o modelo linear
from sklearn.linear_model import LinearRegression

# Criando a instancia da classe do modelo

ln = LinearRegression()

# -- fit
# Encontra os parametros do modelo linear, tendo como parametros da funcao
# os valores de X de treino (X_train) e y de treino (y_train)
ln.fit(X_train, y_train)

# Verificando o modelo
# Intercepcao do modelo e o eixo X
print(ln.intercept_)

# Coeficientes do modelo
print(ln.coef_)

# Interpretando os coeficientes
coefs = pd.DataFrame(ln.coef_, X.columns, columns=['Coefs'])

print (coefs)

# Predizendo valores das casas
house_predict = ln.predict(X_test)
print(house_predict)

# --- Verificando o quao bom foram as previsoes das casas ---
# scatter
#plt.figure(figsize=(12,6))
#plt.scatter(y_test, house_predict)
#plt.show()

# graficos dos erros residuos
#sns.distplot((y_test - house_predict)) # Valor real - valor previsto pelo modelo
# Quanto mais proximo de uma distribuicao normal o grafcio resultar melhor

#plt.show()

# ---

# --- Metricas ---
# Medindo a precisao do modelo
# erro absoluto medio (MAE)
# media do quadrado do erro (MSE), unidade resultante e sem sentido
# raiz do erro medio quadrado (RMSE), raiz da media do quadrado do erro

from sklearn import metrics

print('MAE: ', metrics.mean_absolute_error(y_test, house_predict))
print('MSE: ', metrics.mean_squared_error(y_test, house_predict))
print('RMSE: ', np.sqrt(metrics.mean_absolute_error(y_test, house_predict)))
