import matplotlib.pyplot as plt
import networkx as nx
import pants
import data

# instalar https://pypi.org/project/ACO-Pants/

# criando um grafo direcionado
G = nx.DiGraph()

# pegando as arestas do dataset
edges = data.nova_luz

for start, end, length in edges:
    # adicionando as arestas no grafo
    G.add_edge(start, end, length=length)

# metodo que calcula a distancia entre os elementos comparados
def distancia(a, b):
    if (a[0] == b[0]):
        distancia = nx.shortest_path_length(G, a[0], a[1], weight='length') + nx.shortest_path_length(G, a[1], a[0], weight='length')
        return distancia
    else:
        return nx.shortest_path_length(G, a[0], b[0], weight='length')

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