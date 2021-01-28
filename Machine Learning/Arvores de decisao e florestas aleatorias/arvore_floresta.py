# Árvores de decisão e florestas aleátorias
import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('kyphosis.csv')

# --- Analise exploratoria de dados ---
sns.pairplot(df, hue='Kyphosis')

# --- Treino e teste ---
from sklearn.model_selection import train_test_split
X = df.drop('Kyphosis', axis = 1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=30)

# --- Árvore de decisão ---
# -- Importando
from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier()

# -- Treinando
dtree.fit(X_train, y_train)

# -- Predicoes
pred = dtree.predict(X_test)

# -- Avaliando o modelo
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))

print('\n\n')

# --- Floresta Aleatoria ---
# -- Importando
from sklearn.ensemble import RandomForestClassifier
# Paramatro n_estimators: quantidade de árvores aleatorias a serem criadas
rfc = RandomForestClassifier(n_estimators=200)

# -- Treinando
rfc.fit(X_train, y_train)

# -- Predicoes
rfc_pred = rfc.predict(X_test)

# -- Avaliando
print(classification_report(y_test, rfc_pred))
print(confusion_matrix(y_test, rfc_pred))

plt.show()
