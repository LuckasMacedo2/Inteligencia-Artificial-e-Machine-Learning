#--------------------------- Group by --------------------------------------------
#Agrupar informacoes que contem mesmos elementos em uma coluna e realizar operacoes
#nas outras colunas.

import pandas as pd

# Criar um data frame

data = {'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Nome': ['Sam', 'Charlle', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Venda': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

print (df)


#---- Agrupamento
#metodo: groupby(Quem sera agrupado)
gruop = df.groupby('Empresa')

#Exemplo soma das vendas por empresa
print (gruop.sum())

#Sao aplicados em colunas em que faz sentido para o python
#Metodo     Em python
#Soma       gruop.sum()
#Media      gruop.mean()
#todos      gruop.describe()
#contar     gruop.count()

#Metodo describe() realiza operacoes no grupo e retorna um relatorio   
print (gruop.describe())

