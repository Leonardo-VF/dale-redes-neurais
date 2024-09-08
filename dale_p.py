import numpy as np
from random import random


def dale(N, Ne, mu_E, si, se, p):
    #obter os valores necessários
    f = Ne/N
    mu_I = -(f*mu_E/(1-f))/N**(1/2)
    mu_E = mu_E/N**(1/2)
    se = se/N**(1/2)
    si = si/N**(1/2)

    matriz = np.zeros((N,N))

    #sortear valores da distribuição gaussiana
    
    for j in range(Ne):
        if random() <= p:
            matriz[:, j] = np.random.normal(mu_E, se, N)

    for j in range(Ne, N):
        if random() <= p:
            matriz[:, j] = np.random.normal(mu_I, si, N)

    return matriz


#número de nós da rede
N = 1000

#probabilidade p (0:1)
p = 0.7

for i in range(30):
    #loop para rodar todos os testes
    for Ne in [100, 500, 800]:
        for mu_E in [3, 5]:
            for alpha in [0.1, 1, 10]:
                #aplica a lei de dale na matriz
                f = Ne / N
                se = (1 / (f + (1 - f) * alpha**2))**(1/2)
                si = alpha * se

                matriz = dale(N, Ne, mu_E, si, se, p)

                auto_val = np.linalg.eigvals(matriz)

                with open("dados/dados_alpha{}_Ne{}_mu{}.txt".format(alpha, str(Ne), mu_E), "a") as arq:
                    for data in auto_val:
                        arq.write("{} {}\n".format(data.real, data.imag))
    
    print(i)