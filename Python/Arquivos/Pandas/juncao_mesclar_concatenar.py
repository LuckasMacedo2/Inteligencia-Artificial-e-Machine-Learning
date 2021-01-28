# ------------------------------- Mesclar, juntar e Concatenar Data Frames -----------
import pandas as pd

print ('\nConcatenacao')

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']}, index = [0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']}, index = [4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']}, index = [8, 9, 10, 11])

# --- Concatenacao ---
# Uni dois data frames, especificar o eixo, com isso os df devem possuir o mesmo
# tamanho no eixo de uniao.

#metodo: pd.concat([data_frame1, data_frame2, ...], axis = 1), axis = eixo, por defult e zero

print (pd.concat([df1, df2, df3]))


# ---- Mesclar ---
#Unir df a partir de algum elemento em comum
#Metodo: merge(df1, df2, how = uniao_tabelas_sql , on = 'key'), on indica
# a partir do que sera mesclado
# how, pode ser, linear, outer.
print ('\nMesclar')
esquerda = pd.DataFrame({'key': ['K0', 'K1', 'K1', 'K3'],
                         'A':   ['A0', 'A1', 'A2', 'A3'],
                         'B':   ['B0', 'B1', 'B2', 'B3']})
direita = pd.DataFrame({'key': ['K0', 'K1', 'K1', 'K3'],
                         'C':  ['C0', 'C1', 'C2', 'C3'],
                         'D':  ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(esquerda, direita , on = 'key'))
                       

# --- Juntar ----
# Juntar dataframes que podem possuir diferencas em seus indices. Pode colocar valores
# nos indices em que estao faltando elementos. Nao cria um novo data frame, os outros dois
# metodos criam um novo data frame.

#Metodo: df1.join(df, how = 'outer')


esquerda1 = pd.DataFrame({'A':   ['A0', 'A1', 'A2'],
                         'B':   ['B0', 'B1', 'B2']},
                        index = ['K0', 'K1', 'K2'])

direita1 = pd.DataFrame({ 'C':  ['C0', 'C2', 'C3'],
                         'D':  ['D0', 'D2', 'D3']},
                         index= ['K0', 'K2', 'K3' ])
print ('\nJuntar')
print (esquerda1.join(direita1))












