import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter



def grafico_justos(data):
    #função para criação de um histograma para todos os arquivos utilizados
    ax = plt.gca()
    
    #separa os raios e o numero de pontos para plotar
    keys = [float(x) for x in data.keys()]
    values = [float(x) for x in data.values()]

    teste = savgol_filter(values, 10, 3)
    print(int(-len(keys)/2))
    ax.plot(keys, teste, label=rf"p = {p}")
    plt.scatter(keys[0:int(-len(keys)/4)], values[0:int(-len(keys)/4)], marker='x')
    plt.xlabel("Raio do plano complexo")
    plt.ylabel('Densidade de probabilidade')
    plt.xticks(np.arange(0, 2, 0.2))
    plt.xlim(0, 2)
    plt.grid(True)
    ax.set_facecolor('gainsboro')
    plt.title(f"Densidade de probabilidade ao longo do raio com \n a={alpha} Ne={ne} mu={mu} \n (autovalores 0.0 descartados para facilitar a vizualização)")
    plt.tight_layout() 
    plt.legend()
    plt.savefig(f'Variação alpha com Ne={ne} e Mu={mu}')

def graficos(data):
    #função para criação de gráficos individuais das probabilidades
    keys = [float(x) for x in data.keys()]
    values = [float(x) for x in data.values()]
    
    plt.bar(keys, values, width=0.1)
    ax = plt.gca()
    ax.set_facecolor('gainsboro')
    plt.xlabel('Raio do plano complexo')
    plt.ylabel('Densidade de pontos (n pontos/área)')
    plt.xticks(np.arange(0, max(keys), 0.5))
    plt.xlim(0, max(keys))
    plt.title("Alpha = {} Ne = {} mu = {}".format(alpha, ne, mu))
    plt.savefig(f'plots/hist_alpha{alpha}_Ne{ne}_mu{mu}.png')
    plt.show()
    plt.clf()


def segmentation(matrix, passo):
    #segmenta o raio do plano complexo para fazer a contagem de potnos
    intervalos = np.arange(min(matrix), max(matrix)+1, passo)
    contagem = {'{:.2f}'.format(intervalos[i+1]): 0 for i in range(len(intervalos)-1)}

    # Contar os pontos em cada intervalo  
    for num in matrix:
        for i in range(len(intervalos)-1):
            if intervalos[i] <= num < intervalos[i+1]:
                contagem['{:.2f}'.format(intervalos[i+1])] += 1
                break 

    total = sum(contagem.values())
    
    # Calcular a densidade de probabilidade dos pontos por área
    for i in contagem.keys():
        contagem[i] = float(contagem[i])/(total*float(i))

    
    return contagem


def segmentation(matrix, passo):
    #segmenta o raio do plano complexo para fazer a contagem de potnos
    intervalos = np.arange(0, max(matrix)+1, passo)
    contagem = {'{:.2f}'.format(intervalos[i+1]): 0 for i in range(len(intervalos)-1)}

    # Contar os pontos em cada intervalo  
    for num in matrix:
        for i in range(len(intervalos)-1):
            if intervalos[i] <= num < intervalos[i+1]:
                contagem['{:.2f}'.format(intervalos[i+1])] += 1
                break 

    total = sum(contagem.values())
    
    # Calcular a densidade de probabilidade dos pontos por área
    for i in contagem.keys():
        contagem[i] = float(contagem[i])/(total*float(i))



for alpha in [10]:
    for ne in [800]:
        for mu in [3]:
            for p in [x/10 for x in range(1,11)]:
                x = []
                y = []
                radius = []

                # Ler os dados do arquivo
                with open("5. lei de Dale variação alpha e p/dados_p{}_alpha{}_Ne{}_mu{}.txt".format(p,alpha,ne,mu), "r") as arq:
                    for line in arq:
                        parts = line.split()
                        x.append(float(parts[0]))
                        y.append(float(parts[1]))

                # Calcular as áreas correspondentes aos pontos
                for i in range(len(x)):
                    if (x[i]**2 + y[i]**2)**0.5 != 0:
                        radius.append((x[i]**2 + y[i]**2)**0.5)

                data = segmentation(radius, 0.005)

                #graficos(data)
                grafico_justos(data)

#para mostrar os histogramas juntos
plt.show()