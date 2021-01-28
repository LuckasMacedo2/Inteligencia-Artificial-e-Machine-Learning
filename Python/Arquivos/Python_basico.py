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

#Acesso a múltiplos valores da lista
# Comando lista[i:j],   Onde i é o ínicio e j é o fim, sem nada em j vai até o fim da lista
lista_multipla = [1, 2, 3, 4, 5]
print lista_multipla[1:4]



## ------------------ Dicionarios -------------------------------------
# Cada elemento do dicionário está realcionado a uma chave
# Estrutura {'chave1': valor1, 'chave2': valor2}, primeir chave, depois o valor,....

print ('Dicionario')
dic = {'valor1': 1, 'valor2': 2}
print dic['valor2']


## ------------------ Tupla -------------------------------------------
# Equivalente a listas, porém as tuplas são constantes, elas não podem ser alteradas
# Estrutura tupla = (valor1, valor2, ..., valorN)
print ('Tupla')
tupla = (1, 2, 3,)
print tupla



## ----------------- List Compehensions -------------------------------
# Definição de uma lista em uma linha
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

## --------------- Funções Lambda --------------------------------------
# Reduzem a quantidade de código
# Não possuem nome, nem return. Só existe em um contexto espefico, escopo

# Função normal
print ('Função Lambda')

def quadrado (x):
    return x*x

# Função lambda

lambda x : x*x

## ----------------------- Map ------------------------------------------
# Map função que atribui todos os valores de um iteravel e passando-os como
# valor de uma função.
# map (função, iteravel)
print ('Map')
# Iteravel
seq = [1, 2, 3, 4, 5]

# Convertendo para uma lista

print (list (map (quadrado, seq)))

# Lambda e Map -> map (lambda x : x*x, seq)

print (list (map (lambda x : x*x, seq)))

## ---------------------- Filer ----------------------------------------
print ('Filter')

# Filtra funções lambda, retornando uma sublista se a condição for satisfeita.
# filter (lambda, itens)

print list (filter (lambda item:item%2 == 0, seq))

## ------------------ Orientação a objeto ------------------------------
print ('Orientação a Objeto')

# Funções dentre uma classe, são métodos

# Retirando o primeiro elemento de uma lista


l = [1, 2, 3]
print l

l.pop(0)

print l


## ----------------- Operador in -----------------------------------------
print ('Operador in')

# Operador de lista, e verifica se o item está na lista

x = 1
print x in [1,2,3]


























