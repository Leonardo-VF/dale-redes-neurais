import matplotlib.pyplot as plt
import os
import numpy as np

def grafico_justos(data):
    ax = plt.gca()
    
    keys = [float(x) for x in data.keys()]
    values = [float(x) for x in data.values()]
            
    ax.plot(keys, values, label=f"alpha={alpha} Ne={ne} mu={mu}")
    plt.xlabel("Raio")
    plt.ylabel('Frequência')
    plt.xticks(np.arange(0, 1.05, 0.05))
    plt.xlim(0, 1)
    ax.set_facecolor('gainsboro')
    plt.title("Número de pontos ao longo do raio")
    plt.tight_layout() 
    plt.legend()
    plt.savefig(f'plots/número de autovalores ao longo do raio')

def graficos(data):
    keys = [float(x) for x in data.keys()]
    values = [float(x) for x in data.values()]
    
    plt.bar(keys, values, width=0.03)
    ax = plt.gca()
    ax.set_facecolor('gainsboro')
    plt.xlabel('Raio do plano complexo')
    plt.ylabel('Frequência')
    plt.xticks(np.arange(0, 2.05, 0.5))
    plt.xlim(0, 2)
    desktop_path = os.path.expanduser("~\Desktop")
    plt.title("Alpha = {} Ne = {} mu = {}".format(alpha, ne, mu))
    plt.savefig(f'plots/plot_alpha{alpha}_Ne{ne}_mu{mu}.png')
    plt.show()
    plt.clf()


def segmentation(lista, n):
    intervalos = np.arange(0, 2, 0.05)
    contagem = {'{:.2f}'.format(intervalos[i+1]): 0 for i in range(len(intervalos)-1)}

    for numero in lista:
        for i in range(len(intervalos)-1):
            if intervalos[i] <= numero < intervalos[i+1]:
                contagem['{:.2f}'.format(intervalos[i+1])] += 1
                break 

    for i in contagem.keys():
        contagem[i] = float(contagem[i])/float(i)
        print(f'{i} = {contagem[i]}')

    return contagem


for alpha in [0.1, 1, 10]:
    for ne in [100, 500, 800]:
        for mu in [3, 5]:
            x = []
            y = []
            radius = []
    
            # Ler os dados do arquivo
            with open("dados/dados_alpha{}_Ne{}_mu{}.txt".format(str(alpha), ne, mu), "r") as arq:
                for line in arq:
                    parts = line.split()
                    x.append(float(parts[0]))
                    y.append(float(parts[1]))
    
            # Calcular as áreas correspondentes aos pontos
            for i in range(len(x)):
                radius.append((x[i]**2 + y[i]**2)**0.5)

            data = segmentation(radius, 500)

            graficos(data)
            #grafico_justos(data)

plt.show()