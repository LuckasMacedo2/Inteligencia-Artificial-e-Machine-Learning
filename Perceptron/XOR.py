from sklearn.neural_network import MLPClassifier    # Importa o classificador

X = [[1, 1] , [0, 1], [1, 0], [0, 0]]   # Entrada
y = [0, 1, 1, 0]                        # Saida

# Criando o classificador
# solver -> Solucionadir de otimização de peso
#   lbfgs -> Otimizador da familia quase newton
# alpha -> Parametro de penalidade
# hidden_layer_sizes -> Quantidade de camadas ocultas e quantos perceptrons em cada uma delas
# random_state -> Semente para geracao de numeros aleatorios
# activation -> Funcao de ativacao
#   default ‘relu’ -> Retorna o maximo entre 0 e x
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(4,), random_state=1)

# Treino
clf.fit(X, y)

#print(clf.coefs_)
#print()
#print(clf.intercepts_)
#print()

# Coeficientes
c1 = clf.coefs_[0][0]
c2 = clf.coefs_[0][1]
c3 = clf.coefs_[1]

print("Pesos da camada de entrada A = [", end = "")
for c in c1:
    print(f'{round(c,2)}, ', end = '')
print("]")

print("Pesos da camada de entrada B = [", end = "")
for c in c2:
    print(f'{round(c,2)}, ', end = '')
print("]\n")

print("Pesos da camada oculta:  [", end = "")
for i in range(len(clf.coefs_[1])):
    print(f'{round(c3[i][0],2)}, ', end = '')
print("]\n")

print("Vies da camada Oculta: [", end = "")
for c in clf.intercepts_[0]:
    print(f'{round(c, 2)}, ', end = "")
print ("]")

print("Vies da camada de Saida: [", end = "")
for c in clf.intercepts_[1]:
    print(f'{round(c, 2)}', end = "")
print ("]\n")

# Predicao
print("Predizendo A = 1 e B = 0 -> Y =  ", end = "")
print(clf.predict([[1, 0]])[0])
