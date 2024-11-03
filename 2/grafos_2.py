import networkx as nx
import random

with open("dados.txt", "w") as arq:
    for m in range (2,40):
        #cada for cria um grafo com grau médio diferente até m=39
        m_steps = 0

        for i in range (1000):
            graph = nx.barabasi_albert_graph(100, m)
            nodes = []
            err_aux = []
            err = 0
            steps = 0

            current_node = random.choice(list(nx.neighbors(graph, random.randint(0, graph.number_of_nodes()-1))))

            #faz a varredura da rede e verifica se já foi visitado a metade dos nós
            while len(nodes) != graph.number_of_nodes()/2:
                if current_node not in nodes:
                    nodes.append(current_node)

                current_node = random.choice(list(nx.neighbors(graph, current_node)))
                steps += 1

            #faz a média do número de passos para percorrer a rede e armazena os valores para calcular o desvio padrão
            m_steps += steps
            err_aux.append(steps)

        for i in err_aux:
            err += (i + m_steps/1000)**2

        err = (err/1000)**(1/2)

        arq.write("{} {} {}\n".format(m, m_steps/1000, err))
        
        print(m)