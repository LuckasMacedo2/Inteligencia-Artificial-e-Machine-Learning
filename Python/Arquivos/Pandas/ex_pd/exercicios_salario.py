import pandas as pd

sal = pd.read_csv('/home/lucas/Área de Trabalho/IC/ex_pd/Salaries.csv')

# ---
# head, econtra os dados iniciais do data frame.
#print (sal.head())

# ---
# metodo .info(), descobri a quantidade de entradas existem no dataframe
print(sal.info())
print ('\n\n\n')

# ---
# Encontrando a média de salarios recebidos, coluna BasePay
# metodo mean()
#print (sal['BasePay'].mean())

# ---
# Encontrando o maior valor de uma coluna
# metodo max()
#print (sal['OvertimePay'].max())

# ---
# Descobrindo o cargo de JOSEPH DRISCOLL
#print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL'])

# ---
# Descobrindo quanto JOSEPH DRISCOLL ganha
#print(sal[sal[''] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

# ---
# Encontrando a pessoa com maior salarios
#print(sal [sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()])
#print(sal.loc[sal['TotalPayBenefits'].idxmax()]) #idxmax encontra o indice do maximo

# ---
# Encontrando a pessoa que paga mais baixo
#print(sal [sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()])
#print (sal.loc[sal['TotalPayBenefits'].idxmin()])

# ---
# Media de todos os funcionarios por ano
#print (sal.groupby('Year').mean()) #groupby('Year') Agrupa as colunas por ano
#print (sal.groupby('Year').mean()['BasePay'])

# ---
# Encontrando os titulos unicos de trabalho
#print (sal['JobTitle'].unique())
# Quantidade de titulos unicos
#print (sal['JobTitle'].nunique())

# ---
# Encontrando os 5 empregos mais comuns
#print (sal['JobTitle'].value_counts()[:5])
#print (sal['JobTitle'].value_counts().iloc[:5])

# ---
# Quantidade de titulos de trabalho apresentados por apenas uma pessoa em 2013.
#print (sum(sal[sal['Year'] ==  2013]['JobTitle'].value_counts() == 1))

# ---
# Quantos pessoas tem a palavra chefe em seu cargo
#def chief_str(title):
#    if 'chief' in title.lower():
#        return True
#    return False
# Aplicando apply(funcao)
#print (sum(sal['JobTitle'].apply(lambda x : chief_str(x))))

# ---
# Existe uma correlacao entre o comprimento da sequencia do titulo do trabalho e o salario
# Metodo corr(), indica se existe uma correlacao entre os dados
#sal['Tamanho da string'] = sal['JobTitle'].apply(len)
#print(sal[['Tamanho da string', 'TotalPayBenefits']].corr())









