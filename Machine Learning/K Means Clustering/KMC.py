# K Mean Clustering

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Forjando dados falsos aleatorios baseados em clusters
# Baseados na distribuicao guasiana
# make_blobs
from sklearn.datasets import make_blobs

data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=50)
# Parametros:
# n_samples = "numero de linhas"
# n_features = numero de parametros, "numero de colunas"
# center = qtd de centroides
# std = desvio padrão
# Retorna uma tupla

#plt.figure(figsize=(12,8))
#plt.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap='rainbow')

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
# n_clusters = numero de clusters

# Algoritmo de aprendizagem nao supervisionada logo nao e necessario
# dividir os dados em teste e treino

# --- Treinando ---
kmeans.fit(data[0])

f,(ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(12,8))
ax1.set_title('Kmeans')
ax1.scatter(data[0][:,0], data[0][:,1], c = kmeans.labels_, cmap='rainbow')

ax2.set_title('Original')
ax2.scatter(data[0][:,0], data[0][:,1], c = data[1], cmap='rainbow')

plt.show()