print ('String')

print (type (1)) #Retorna o tipo

#Formatando uma String
print ('{one} e {two}'.format(one = 1, two = 2))

# i**2 == i ^ 2
#elif == else if


## ------------------ Listas--------------------------------------------
print ('Lista')
#Lista
[1, 2, 3]

#Lsita de Listas
lista = [[1, 2, 3], [1, 2, 3]]
print lista

#Acessando um elemento da lista de lista
print lista[1][1] #Acessa o elemento ij da lista

#Acesso a m�ltiplos valores da lista
# Comando lista[i:j],   Onde i � o �nicio e j � o fim, sem nada em j vai at� o fim da lista
lista_multipla = [1, 2, 3, 4, 5]
print lista_multipla[1:4]



## ------------------ Dicionarios -------------------------------------
# Cada elemento do dicion�rio est� realcionado a uma chave
# Estrutura {'chave1': valor1, 'chave2': valor2}, primeir chave, depois o valor,....

print ('Dicionario')
dic = {'valor1': 1, 'valor2': 2}
print dic['valor2']


## ------------------ Tupla -------------------------------------------
# Equivalente a listas, por�m as tuplas s�o constantes, elas n�o podem ser alteradas
# Estrutura tupla = (valor1, valor2, ..., valorN)
print ('Tupla')
tupla = (1, 2, 3,)
print tupla



## ----------------- List Compehensions -------------------------------
# Defini��o de uma lista em uma linha
print ('List Compehensions')
# Jeito normal
out = []
x = [1, 2, 3, 4]
for item in x:
    out.append(item**2)
print out

# Outro jeito
l = [item ** 2 for item in x]
print l

## --------------- Fun��es Lambda --------------------------------------
# Reduzem a quantidade de c�digo
# N�o possuem nome, nem return. S� existe em um contexto espefico, escopo

# Fun��o normal
print ('Fun��o Lambda')

def quadrado (x):
    return x*x

# Fun��o lambda

lambda x : x*x

## ----------------------- Map ------------------------------------------
# Map fun��o que atribui todos os valores de um iteravel e passando-os como
# valor de uma fun��o.
# map (fun��o, iteravel)
print ('Map')
# Iteravel
seq = [1, 2, 3, 4, 5]

# Convertendo para uma lista

print (list (map (quadrado, seq)))

# Lambda e Map -> map (lambda x : x*x, seq)

print (list (map (lambda x : x*x, seq)))

## ---------------------- Filer ----------------------------------------
print ('Filter')

# Filtra fun��es lambda, retornando uma sublista se a condi��o for satisfeita.
# filter (lambda, itens)

print list (filter (lambda item:item%2 == 0, seq))

## ------------------ Orienta��o a objeto ------------------------------
print ('Orienta��o a Objeto')

# Fun��es dentre uma classe, s�o m�todos

# Retirando o primeiro elemento de uma lista


l = [1, 2, 3]
print l

l.pop(0)

print l


## ----------------- Operador in -----------------------------------------
print ('Operador in')

# Operador de lista, e verifica se o item est� na lista

x = 1
print x in [1,2,3]


























