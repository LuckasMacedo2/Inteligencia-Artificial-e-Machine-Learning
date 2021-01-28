# Suport Vector Machine

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

#print(cancer['DESCR'])

# -- Configurando o dataframe --
df_cancer = pd.DataFrame(cancer['data'], columns=cancer['feature_names'])

df_target = pd.DataFrame(cancer['target'], columns = ['Cancer'])

from sklearn.model_selection import train_test_split

# np.ravel: Converte os dados em array (vetor)
X_train, X_test, y_train, y_test = train_test_split(df_cancer, np.ravel(df_target), test_size=0.3, random_state=101)

from  sklearn.svm import SVC
model = SVC()

model.fit(X_train, y_train)

pred = model.predict(X_test)

from sklearn.metrics import  classification_report, confusion_matrix
# --- Desempenho ruim ---
#print(classification_report(y_test, pred))
#print(confusion_matrix(y_test, pred))

# --------------------- Grid Search ------------------------------------------------------------------
# Utilizando o Grid Search para melhorar o desempenho
# Testa uma combinacao de parametros e encontra o melhor e netao retreina
# o modelo para melhorar o modelo. Lento, testa todas as combinacoes de
# variaveis possiveis.

# Tem como parametro (funcao) um discionario
# C -> custo de classificacoes erradas.
# Quanto maior maior o overfit. Maior a penalizacao por erros na classificacao.
# gamma -> Relacionado ao tipo de kernel utilizado, altera a funcao gaussiana utilizada
#  Quanto menor maior a variacao e menor o vies.

# Portanto o importante e econtrar um bom vies e variancias
param_grid = {'C':[0.1, 1, 10, 100, 1000], 'gamma':[1, 0.1, 0.01, 0.001, 0.0001], 'kernel':['rbf']}

from sklearn.model_selection import GridSearchCV
# Parametros
# 1: Modelo de classificação
# 2: os parametros a serem alterados
# 3: refit=True, permite que o modelo se retreine
# 4: verbose = , altera os outputs ao longo da otimizacao, por default 0
# Mostra algo na saida
grid = GridSearchCV(SVC(), param_grid, verbose = 3)

# -- treinando
grid.fit(X_train, y_train)

# - Verificando os melhores parametros encontrados
print(grid.best_params_) # Retorna um dicionario

pred = grid.predict(X_test)
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))


plt.show()