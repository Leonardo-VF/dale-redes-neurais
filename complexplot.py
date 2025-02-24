import matplotlib.pyplot as plt
import numpy as np
import os


for ne in [800]:
    for mu in [3]:
        for alpha in [10]:
            for p in [x/10 for x in range(1,11)]:
                x = []
                y = []

                with (open("5. lei de Dale variação alpha e p/dados_p{}_alpha{}_Ne{}_mu{}.txt".format(p,alpha,ne,mu))) as arq:
                    for line in arq:
                        parts = line.split()
                        x.append(float(parts[0]))
                        y.append(float(parts[1]))

                theta = np.linspace(0, 2*np.pi, 100)  # Ângulos variando de 0 a 2*pi
                raio = 1  # Raio do círculo
                circulo_complexo = raio * np.exp(1j * theta)  # Pontos do círculo

                plt.figure(figsize=(7, 7))
                plt.scatter(x, y, marker='.')
                plt.plot(circulo_complexo.real, circulo_complexo.imag, color='black', label='Círculo')
                plt.xlabel('Re')
                plt.ylabel('Im')
                plt.title("Ne = {} Mu = {} Alpha = {}".format(ne,mu,alpha))
                ax = plt.gca()
                ax.set_facecolor('gainsboro')
                plt.grid(True)
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                desktop_path = os.path.expanduser("~/Desktop")
                file_path = os.path.join(desktop_path, "Ne{}_Mu{}_alpha{}".format(ne, mu, alpha))
                #plt.xlim(-1.5, 1.5)  # Ajusta os limites do eixo x
                #plt.ylim(-1.5, 1.5)
                plt.savefig(f'plot_Ne{ne}_mu{mu}_alpha{alpha}.png')
                plt.show()
            

        