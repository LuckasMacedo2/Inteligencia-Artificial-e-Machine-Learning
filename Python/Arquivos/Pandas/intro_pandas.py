## --------------------------------------------- Pandas -------------------------------------
# Semelhante ao excel
# Visualizacao de dados. Grande quantidade de tipos de dados


## --------------------------------------------- Series --------------------------------------
# Series: Objeto basico do Pandas. Pode conter qualquer coisa, tipos e metodos

import numpy as np

import pandas as pd #pd padrao de pandas

labels = ['a', 'b', 'c']

minha_lista = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a':10, 'b':20, 'c':30}

# Transformando em series

# Series(dados, indice), a ordem importa aqui. O indice e a referencia para os dados
print (pd.Series(data=minha_lista,index=labels)) #Fica parecida com os dicionario

# Acessando elementos da Series
serie = pd.Series(data=minha_lista,index=labels)
# Nome_variavel['chave']
print (serie['b'])

# Operacos aritmeticas. Operacoes sao baseadas no indece.
# Soma: Soma os elementos baseados no indice.

serie1 = pd.Series([1, 2, 3, 4], index = ['EUA', 'Alemanha', 'URSS', 'Japao'])
serie2 = pd.Series([1, 2, 3, 4], index = ['EUA', 'Alemanha', 'Italia', 'Japao'])

serie3 = serie1 + serie2

print(serie3)


## --------------------------------------------- Data Frame -------------------------
# Objeto principal do pandas, um conjunto de series

# seed (numero) Os numeros aleatorios gerados serao iguais em qualquer computador em que
# o codigo for executado.
np.random.seed(101)

# DataFram(dados, indice, colunas)
df = pd.DataFrame(np.random.randn(5,4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())

print (df)

# Selecionando dados, Nome_data_frame['indice'], retorna uma serie
# Um unico
print (df['W']) 
# Varios, passar uma lista de indices
print (df[['W', 'Z']])
# Outro metodo
# nome_data_frame.indice
print(df.W)

# Criando uma nova coluna
df['new'] = df['W'] + df['X']
print (df)

# Deletando uma coluna
# axis = eixo. eixo 0 = indices
# nome_data_frame = nome_data_frame.drop('coluna', axis = 1)
df = df.drop('new', axis = 1)
print (df)
# Outra forma, passar o parametro inplace = true no metodo drop, ficando assim
# nome_data_frame.drop('coluna', axis = 1, inplace = True)


# Acessando elementos
# Metodo loc['indice'], Selecao baseado no nome dos indices e colunas
print(df.loc['A']) #Serie de elementos que compartilham o mesmo elemento
# Acessando mais de um elemento passar uma lista de elementos
# Metodo loc[[lista_indices]]
print(df.loc[['A', 'B'],['X', 'Y','Z']])

# Metodo para acessar elementos baseados em numpy, utilizando indices
# Metodo: iloc. Baseados em metodos baseados em numpy
print (df.iloc[1:4,2:])


## ----- Selecao Condicional -----
# Selecao de dados, baseados em criterios
from numpy.random import randn
np.random.seed(10)

df1 = pd.DataFrame(np.random.randn(5,4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())

print (df1)

# Testes condicionais semelhantes ao numpy array
print (df1 > 0)

# Teste condicional em uma linha
print (df1[df1['W']>0]) # Retorna o data frame somente com w onde w > 0

# Selecao multipla, usar operadores logicos &(e), |(ou) (and e or, so comparada bolleano)
print (df1[(df1['W'] > 0) & (df1['Y'] > 1)])

# Resetando os indices, reseta o data frame ao padrao original.
df1.reset_index(inplace = True) # inplace = True alterando permanentemente o data frame
print (df1)

# Adicionando uma nova coluna, deve possuir o mesmo tamanho que a coluna do data frame
col = 'RS RJ SP AM SC'.split()
df1['Estado'] = col
print (df1)

# Setando uma coluna como indice do data frame
# metodo nome_data_frame.set_index('nomeColuna')
df1.set_index('Estado', inplace = True)
print (df1)


## ----- Indice multinivel -----

# Niveis de indice
outside = ['G1', 'G1','G1','G2','G2','G2'] # Lista
inside = [1, 2, 3, 1, 2, 3] # Lista
hier_index = list(zip(outside, inside)) # zip -> cria uma lista de tuplas, associando os valores
hier_index = pd.MultiIndex.from_tuples(hier_index) # Cria um objeto de indice de multinivel

df2 = pd.DataFrame(np.random.randn(6,2), index = hier_index, columns = ['A', 'B'])
print (df2)

# Acessando elementos de multinivel
print (df2.loc['G1'])

# Outro metodo
# metodo: nome_data_frame.xs('Nome_indice')
print (df2.xs('G1'))

# Especificando nomes para os indices
# metodo: nome_data_frame = ['Nome1', 'Nome2', 'NomeN']
df2.index.names = ['Grupo', 'Numero']
print (df2)


## ----- Dados Ausentes -----
dic = {'A':[1, 2, np.nan], 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]} #np.nan = valor ausente
df3 = pd.DataFrame(dic)
print (df3)

# Eliminando valores ausentes
# metodo: nome_data_frame.dropna(thresh=quantidade_de_valores_ausente)
# thresh = elimina as linhas que possuirem a quantidade de valores especificados
print (df3.dropna()) #, se nao for especificado o parametro, exclui toda a linha que contem o valor ausente
print (df3.dropna(thresh=2))

# Substituindo os valores ausentes por qualquer coisa
# metodo: nome_data_frame.fillna(value = 'Fill na')
# parametro: method = 'ffill'; preenche com valores anteriores 
print (df3.fillna(value = 0))






















































































