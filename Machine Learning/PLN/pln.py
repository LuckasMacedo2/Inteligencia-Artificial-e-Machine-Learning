# Processamento de linguagem natural

# Lista com as mensagens
#messages = [line.rstrip() for line in open('SMSSpamCollection')]

#print(len(messages))
#print(messages[0])

# Transformando a lista em pandas
import pandas as pd
messages = pd.read_csv('SMSSpamCollection', sep='\t', names=['Label', 'Message'])

# Descricao das mensagens
#print (messages.describe())

# Descricao a partir das labels
#print (messages.groupby('Label').describe())

# Visualizacao dos dados
import matplotlib.pyplot as plt
import seaborn as sns

# Visualizando o tamanho das mensagens
messages['Lenght'] = messages['Message'].apply(len)

# Histograma do tamanho das mensagens
#plt.figure(figsize=(12, 8))
#messages['Lenght'].plot(kind='hist', bins=50)

# Verificando a maior mensagem do conjunto de dados
#print (messages[messages['Lenght'] == 910]['Message'].iloc[0])

# Plots separados entre spam ou ham
#messages.hist(bins=100, column='Lenght', by='Label', figsize=(12, 8))

# Pontuacoes podem prejudicar o modelo

import string

# -------------------------------- String --------------------------------------------
# string.punctuation() Retorna uma lista com todas as pontuacoes possiveis
#print(string.punctuation)

#mss = 'Mensagem de exemplo, com pontuação'
#sempontu = [car for car in mss if car not in string.punctuation]
#print(sempontu)
#sempontu = ''.join(sempontu) # Coloca '' (aqui nada) entre cada elemento da lista
# Ou seja, coloca o caracter entre os elementos da lista
#print(sempontu)
# ------------------------------------------------------------------------------------

from nltk.corpus import stopwords

# -------------------------------- StopWords --------------------------------------------
# stopwords, palavras comuns sem muito valor, relevante sua retirada

# .word('Idioma')
#print (stopwords.words('english'))

# Retirando as stopwords exemplo
#tst = 'sample message! Notice: it has punctuation.'
#clean_msg = [word for word in tst.split() if word.lower() not in (stopwords.words('english'))]
#print(clean_msg)
# ------------------------------------------------------------------------------------

# Limpa os emails
def text_process(msg):
    # Retirando as pontucoes
    nopunc = [char for char in msg if char not in string.punctuation]

    # Juntando para formas as palavras
    nopunc = ''.join(nopunc)

    # Removendo as stopwords
    sms = [word for word in nopunc.split() if word.lower() not in (stopwords.words('english'))]
    return sms

# Criando tokens
# Transforma as mensagens em uma lista de palavras importantes

#print(messages['Message'].head().apply(text_process))

# --- Vetorizacao ---
# Stiming
# Palavras com sentido semelhante. Transforma palavras semelhantes em uma unica palavra

# Criando o vetor a partir dos dados
from sklearn.feature_extraction.text import CountVectorizer
# CountVectorizer: Transforma as strings em matrizes esparsas (mais 0)
# analyzer: Permite a aplicacao de uma funcao nas mensagens antes da conversao

bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['Message'])

# - Exemplo -
msg1 = messages['Message'][3]
#print (msg1)

bow1 = bow_transformer.transform([msg1])
#print(bow1)

#print((bow_transformer.get_feature_names()[9554]))
# --

# --- TF ---
# TF: Contagem de palavras sobre a quantidade total de documentos
# Criando os vetores
messages_bow = bow_transformer.transform(messages)['Message']

# Tamanho da matriz
print (messages_bow.shape)
# Valores que nao sao zero
print(messages_bow.nnz)
# ------

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(messages_bow)

# Verificando uma mensagem no modelo
tfidf1 = tfidf_transformer.transform(bow1)
#print (tfidf_transformer.idf_([bow_transformer.vocabulary_['university']]))

# Evitar usar todos os dados para modelar

from sklearn.naive_bayes import MultinomialNB

msg_tfidf = tfidf_transformer.transform(messages_bow)
spam_detect_model = MultinomialNB().fit(msg_tfidf, messages['Label'])

print ('Predito: ', spam_detect_model.predict(tfidf1)[0])
print ('Esperado: ', messages['Label'][3])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(messages['Message'], messages['Label'], test_size=0.2)

# Treinando com o pipeline
# Permite a criacao do fluxo de trabalho
from sklearn.pipeline import Pipeline

# Parametro: lista com o fluxo de trabalho
pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])
pipeline.fit(X_train, y_train)
pred = pipeline.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(pred, y_test))

plt.show()