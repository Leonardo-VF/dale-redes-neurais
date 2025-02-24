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
        matriz[:, j] = np.random.normal(mu_E, se, N)

    for j in range(Ne, N):
        matriz[:, j] = np.random.normal(mu_I, si, N)

    for i in range(N):
        for j in range(N):
            if random() >= p:
                matriz[i,j] = 0.0

    return matriz


#número de nós da rede
N = 1000

#loop para rodar todos os testes
for i in range(30):
    for mu_E in [x for x in range(1,6)]:
        for Ne in [800]:
            for alpha in [10]:
                for p in [0.5]:
                    #aplica a lei de dale na matriz
                    f = Ne / N
                    se = (1 / (f + (1 - f) * alpha**2))**(1/2)
                    si = alpha * se

                    matriz = dale(N, Ne, mu_E, si, se, p)

                    auto_val = np.linalg.eigvals(matriz)

                    with open(f"dados_p{p}_alpha{alpha}_Ne{Ne}_mu{mu_E}.txt", "a") as arq:
                        for data in auto_val:
                            arq.write("{} {}\n".format(data.real, data.imag))

    print(f"{i}/30")