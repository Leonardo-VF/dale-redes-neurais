import networkx as nx
import numpy as np


def dale(matriz, N, Ne, mu_E, si, se):
    #obter os valores necessários
    f = Ne/N
    mu_I = -(f*mu_E/(1-f))/N**(1/2)
    mu_E = mu_E/N**(1/2)
    se = se/N**(1/2)
    si = si/N**(1/2)

    matriz = np.m

    #sortear valores da distribuição gaussiana
    for j in range(Ne):
        matriz[:, j] = np.random.normal(mu_E, se, N)
    
    for j in range(Ne, N):
        matriz[:, j] = np.random.normal(mu_I, si, N)

#número de nós da rede
N = 3000

#loop para rodar todos os testes
for Ne in [600, 1500, 2400]:
    for mu_E in [3, 5]:  
        #aplica a lei de dale na matriz
        matriz = dale(matriz, N, Ne, mu_E, 1, 1)

        auto_val = np.linalg.eigvals(matriz)

        with open("dados_Ne{}_mu{}.txt".format(str(Ne), mu_E), "w") as arq:
            for data in auto_val:
                arq.write("{} {}\n".format(data.real, data.imag))