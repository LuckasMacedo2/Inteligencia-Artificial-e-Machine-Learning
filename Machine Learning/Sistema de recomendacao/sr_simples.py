# Sistema de recomendacao simples
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

column_name = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data', sep = '\t', names = column_name)

#print (df.head())

movie_title = pd.read_csv('Movie_Id_Titles')

# Mescalndo o dataframe
df = pd.merge(df, movie_title, on = 'item_id')

# Media de avaliacao dos filmes
#print (df.groupby('title')['rating'].mean().sort_values(ascending=False))

# Contagem dos filmes mais vistos
#print (df.groupby('title')['rating'].count().sort_values(ascending=False))

#  --- Agrupandos os dados ---
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())

#print(ratings.head())

ratings['count'] = pd.DataFrame(df.groupby('title')['rating'].count())

#print(ratings.head())

# --- Analise exploratoria ---
plt.figure(figsize=(12, 8))

# Histograma da quantidade de usuarios que viram o filme
#ratings['count'].hist(bins=70)

# Histograma da media de estrelas dadas ao filme
#ratings['rating'].hist(bins=70)

# Joinplot dos dados
#sns.jointplot(x='rating', y='count', data=ratings, size=8)
# Verifica-se que quanto maior a media maior a quantidade de visualizacoes do filme

# Criando um data frame de pivo
moviemat = df.pivot_table(index='user_id', columns='title', values='rating')
#print(moviemat.head())

# ---- Sistema de recomendacao para dois filmes ----
# Star Wars e Liar Liar
ratings.sort_values('count', ascending=False)

# Fatiando o data frame
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']

# Metodo
# df.corrwith(dataframe) - esepecifica os dataframes ao qual as correlacoes serao calculadas
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
# Similaridade entre as pessoas que assistiram o filme e star wars
#print(similar_to_starwars.head())

similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)
# Similaridade entre as pessoas que assistiram o filme e star wars
#print(similar_to_starwars.head())

# Recriando os dataframes, retirando os NAN

# -- Star Wars --
corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)

#print (corr_starwars.sort_values('Correlation', ascending=False).head(10))

corr_starwars = corr_starwars.join(ratings['count'])
#print (corr_starwars[corr_starwars['count'] > 100].sort_values('Correlation', ascending=False).head(10))

# -- Liar Liar
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.dropna(inplace=True)

corr_liarliar = corr_liarliar.join(ratings['count'])
print (corr_liarliar[corr_liarliar['count'] > 100].sort_values('Correlation', ascending=False).head(10))

#corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])

#splt.show()