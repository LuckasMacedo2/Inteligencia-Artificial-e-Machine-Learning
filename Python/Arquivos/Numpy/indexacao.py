## -------------------------------- Indexacao de vetores com Numpy ------------------------------

# np nome padrao para referenciar numpy
import numpy as np


# Criando o vetor
arr = np.arange (0, 30, 3)
print 'Vetor = {one}'.format (one = arr)


# Acessando um valor do array
print arr[3]


# Acessando elementos entre um indice i e j, o valor de j nao esta incluso
# Formato: vetor[i:j]
print arr[2: 5]


# Acessando desde o incio ate o indice j, j nao esta incluso
# Formato: vetor[:j]
print arr[:5]


# Acessando desde o indice i e o final do vetor
# Formato: vetor[i:]
print arr[2:]


## ------ Servem tambem para alterar os valores do vetor. ------
# Por exemplo definido que os valores a partir do terceiro indice do vetor arr
# sao igual a 10.
print 'Antes: {one}'.format(one = arr)
arr[3:] = 10
print 'Depois: {one}'.format(one = arr)


# --------------------- Vetores bidimensionais -----------------------------------
# Criando um vetor de duas dimensoes
# Metodo: reshape
arr1 = np.arange(50).reshape((5, 10))
print arr1

# ** Slice == fatias de um vetor

# Acessando elementos de uma matriz
# vetor [...] [...], primeiro colchete linha, segundo colchete coluna

print 'Acessando elementos de uma matriz'
print arr1[1:2][:]

# Tomar cuidado pois ao definir um vetor a partir de outro o Python considera
# que o segundo e uma referencia do outro, comm  isso ao alterar valores no
# segundo, altera-se no primeiro tambem.

print 'Problema no Python'
print 'Primeiro vetor, antes'
print arr1
arr2 = arr1[:3]
arr2[:] = 100
print 'Problema'
print 'Primeiro vetor'
print arr1
print 'Segundo vetor'
print arr2

# Para contornar o problema utilizar o metodo copy
arr3 = np.arange(50).reshape((5, 10))
arr4 = arr3[:3].copy();
arr4[:] = 100
print 'Segundo vetor com parte do primeiro copiada'
print arr4
print 'Primeiro vetor'
print arr3
print 'Segundo vetor'
print arr4


# Outra notacao para acessar elementos em vetores de duas dimensoes
# Semantica vetor[i:j , k:l], i:j -> linha, k:l -> coluna
print 'Extraindo elemento 0:2, 2'
print arr4[0:2, 2]


# E possivel realizar operacoes logicas com os vetores, que podem vir a retornar
# outro vetor com as respostas.

# Por exemplo: Quando os valores de arr3 sao maiores que 30?
print 
# Como retorno ha um vetor booleano para cada elemento do vetor.

print 'Extraindo apenas os valores de arr3 que sao maiores que 30'
bol = arr3 > 30 # bol recebe um vetor de boolenos.
print arr3[bol] # Pega apenas os valores que satisfacam a condicao acima.

























