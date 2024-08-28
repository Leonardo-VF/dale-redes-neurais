import matplotlib.pyplot as plt
from math import pi as pi
import os

for alpha  in [0.1, 1, 10]:
    for ne in [100, 500, 800]:
        for mu in [3,5]:
            x = []
            y = []
            areas = []
    
            # Ler os dados do arquivo
            with open("dados_alpha{}_Ne{}_mu{}.txt".format(str(alpha),ne,mu), "r") as arq:
                for line in arq:
                    # Dividir a linha em partes separadas por espaços
                    parts = line.split()
                    # Extrair as coordenadas x e y dos dados
                    x.append(float(parts[0]))
                    y.append(float(parts[1]))
    
            # Calcular as áreas correspondentes aos pontos
            for i in range(len(x)):
                radius = (x[i]**2 + y[i]**2)**0.5
                area = radius**2 * pi
                areas.append(area)

            # Criar o histograma com base nas áreas calculadas
            plt.hist(areas, bins=60, edgecolor='black')
    
            # Adicionar títulos e rótulos aos eixos
            plt.xlabel('Área do plano complexo')
            plt.ylabel('Frequência')
    
            # Exibir o histograma
            desktop_path = os.path.expanduser("~\Desktop")
            file_path = os.path.join(desktop_path, "hist_alpha{}_Ne{}_Mu{}".format(str(alpha), str(ne), mu))
            plt.title("Alpha = {} Ne = {} mu = {}".format(alpha,ne,mu))
            plt.savefig(f'plot_alpha{alpha}_Ne{ne}_mu{mu}.png')
            plt.show()
            plt.clf()

