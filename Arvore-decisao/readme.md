## Árvores de decisão

# Português
	Que divisão nas variaveis prediz a variavel alvo 

Nós: Pontos dee divisão
Ramos: saída dos nós
Raiz: Nó que faz a primeora divisão.
Folha: Nó final que toma a decisão.

	O algoritmo faz a divisão sempre na classe que apresentar o maior ganho de informação.

	Suscetiveis a overfitting

	A separação se dá a partir de linhas, "quadrados".
	Não são muito boas, devido ao overfitting.


Florestas aleatorias
	Multiplas arvores de decisão
	Dividir os dados de treino aleatoriamente e crescer várias arvores aleatorias diferentes.
	Todas elas predizem algo, então tira-se a média da precisão e retorna um valor.
	
	Para que todas as arvores escolham parametros raizes distintos é utilizado um algoritmo que escolhe um parametro dentre todo o conjunto de parametros.
	Evitando assim que as árvores geradas fiquem muito correlacionadas.

-> Instalar: Pydot e graphviz, para visualizar as arvores

# English

Which division in the variables predicts the target variable

Us: Split Points
Ramos: exit from the nodes
Root: Knot that makes the first division.
Folha: Final node that makes the decision.

The algorithm always divides the class with the greatest gain in information.

Susceptible to overfitting

The separation occurs from lines, "squares".
They are not very good, due to overfitting.


Random forests
Multiple decision trees
Split training data at random and grow several different random trees.
They all predict something, so the accuracy is averaged and a value is returned.

For all trees to choose different root parameters, an algorithm is used that chooses a parameter from the entire set of parameters.
Thus preventing the trees generated from being too correlated.


-> Install: Pydot and graphviz, to view the trees