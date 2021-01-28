## -------------------------------- Operacoes com vetores com Numpy ------------------------------
## Referencia: https://docs.scipy.org/doc/numpy/reference/


import numpy as np


arr = np.arange(0, 16)
print 'Vetor: {one}'.format(one = arr)


# Operacoes entre vetores: +, -, *, /, ** (exponenciacao).
# Os vetores necessitam de ter o mesmo numero de elementos
# Soma de dois vetores
arr1 = arr + arr
print 'Soma de vetores'
print arr1


# Operacoes com escalares
# Opera com o escalar em todos os elementos do array
arr2 = arr + 1
print 'Soma de um escalar e um vetor'
print arr2


# Raiz quadrada de um vetor: np.sqrt(vetor)
# Exponenciacao de um vetor: np.exp(vetor)
# Media de um vetor:         np.mean(vetor)
# Desvio padrao:             np.std(vetor)
# Seno de um vetor:          np.sin(vetor)


