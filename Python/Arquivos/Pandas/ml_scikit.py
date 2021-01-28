# Scikit learning: Biblioteca de Python para trabalhar com Machine Learning

from sklearn import datasets # datasets contem dados para treino

iris = datasets.load_iris()

#print (iris.data)
#print (iris.target)

# Dividindo o dataset, conjunto de dados em uma porcentagem para treino e teste.
# test_size = tamanho_teste, define a porcentagem que sera do teste
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split (iris.data, iris.target, test_size=0.4, random_state=0)

from sklearn import svm


# Treinando o modelo
clf = svm.SVC(kernel = 'linear', C = 1).fit(X_train, y_train)

# Verificando o score do treino
print (clf.score(X_test, y_test))
