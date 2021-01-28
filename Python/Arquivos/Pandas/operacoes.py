# -------------------------- Operacoes Pandas --------------------------
import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2':[111, 222, 333, 111], 'col3':['abc', 'def', 'ghi', 'xyz']})
df.head()


# --- Dados unicos ---

# Metodo: unique()
# Selecao de dados unicos, retorna uma lista que nao contem valores repetidos de uma coluna
print ('\nElementos unicos')
print (df['col2'].unique())


# Metodo: nunique()
# Retorna a quantidade de elementos distintos, ou seja, o tamanho do vetor resposta do metodo anterior.
print ('\nQtd elementos distinto')
print (df['col2'].nunique())

# Metodo: value_counts()
# Uniao dos dois metodos anteriores, retorna os elementos distintos e quantas vezes aqueles elemento aparece
print ('\nQtd elementos distinto e quantas vezes cada um aparece')
print (df['col2'].value_counts())


# --- Selecao de dados ---

print ('\nSelecionando dados de duas colunas distintas')
print (df[(df['col1'] > 2) & (df['col2'] == 444)])

# Metodo: apply(funcao)
# Permite a aplicacao de suas funcoes no data frame
print ('\nutilizando funcoes')
def vezes2(x):
    return 2*x

print(df['col1'].apply(vezes2))
# Com funcoes lambda
print(df['col1'].apply(lambda x : x*x))

# Metodo: del df['coluna_a_ser_deletada']
# Metodo padrao do python, deleta a coluna especificada

print ('\nDeletando uma coluna')
del df['col2']
print (df)

#df.columns: Retorna as colunas do data frame.
#df.index:   Retorna os indices do data frame.

# Metodo: sort_values(by = 'coluna_a_ser_ordenada')
# Ordena a partir da coluna especificada, o parametro inplace e false por default  
print ('\nOrdenando uma coluna')

print (df.sort_values(by = 'col3', inplace = True))

# Metodo: isnull()
# Retorna boleanos que indicam se o df possui valores iguais a null
print('\nValores nulos')
print (df.isnull())

# Metodo: dropna()
# Apagar valores NAN, a linha toda por default

df1 = pd.DataFrame({'col1': [1, 2, 3, np.nan], 'col2':[np.nan, 222, 333, 111], 'col3':['abc', 'def', 'ghi', 'xyz']})
df1.head()

print ('\nApagando valores Nan')
print (df1.dropna())

# Metodo: fillna(value = valor)
# Substitui os Nan pelo valor especificado

# Metodo: pivot_table(values = valor, index = indice, colums = coluna)
# Permite reajustar a dataframe, para melhorar a visualizacao


























