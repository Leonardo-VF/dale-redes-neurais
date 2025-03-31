import numpy as np
import Sparse_Matrix
from tqdm import tqdm


def dale(matriz, Ne, muE, sigmaI, sigmaE):
    #obter os valores necessários
    N = len(matriz)
    f = Ne/N
    muI = -(f*muE/(1-f))/N**(1/2)
    muE = muE/N**(1/2)
    sigmaE = sigmaE/N**(1/2)
    sigmaI = sigmaI/N**(1/2)

    #sortear valores da distribuição gaussiana
    for i in range(N):
        for j in range(Ne):
            if matriz[i,j] != 0:
                matriz[:, j] = np.random.normal(muE, sigmaE, N)

    for i in range(N):
        for j in range(Ne, N):
            if matriz[i,j] != 0:
                matriz[:, j] = np.random.normal(muI, sigmaI, N)

    return matriz

def main():
    #número de nós da rede
    N = 1000

    #loop para rodar todos os testes
    for _ in tqdm(range(30)):
        for muE in [1,3,5,7]:
            for Ne in [100,500,800]:
                for alpha in [0.1,1,10]:
                    for gamma in [2.5,3]:
                        k0 = 2
                    
                        #aplica a lei de dale na matriz
                        f = Ne / N
                        sigmaE = (1 / (f + (1 - f) * alpha**2))**(1/2)
                        sigmaI = alpha * sigmaE
                        muI = -(f*muE/(1-f))/N**(1/2)

                        #dale_matriz = dale(matriz, Ne, muE, sigmaI, sigmaE)
                        matriz = Sparse_Matrix.generate_heterogeneous(N, gamma, k0, Ne, muE, sigmaE, muI, sigmaI, outdegree=True)

                        auto_val = np.linalg.eigvals(matriz)

                        with open(f"6. verificação da topologia da rede/dados/dados_gamma{gamma}_alpha{alpha}_Ne{Ne}_mu{muE}.txt", "a") as arq:
                            for data in auto_val:
                                arq.write("{} {}\n".format(data.real, data.imag))


if __name__ == "__main__":
    main()