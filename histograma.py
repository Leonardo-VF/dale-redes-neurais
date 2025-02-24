import matplotlib.pyplot as plt

data = []

with open("1. primeiro trabalho com grafos/dados.txt") as arq:
    for lines in arq:
        data.append(int(lines))

plt.hist(data, bins=100)
plt.show()