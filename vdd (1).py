import numpy as np
import matplotlib.pyplot as plt


def aneis(n):
    raios_quad = np.linspace(0, 1, n + 1)
    aneis = []

    for i in range(1, len(raios_quad)):
        r_interno = np.sqrt(raios_quad[i - 1])
        r_externo = np.sqrt(raios_quad[i])
        aneis.append((r_interno, r_externo))

    return aneis

plt.figure(figsize=(10, 7))

def grafico(contagem, aneis):
    raios_externos = [r_externo for _, r_externo in aneis]
    ax = plt.subplot(111)
    
    # Plotando os dados
    ax.plot(raios_externos, contagem, label=f"alpha={alpha} Ne={ne} mu={mu}")
    
    # Definindo os rótulos dos eixos
    plt.xlabel("Raio")
    plt.ylabel("Número de Pontos")
    
    # Definindo a gradação do eixo X de 0.05 em 0.05
    plt.xticks(np.arange(0, 1.05, 0.05))  # De 0 até 1, com passos de 0.05
    
    # Outras personalizações
    ax.set_facecolor('gainsboro')
    plt.title("Número de pontos ao longo do raio")
    plt.legend()
    plt.tight_layout() 
    
    # Salvando o gráfico
    plt.savefig(f'plots/Variação ne alpha = ')


def contador_pontos(x_coords, y_coords, aneis):
    contagem = [0] * len(aneis)

    for x, y in zip(x_coords, y_coords):
        raio_ponto = np.sqrt(x**2 + y**2)

        for i, (r_interno, r_externo) in enumerate(aneis):
            if r_interno <= raio_ponto <= r_externo:
                contagem[i] += 1
                break

    return contagem


n = 100

aneis = aneis(n)

for alpha in [1]:
    for ne in [500]:
        for mu in [x for x in range(10)]:
            for p in [0.5]:
                x = []
                y = []
                areas = []

                # Carregando os dados do arquivo
                with open(f"dados/dados_p{p}_alpha{alpha}_Ne{ne}_mu{mu}.txt", "r") as arq:
                    for line in arq:
                        parts = line.split()
                        if float(parts[0])!= 0.0 and float(parts[1]) != 0.0:
                            x.append(float(parts[0]!= 0))
                            y.append(float(parts[1]))

                # Contando os pontos
                contagem = contador_pontos(x, y, aneis)

                # Gerando o gráfico
                grafico(contagem, aneis)

plt.show()
