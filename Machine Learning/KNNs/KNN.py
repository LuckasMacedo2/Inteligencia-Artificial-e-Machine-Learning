# ------------------------------------ KNN ----------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Dados criptografados
df = pd.read_csv('Classified Data', index_col = 0)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# --- Normalizando os parametros ---
scaler.fit(df.drop('TARGET CLASS', axis = 1))
df_normalizado = scaler.transform(df.drop('TARGET CLASS', axis = 1))
# .trasnform() tira a media e desvio padrao e recalcula ponto a ponto no conjunto de dados

df_param = pd.DataFrame(df_normalizado, columns = df.columns[:-1])

# --- Divindo os dados ---
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df_param, df['TARGET CLASS'], test_size=0.3)

# --- KNN ---
from sklearn.neighbors import KNeighborsClassifier

# Parametro: Numero de vizinhos
knn = KNeighborsClassifier(n_neighbors=1)

# Treinando
knn.fit(X_train, y_train)

# Predizendo
pred = knn.predict(X_test)

# Avaliando
from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)
    error_rate.append(np.mean(pred != y_test))

print (error_rate)

plt.figure(figsize=(14,8))

plt.plot(range(1,40), error_rate, color = 'blue', linestyle = 'dashed', marker = 'o')
plt.xlabel('K')
plt.ylabel('Taxa de erro')


plt.show()