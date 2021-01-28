## -------------------------------- Exercicios ------------------------------

import numpy as np

# Criar uma matriz de 10 zeros
m1 = np.zeros(10)
print m1

# Criar uma matriz com 10 1's
m2 = np.ones(10)
print m2

# Criar uma matriz com 10 5's
m3 = np.ones(10)*5
print m3

# Criar um vetor de inteiros de 10 a 50
v1 = np.arange(10, 51)
print v1

# Criar um vetor de inteiros pares de 10 a 50
v2 = np.arange(10, 51, 2)
print v2

# Criar uma matriz 3x3 de 0 a 8
m4 = np.arange(0,9).reshape(3, 3)
print m4

# Criar uma matriz identidade 3x3
m5 = np.eye(3)
print m5

# Gerar numeros aleatorios entre 0 e 1
n1 = np.random.rand(1) #Parametro quantidade de elementos do vetor
print n1

# Gerar um vetor de 25 numeros aleatorios de uma distribuicao normal
v3 = np.random.randn(25) #randn() os numeros sao retirados de uma distribuicao normal
print v3

# Criar uma matriz indo 0 a 1 com passo 0.01
m5 = np.arange(0, 1.01, 0.01) #Ou: np.arange(0, 101)/100
print m5

# Criar um vetor de tamanho 20 de 0 a 1 igualmente espacado
v4 = np.linspace(0, 1, 20)
print v4




