import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

graph = nx.barabasi_albert_graph(10, 1)

nx.draw(graph, with_labels = True)
plt.show()

print(nx.to_numpy_array(graph))