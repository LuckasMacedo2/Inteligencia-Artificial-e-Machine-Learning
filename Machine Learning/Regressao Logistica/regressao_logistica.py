# Regressao logistica

import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
import seaborn as sns

train = pd.read_csv('titanic_train.csv')

#print(train.head())
#print(train.info())

# Lidando com dados faltantes

# metodo .isnull()
# True se o dado é null e false senão
#print (train.isnull())

# Tracando um heatmap dos dados faltantes
#plt.figure(figsize=(12,6))
#sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap = 'viridis')

# --------------------------------- Analise exploratoria de dados -------------------------------------------
sns.set_style('whitegrid')

# countplot dos passageiros que sobreviveram ou nao
#sns.countplot(x = 'Survived', data = train, hue = 'Sex', palette='RdBu_r')

# agora das classes
#sns.countplot(x = 'Survived', data = train, hue = 'Pclass', palette='rainbow')

# histograma das idades das pessoas
#train['Age'].hist(bins=30, color = 'darkred', alpha = 0.4)

# Pessoas que acompanhavam outras pessoas no navio
#sns.countplot(x = 'SibSp', data = train)
#train[train['SibSp'] == 0]['Age'].hist(bins = 30)

#train[train['Fare']<70]['Fare'].hist(color = 'green', bins = 50, figsize=(12,6))
# -----------------------------------------------------------------------------------------------------------

# ---------------------------- Tratando os dados faltante ---------------------------------------------------
# Estrategias
# -> Deletar todos os valores, nao e uma boa ideia
# -> Preencher com algo
# -> Preencher os dados com a media de algum outro parametro, no caso aqui a classe.

plt.figure(figsize=(12,6))
#sns.boxplot(x = 'Pclass', y = 'Age', data = train)

# Tratando Idades (Age)

# Funcao, adiciona nas idades faltantes a media das idades presentes na classe
def inputar_idade (cols):
    Idade = cols[0]
    classe = cols[1]

    if pd.isnull(Idade):
        if classe == 1:
            return 37
        elif classe == 2:
            return 29
        else:
            return 24
    else:
        return Idade

# Dados tratados, adicionando a media da s idades baseados na classe em que a pessoa se encontrava
# OK
train['Age'] = train[['Age', 'Pclass']].apply(inputar_idade, axis=1)

# Tratando Cabines (Cabin)
# Contem muitos dados faltantes
# Coluna sera deletada
del train['Cabin'] # ou: train.drop('Cabin', inplace = True)

# Tratando dado faltante de um unico passageiro
# Deletar a linha do mesmo

train.dropna(inplace=True) #dropna() apaga valores faltantes, na

# Verificando dados faltantes graficamente
#sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap = 'viridis')

# metodo get_dummies() transforma variaveis categoricas em variaveis numericas
# drop_first=True, deleta uma das colunas, ja que binario consequentemente sabe se o valor da coluna deletada
sex = pd.get_dummies(train['Sex'], drop_first=True) # Sexo
embark = pd.get_dummies(train['Embarked'], drop_first=True) # Embarcados

# Deletando dados irrelevantes
# Nome, id, ticket, cabin ja deletado
train.drop(['Sex','PassengerId','Name', 'Ticket', 'Embarked'], axis=1, inplace=True)

# Adicionando as novas colunas
# sexo e embarcados
train = pd.concat([train, sex, embark], axis=1)

#print(train.head())
# -----------------------------------------------------------------------------------------------------------

# --------------------------- Modelando ---------------------------------------------------------------------

# importando
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived', axis = 1), train['Survived'], test_size=0.3)

# Criando uma instancia da classe
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)

# Predizendo
predictions = logmodel.predict(X_test)

# Avaliando o modelo
# Acerto ou erro
from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))

# precision mais importante

# Matriz de confusão
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, predictions))

# -----------------------------------------------------------------------------------------------------------

#plt.show()