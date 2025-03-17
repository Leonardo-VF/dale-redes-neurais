import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import math


def grafico_justos(data):
    #função para criação de um histograma para todos os arquivos utilizados
    ax = plt.gca()

    #separa os raios e o numero de pontos para plotar
    keys = [float(x) for x in data.keys()][1::]
    values = [float(x) for x in data.values()][1::]

    window_length = min(15, len(values) - 1 if len(values) % 2 == 0 else len(values))
    teste = savgol_filter(values, 25, 2)

    ax.plot(keys, teste, label=rf"$\mu_e$ = {mu}")
    plt.scatter(keys[1::5], values[1::5], marker='.')
    plt.xlabel("Raio do plano complexo")
    plt.ylabel('Densidade de probabilidade')
    plt.xticks(np.arange(0, 5.1, 0.5))
    plt.xlim(0, 5.1)
    plt.grid(False)
    ax.set_facecolor('gainsboro')
    plt.title(f"Densidade de probabilidade ao longo do raio com \n "
          fr"Ne={ne} $\alpha$={alpha} $p$={p} $\sigma_E$ = {round(se,2)} $\sigma_I$ = {round(si,2)}")
    plt.tight_layout() 
    plt.legend()
    plt.savefig(f'Variação mu com Ne={ne} e p=1')

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
    plt.savefig(f'plots/hist_alpha{alpha}_Ne{ne}_p0,5.png')
    plt.show()
    plt.clf()



def calcular_aneis(R, N):
    limites = [0.0]
    for i in range(1, N + 1):
        limites.append(R * math.sqrt(i / N))

    return limites

def segmentation(lista, passo):
    #segmenta o raio do plano complexo para fazer a contagem de potnos
    #intervalos = np.arange(0, max(lista)+1, passo)

    intervalos = calcular_aneis(max(lista), 100000)

    contagem = {'{:.2f}'.format(intervalos[i+1]): 0 for i in range(len(intervalos)-1)}

    # Contar os pontos em cada intervalo  
    for num in lista:
        for i in range(1, len(intervalos)):
            if intervalos[i-1] <= num < intervalos[i]:
                contagem['{:.2f}'.format(intervalos[i])] += 1
                break 

    total = sum(contagem.values())
    
    # Calcular a densidade de probabilidade dos pontos por área
    for i in contagem.keys():
        contagem[i] = float(contagem[i])/(total*float(i))
    
    return contagem

for alpha in [10]:
    for ne in [800]:
        for mu in [x for x in range(1,6)]:
            for p in [1]:
                x = []
                y = []
                radius = []

                f = ne / 1000
                se = (1 / (f + (1 - f) * alpha**2))**(1/2)
                si = alpha * se

                # Ler os dados do arquivo
                with open("5. lei de Dale variação alpha e p/dados_p{}_alpha{}_Ne{}_mu{}.txt".format(p,alpha,ne,mu), "r") as arq:
                    for line in arq:
                        parts = line.split()
                        x.append(float(parts[0]))
                        y.append(float(parts[1]))

                # Calcular as áreas correspondentes aos pontos
                for i in range(len(x)):
                    radius.append((x[i]**2 + y[i]**2)**0.5)
                
                data = segmentation(radius, 0.05)

                #graficos(data)
                grafico_justos(data)

#para mostrar os histogramas juntos
plt.show()