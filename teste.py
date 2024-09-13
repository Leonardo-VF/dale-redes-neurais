import matplotlib.pyplot as plt
import numpy as np


def grafico_justos(data):
    ax = plt.gca()
    
    keys = [float(x) for x in data.keys()]
    values = [float(x) for x in data.values()]
            
    ax.plot(keys, values, label=f" p = {p} mu={mu}")
    plt.xlabel("Raio do plano complexo")
    plt.ylabel('Densidade de probabilidade $(\\frac{pontos_{local}}{pontos_{totais}*raio})$')
    plt.xticks(np.arange(0, 3.1, 0.2))
    plt.xlim(0, 3)
    ax.set_facecolor('gainsboro')
    plt.title(f"Densidade de probabilidade ao longo do raio \n alpha = {alpha} ne = {ne} \n (autovalores 0.0 descartados para facilitar a vizualização)")
    plt.tight_layout() 
    plt.legend()
    plt.savefig(f'plots/Variação de p com mu = 5')

def graficos(data):
    keys = [float(x) for x in data.keys()]
    values = [float(x) for x in data.values()]
    
    plt.bar(keys, values, width=0.01)
    ax = plt.gca()
    ax.set_facecolor('gainsboro')
    plt.xlabel('Raio do plano complexo')
    plt.ylabel('Densidade de pontos (n pontos/área)')
    plt.xticks(np.arange(0, 2.05, 0.5))
    plt.xlim(0, 2)
    plt.title("Alpha = {} Ne = {} mu = {}".format(alpha, ne, mu))
    plt.savefig(f'plots/hist_alpha{alpha}_Ne{ne}_mu{mu}.png')
    plt.show()
    plt.clf()


def segmentation(lista, passo):
    intervalos = np.arange(0, 5, passo)
    contagem = {'{:.2f}'.format(intervalos[i+1]): 0 for i in range(len(intervalos)-1)}

    for num in lista:
        for i in range(len(intervalos)-1):
            if intervalos[i] <= num < intervalos[i+1]:
                contagem['{:.2f}'.format(intervalos[i+1])] += 1
                break 
    
    total = sum(contagem.values())

    for i in contagem.keys():
        contagem[i] = float(contagem[i])/(total*float(i))

    
    return contagem


for alpha in [1]:
    for ne in [500]:
        for mu in [5]:
            for p in [x/10 for x in range(1,11)]:
                x = []
                y = []
                radius = []

                # Ler os dados do arquivo
                with open("dados/dados_p{}_alpha{}_Ne{}_mu{}.txt".format(p, alpha, ne, mu), "r") as arq:
                    for line in arq:
                        parts = line.split()
                        x.append(float(parts[0]))
                        y.append(float(parts[1]))

                # Calcular as áreas correspondentes aos pontos
                for i in range(len(x)):
                    if x[i] != 0.0 and y[i] != 0.0:
                        radius.append((x[i]**2 + y[i]**2)**0.5)

                data = segmentation(radius, 0.05)

                #graficos(data)
                grafico_justos(data)

plt.show()