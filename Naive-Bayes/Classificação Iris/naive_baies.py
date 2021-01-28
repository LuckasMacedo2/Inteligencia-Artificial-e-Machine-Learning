import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Metricas
from sklearn.metrics import classification_report, confusion_matrix

from sklearn import datasets

# Carregando os dados
iris = sns.load_dataset('iris')

# Gráfico dos dados
sns.pairplot(iris, hue = 'species', palette='rainbow')
plt.show()

# Importando o modelo e criando o objeto da classe
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

# Treino sem separar os dados
X = iris.drop('species', axis = 1) # Variaveis que seram utilizadas para predizer
y = iris['species'] # Variavel a ser predita

gnb.fit(X, y)

predito = gnb.predict(X)

def metricas(y, predito):
    print("Confusion Matrix (Matriz de confusao)")
    print(confusion_matrix(y, predito))
    print("Classification Report (Reporte de classificação)")
    print(classification_report(y, predito))


print("\nPredicao sem separacao em dois conjuntos, teste e treino")
metricas(y, predito)

# Teste com separacao dos dados para treino e teste
from sklearn.model_selection import train_test_split
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, random_state = 101, test_size=0.3)


gnb.fit(X_treino, y_treino)



predito_sep = gnb.predict(X_teste)


print("\n\nPredicao com separacao em dois conjuntos, teste e treino")
metricas(y_teste, predito_sep)


