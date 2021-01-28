from sklearn.neural_network import MLPClassifier    # Importa o classificador

X = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
y = [[0, 0], [0, 1], [1, 1], [0, 1], [1, 0], [0, 0], [1, 0], [1, 1]]

# Criando o classificador
# solver -> Solucionadir de otimização de peso
#   lbfgs -> Otimizador da familia quase newton
# alpha -> Parametro de penalidade
# hidden_layer_sizes -> Quantidade de camadas ocultas e quantos perceptrons em cada uma delas
# random_state -> Semente para geracao de numeros aleatorios
# activation -> Funcao de ativacao
#   default ‘relu’ -> Retorna o maximo entre 0 e x
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6,), random_state=1)

# Treino
clf.fit(X, y)

# Coeficientes
c1 = clf.coefs_[0][0]
c21 = clf.coefs_[0][1]
c2 = clf.coefs_[0][2]
c3 = clf.coefs_[1]

print("Pesos da camada do sensor da esquerda: [", end = "")
for c in c1:
    print(f'{round(c,2)}, ', end = '')
print("]")


print("Pesos da camada do sensor da frente: [", end = "")
for c in c21:
    print(f'{round(c,2)}, ', end = '')
print("]")


print("Pesos da camada do sensor da direita: [", end = "")
for c in c2:
    print(f'{round(c,2)}, ', end = '')
print("]\n")

print("Pesos da camada oculta saida roda esquerda: [", end = "")
for i in range(len(clf.coefs_[1])):
    print(f'{round(c3[i][0],2)}, ', end = '')
print("]")

print("Pesos da camada oculta saida roda direita:  [", end = "")
for i in range(len(clf.coefs_[1])):
    print(f'{round(c3[i][1],2)}, ', end = '')
print("]\n")

print("Vies da camada Oculta: [", end = "")
for c in clf.intercepts_[0]:
    print(f'{round(c, 2)}, ', end = "")
print ("]\n")

print("Vies da camada de saida da roda esquerda: [", end = "")
#for c in clf.intercepts_[1]:
print(f'{round(clf.intercepts_[1][0], 2)}]')
print("Vies da camada de saida da roda direita: [", end = "")
print(f'{round(clf.intercepts_[1][1], 2)}]\n')
#print ("]\n")

# Predicao
print("Informe o valor do sensor da esquerda: ", end = "")
esquerda = int(input())

print("Informe o valor do sensor da frente: ", end = "")
frente = int(input())

print("Informe o valor do sensor da direita: ", end = "")
direita = int(input())

y = clf.predict([[esquerda, frente, direita]])[0]
print(f"Predizendo Esquerda = {esquerda}, Frente = {frente} e Direita = {direita} -> Roda esquerda = {y[0]} e Roda direita = {y[1]}", end = "")
