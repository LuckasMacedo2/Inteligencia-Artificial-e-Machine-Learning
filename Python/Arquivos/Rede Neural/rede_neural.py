import numpy as np


class rede (object):
    # tamanho = lista com a quantidade neuronios em cada camada
    # bias = permite aumentar o grau de liberdade dos ajustes dos pesos
    def __init__(self, tamanho):
        self.num_camadas = len(tamanho)
        self.tamanho = tamanho

        # inicializando bias e pesos aleatoriamente
        self.bias = [np.random.randn(y, 1) for y in tamanho[1:]] # utilizadas para calcular saidas de camadas posteriores
        self.pesos = [np.random.randn(y, x) for x, y in zip( tamanho[:-1], tamanho[1:])]

        # randn gera distribuicoes normais com media = 0 e desvio padrao = 1

    # funcao zip returna tuplas, ou seja combina os elementos de dois vetores em tuplas onde
    # os indices sao iguais
    # mais em: https://pythonhelp.wordpress.com/2013/04/16/funcao-zip-em-python/

    # Funcao de ativacao
    def sigmoide(z):
        return 1.0/(1.0 + np.exp(-z))


    # a e o vetor de ativacao da segunda camada, w o peso, b a bias
    def alimentacao_frente (self, a):
        for b, w in zip (self.bias, self.pesos):
            a = self.sigmoide(np.dot(w, a) + b)
        return a


    # dados_treino lista de tuplas com as entradas de treinamento e as saidas desejadas
    # epochs = epoca, numero de epocas para treinar
    # mini_batch_size tamanho dos mini lotes a serem utilizados durante a amostragem
    # eta = taxa de aprendizagem
    # dados_teste e opcional, existe a avaliacao e a cada periodo de avaliacao existe a saida do progresso

    def SGD(self, dados_treino, epochs, mini_batch_size, eta, dados_teste = None):
        dados_treino = list(dados_treino)
        n = len(dados_treino)

        if dados_teste:
            dados_teste = list (dados_teste)
            n_teste = len(dados_teste)

        for j in range(epochs):
            np.random.shuffle(dados_treino)
            mini_batches = [dados_treino[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)

            if dados_teste:
                print ("Epoch {} : {} / {}".format(j, self.evaluate(dados_teste), n_teste))
            else:
                print ("Epoch {} finalizada".format(j))


    # Metodo que busca atualizar os pesos e os bias de acordo com uma unica iteracao de descida, usando
    # os dados de treinamento
    # Calcula os gradientes da funcao de custo e entao atualiza os pesos e a bias
    def update_mini_batch (self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.pesos]


        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.alimentacao_tras(x, y)
            nabla_b = [nb + dnb for nb , dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw , dnw in zip(nabla_w, delta_nabla_w)]

            self.pesos = [w - (eta/len(mini_batch)) * nw for w, nw in zip (self.pesos, nabla_w)]
            self.bias = [b - (eta/len(mini_batch)) * nb for b, nb in zip (self.bias, nabla_b)]


    # Algoritmo backpropagation, calcula o gradiente da funcao de custo
    # Retorna o gradiente apropriado para o custo associado ao exemplo de treinamento x.

    def alimentacao_tras(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.bias]
        nabla_w = [np.zeros(w.shape) for w in self.pesos]

        # Alimentacao para frente
        ativacao = x

        # Armazena as ativacoes, camada por camada
        ativacoes = [x]

        # Armazena todos os vetores z, camada por camada
        zs = []

        for b, w in zip(self.bias, self.pesos):
            z = np.dot(w, ativacao) + b
            zs.append(z)
            ativacao = self.sigmoide(z)
            ativacoes.append(ativacao)

        # Passo para tras
        delta = self.cost_derivative(ativacoes[-1], y) * sigmoide_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, )


rede1 = rede([2, 3, 1])



