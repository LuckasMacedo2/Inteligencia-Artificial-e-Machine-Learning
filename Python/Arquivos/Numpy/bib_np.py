## -------------------------------- Numpy -----------------------------------------
# Biblioteca de algebra linear de Python, rapida e eficiente. Feita em C


# importando numpy e a referenciando como np
import numpy as np


### ---------------------------------------- Introducao ------------------------------
# Convertendo uma lista em um array
minha_lista = [1, 2, 3]
x = np.array(minha_lista)
print 'Conversao lista array'
print x


# Criando uma matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = np.array(matriz)
print 'Criando uma matriz'
print y


# Metodo arange
# Cria uma sequencia de numeros
# Parametros, inicio, o final que nao esta incluso na sequencia e o intervalo
z = np.arange(0, 10)
print 'Criando vetores com o arange'
print z
z1 = np.arange(0, 10, 2)
print 'Criando vetores com o arange e com o parametro intervalo'
print z1


# Metodo zeros (ones)
# Cria vetores/matrizes compostos somente por zeros
# Parametros: tamanho do vetor/matriz
a = np.zeros(3)
print 'Criando vetores/matrizes apenas com zeros'
print a


# Matriz identidade
# Metodo eye
# Parametro: Tamanho n da matriz
I = np.eye(4)
print 'Criando uma matriz identidade'
print I


# Metodo linspace
# Semelhante ao arange, inicio, fim e quantidade de numeros que estao
# igualmente espacados
b = np.linspace(0, 10, 3)
print 'Metodo linspace'
print b


# Biblioteca random
# Cria numeros aleatorios, a partir de uma distribuicao uniforme
# todos possuem igual probabilidade de serem retirados
r = np.random.rand(10)
print 'Numeros aleatorios'
print r


# Metodo randn
# Cria numeros aleatorios, retirados de uma distribuicao normal, com:
# media 0 e desvio padrao 1
rn = np.random.randn(10)
print 'Numeros aleatorios'
print rn


# Metodo randint
# Cria numeros aleatorios e inteiros, dentro de um intervalo
ri = np.random.randint(0, 100, 10)
print 'Numeros inteiros aleatorios'
print ri


# Metodo round
# Determina o numero de casas decimais
# Parametros: numero(s) a serem arredondados e quantidade de casas decimais que o
# numero deve ter
ro = np.round([0.0001, 0.9, 999.999, 100.00190912093], 0)
print 'Arredondando numeros'
print ro


# Metodo reshape
# Faz com o vetor assuma diferentes formatos
arr = np.random.rand(25)
print 'Vetor'
print arr

arrs = arr.reshape((5,5))
print 'Transformando o vetor em uma matriz 5x5'
print arrs


# Tamanho das matrizes/vetores
# Atributo: shape
print 'Tamanho de matrizes/vetores'
print arrs.shape


# Determinando o maior valor de um vetor. 
# Metodo: max()
print 'Determiando o maior valor do vetor {one}'.format(one = arr)
print 'Maior valor = {one}'.format(one = arr.max())
# Para determinar o menor valor utilizar o metodo min, equivalente ao max


# Determinando o indice ao qual o maior elemento se encontra
# Metodo: argmax()
print 'Determinando o indice ao qual o maior elemento se encontra.'
print 'Vetor: {one}'.format(one = arr)
print 'Indice = {one}'.format(one = arr.argmax())
# Para determinar o indice do menor valor utilizar o metodo argmin(),
# equivalente ao argmax()
### ---------------------------------------- End ----------------------------------------------






















