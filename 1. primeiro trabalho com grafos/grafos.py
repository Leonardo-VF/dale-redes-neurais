import networkx as nx
import matplotlib.pyplot as plt
import random

passos = 0
with open("dados.txt", "w") as arq:
    for i in range (10000):
        graph = nx.barabasi_albert_graph(100,1)
        nodes = []
        steps = 0

        current_node = random.choice(list(nx.neighbors(graph, random.randint(0, graph.number_of_nodes()-1))))

        while len(nodes) != graph.number_of_nodes()/2:
            if current_node not in nodes:
                nodes.append(current_node)

            current_node = random.choice(list(nx.neighbors(graph, current_node)))
            steps += 1

        passos += steps
        arq.write("{}\n".format(steps))

print(passos)
nx.draw(graph, with_labels = True)
plt.show()