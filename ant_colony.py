import matplotlib.pyplot as plt
import networkx as nx
import pants
import data
import time


# instalar https://pypi.org/project/ACO-Pants/

# Valores padrão utilizados na configuracao do algoritmo
# relative importance placed on pheromones; default=1
# relative importance placed on distances; default=3
# number of iterations to perform; default=100
# ratio of evaporated pheromone (0 <= P <= 1); default=0.8
# ratio of elite ant's pheromone; default=0.5
# total pheromone capacity of each ant (Q > 0); default=1
# initial amount of pheromone on every edge (T > 0); default=0.01
# number of ants used in each iteration (N > 0); default=10
# specify a particular set of demo data; default=33

tempos = list()
arestas = list()


# metodo que calcula a distancia entre os elementos comparados
def distancia(a, b):
    if (a[0] == b[0]):
        distancia = nx.shortest_path_length(G, a[0], a[1], weight='length') + nx.shortest_path_length(G, a[1], a[0], weight='length')
        return distancia
    else:
        return nx.shortest_path_length(G, a[0], b[0], weight='length')


inicio = time.time()


# criando um grafo direcionado
G = nx.DiGraph()

# pegando as arestas do dataset
edges = data.nova_luz2

for start, end, length in edges:
    # adicionando as arestas no grafo
    G.add_edge(start, end, length=length)

# pegando uma lista de arestas do grafo
edges = list(G.edges)

# criando o "mundo" onde serao adicionadas as formigas e solucionando o problema
world = pants.World(edges, distancia)
solver = pants.Solver()
solution = solver.solve(world)

# ali na solucao ja temos a sequencia de arestas agora vamos ver exatamente os vertices que serao visitados
caminho = list()
for edge in solution.path:
    short = nx.shortest_path(G, edge.start[0], edge.end[0], weight='length')
    for i in short:
        if len(caminho) == 0:
            caminho.append(str(i))
        else:
            if caminho[-1] != str(i):
                caminho.append(str(i))

print(f'Caminho: {" -> ".join(caminho)}')
print(f'{solution.distance}')

tempos.append(time.time() - inicio)
arestas.append(len(edges))

#SEGUNDO GRAFO
# criando um grafo direcionado
G2 = nx.DiGraph()

# pegando as arestas do dataset
edges2 = data.nova_luz

for start, end, length in edges2:
    # adicionando as arestas no grafo
    G.add_edge(start, end, length=length)

# pegando uma lista de arestas do grafo
edges2 = list(G.edges)

# criando o "mundo" onde serao adicionadas as formigas e solucionando o problema
world = pants.World(edges2, distancia)
solver = pants.Solver()
solution = solver.solve(world)

# ali na solucao ja temos a sequencia de arestas agora vamos ver exatamente os vertices que serao visitados
caminho2 = list()
for edge in solution.path:
    short = nx.shortest_path(G, edge.start[0], edge.end[0], weight='length')
    for i in short:
        if len(caminho2) == 0:
            caminho2.append(str(i))
        else:
            if caminho2[-1] != str(i):
                caminho2.append(str(i))

print(f'Caminho: {" -> ".join(caminho2)}')
print(f'{solution.distance}')

tempos.append(time.time() - inicio)
arestas.append(len(edges2))

plt.xlabel('Número de Arestas')
plt.ylabel('Tempo')
# plt.plot(elements, times, label='Força Bruta')
plt.plot(arestas, tempos, label='Tempo em x número de Arestas - Colônia de Formigas')
plt.grid()
plt.legend()
plt.show()