# PCA
# Busca encontrar a combinacao linear entre o compoente de resposta e todos
# os demais componentes
# o modelo se trona menos suscetivel a ruidos

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer() # equivalente a um dicionario

df = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

# Os componentes sao combinacoes lineares das demais variaveis
# Passando os 30 parametros, dimensao 30, para dimensao 2

# --- Transformando os dados ---
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# -- Treinando --
scaler.fit(df)

scaled_data = scaler.transform(df) # Variâncias unitárias

# ------------------------------ PCA --------------------------------

# - Importando -
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
# Parametro
# n_components = numero de componentes

# --- Treinando o PCA ---
pca.fit(scaled_data)

x_pca = pca.transform(scaled_data)

# Analise visual
#print (x_pca.shape)
#print (scaled_data.shape)
# Resultou na diminuicao das dimensoes de 30 para 2 dimensoes

# Graficos
#plt.figure(figsize=(12, 8))
#plt.scatter(x_pca[:, 0], x_pca[:, 1], c = cancer['target'], cmap='plasma')
# Parametro
# c coloca as cores conforme algo
#plt.xlabel('Primeiro compoenente principal')
#plt.ylabel('Segundo compoenente principal')

# Menos ruido
# pca.components_, retorna so componentes que sao uma tupla (2, 30)
# e cada compomente representa a correlacao entre aquela variavel e o primeiro componente

# -- Mapa de calor --
df_comp = pd.DataFrame(pca.components_, columns=cancer['feature_names'])

plt.figure(figsize=(12, 8))
sns.heatmap(df_comp, cmap='plasma')

plt.show()