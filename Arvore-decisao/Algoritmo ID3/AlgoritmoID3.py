#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from math import log2
from operator import itemgetter


# In[2]:


df = pd.read_csv('campus_party.csv')


# In[3]:


def entropia(p0, p1):
    if p0 == 0 or p1 == 0: # Todos os exemplos positivos ou negativos
        return 0
    if p0 == p1: # Quantidade de exemplos positivos igual a quantidade de exemplos negativos
        return 1
    return (-(p1 * log2(p1)) - (p0 * log2(p0)))


# In[4]:


df.head()


# In[5]:


def ID3(df, label):
    
    sucesso = df[label]
    df1 = df.drop(label, axis = 1)
    
    dict_ganhos = {} 
    
    
    for coluna in df1.columns: # Percorre as colunas do DataFrame
        dict_atributos = {} # O dicionario e formado por:
                            # 'chave (valor da coluna)':[exemplos negativos, exemplos positivos]
        for i in range (0, len(df1[coluna])): # Percore cada valor da coluna
            valor = df1[coluna][i]
            
            # Verifica os possiveis valores e soma-os como exemplos positivos ou negativos
            if not valor in dict_atributos:
                # Adiciona a chave no dicionario
                dict_atributos[valor] = [0, 0]
            
            # Soma os exemplos positivos
            if sucesso[i] == 'SIM':
                dict_atributos[valor][1] += 1
            # Soma os exemplos negativos
            else:
                dict_atributos[valor][0] += 1
        
        
        #print (coluna)
        #print(dict_atributos)
        
        ganho = 0
        aux = 0
        
        for key in dict_atributos.keys():
            total_exemplos = dict_atributos[key][1] + dict_atributos[key][0] 
            exemplos_positivos = dict_atributos[key][1] / total_exemplos
            exemplos_negativos = dict_atributos[key][0] / total_exemplos
            porcentagem  = ((total_exemplos)/len(df1[coluna]))
            ganho +=  porcentagem * entropia(exemplos_positivos, exemplos_negativos)
            #aux =   entropia(exemplos_positivos, exemplos_negativos)
            #print(dict_atributos[key] + ' : ' + str(aux))
            #print(f'{dict_atributos[key]} -> {aux}: {total_exemplos}')
        
        dict_ganhos[coluna] = 1 - ganho
        
    return dict_ganhos
        
            
        


# In[6]:


v = ID3(df, "Let's go party")


# In[7]:


s = sorted(v.items(), key = itemgetter(1), reverse = True)


# In[8]:


print(s)

