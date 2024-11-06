import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import random


def BA(n, p):
    #cria uma rede de Barabási-Albert
    barabasi = nx.barabasi_albert_graph(n, p)

    #converte para uma rede direcionado
    graph = nx.to_directed(barabasi)
    graph = graph.copy()

    #altera a direção da aresta de forma aleatória
    for u, v in list(graph.edges()):
        if graph.has_edge(u, v) and graph.has_edge(v, u):
            if random() < 0.5:
                graph.remove_edge(u, v)
            else:
                graph.remove_edge(v, u)

    return nx.to_numpy_array(graph)


def ED(n, p):
    #cria uma rede de Erdös-Rényi
    erdos = nx.erdos_renyi_graph(n, p)

    #converte para uma rede direcionado
    graph = nx.to_directed(erdos)
    graph = graph.copy()

    #altera a direção da aresta de forma aleatória
    for u, v in list(graph.edges()):
        if graph.has_edge(u, v) and graph.has_edge(v, u):
            if random() < 0.5:
                graph.remove_edge(u, v)
            else:
                graph.remove_edge(v, u)

    return nx.to_numpy_array(graph)

def dale(matriz, Ne, mu_E, si, se):
    #obter os valores necessários
    N = len(matriz)
    f = Ne/N
    mu_I = -(f*mu_E/(1-f))/N**(1/2)
    mu_E = mu_E/N**(1/2)
    se = se/N**(1/2)
    si = si/N**(1/2)

    #atribui um valor de uma distribuição gaussiana para um elemento não nulo da matriz
    for i in range(N):
        for j in range(Ne):
            if matriz[i,j] != 0:
                matriz[i,j] = np.random.normal(mu_E, se)

    #atribui um valor de uma distribuição gaussiana para um elemento não nulo da matriz
    for i in range(N):
        for j in range(Ne, N):
            if matriz[i,j] != 0:
                matriz[i,j] = np.random.normal(mu_I, si)

    return matriz

def main():
    #número de nós da rede
    N = 1000

    #loop para rodar todos os testes
    for i in range(30):
        for mu_E in [5]:
            for Ne in [800]:
                for alpha in [10]:
                    for p in [x/10 for x in range(2,11,2)]:
                        #parâmetros inicias para aplicação da lei de dale
                        f = Ne / N
                        se = (1 / (f + (1 - f) * alpha**2))**(1/2)
                        si = alpha * se
                        
                        #escolha de qual tipo de rede será criada
                        #matriz = BA(N, p)
                        matriz = ED(N, p)

                        #aplica a lei de dale na matriz
                        dale_matriz = dale(matriz, Ne, mu_E, si, se)

                        #extrai os autovalores da matriz gerada a partir da lei de dale
                        auto_val = np.linalg.eigvals(dale_matriz)

                        with open(f"dados/dados_p{p}_alpha{alpha}_Ne{Ne}_mu{mu_E}.txt", "a") as arq:
                            for data in auto_val:
                                arq.write("{} {}\n".format(data.real, data.imag))

        print(f"{i}/30")

if __name__ == "__main__":
    main()