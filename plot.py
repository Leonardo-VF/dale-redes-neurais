import matplotlib.pyplot as plt
import numpy as np
import os


for ne in [100, 500, 800]:
    for mu in [3,5]:
        for alpha in [0.1,1,10]:
            x = []
            y = []

            with (open("dados_alpha{}_Ne{}_mu{}.txt".format(alpha,ne,mu))) as arq:
                while True:
                    try:
                        line = arq.readline().split()
                        print(line)
                        x.append(float(line[0]))
                        y.append(float(line[1]))
                    except:
                        break
                    
            theta = np.linspace(0, 2*np.pi, 100)  # Ângulos variando de 0 a 2*pi
            raio = 1  # Raio do círculo
            circulo_complexo = raio * np.exp(1j * theta)  # Pontos do círculo

            plt.figure(figsize=(7, 7))
            plt.scatter(x, y, marker='.')
            plt.plot(circulo_complexo.real, circulo_complexo.imag, color='black', label='Círculo')
            plt.xlabel('Re')
            plt.ylabel('Im')
            plt.title("Alpha = {} Ne = {} mu = {}".format(alpha,ne,mu))
            ax = plt.gca()
            ax.set_facecolor('gainsboro')
            plt.grid(True)
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            desktop_path = os.path.expanduser("~/Desktop")
            file_path = os.path.join(desktop_path, "Ne{}_Mu{}".format(ne, mu))
            plt.xlim(-1.5, 1.5)  # Ajusta os limites do eixo x
            plt.ylim(-1.5, 1.5)
            plt.savefig(f'plot_alpha{alpha}_Ne{ne}_mu{mu}.png')
            plt.show()
            

        