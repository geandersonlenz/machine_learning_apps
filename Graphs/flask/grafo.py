import networkx as nx
import pandas as pd

df = pd.read_csv('products.csv')

# data = df.sample(n=1000)
sample = df.sample(n=50)


source = 'Top1'
target = 'Quantidade'

grafo = nx.from_pandas_edgelist(sample, source=source, target=target, edge_attr=True,)
nodes = grafo.nodes()
edges = grafo.edges()
density = nx.density(grafo)
adc = nx.average_degree_connectivity(grafo)


print(nodes)
print(edges)
print(density)
print(adc)



class Calculus(object):

    def __init__(self):
        self.graph = nx.from_pandas_edgelist(sample, source=source, target=target, edge_attr=True,)
        #self.weight = weight
        #self.origin = origin
        #self.target = target

    def graphs():
        return graph

    def node():
        nodes = graph.nodes()
        return nodes

    def edge():
        edges = graph.edges()
        return edges

    def density():
        """
        Average edge density of the Graphs
        """
        density = nx.density(graph)
        return density

    def average_degree_connectivity(graph):
        """
        For a node of degree k - What is the average of its neighbours' degree?
        """
        adc = nx.average_degree_connectivity(graph)
        return adc

    def shortest(graph):
        """
        Average shortest path length for ALL paths in the Graph
        """
        aspl = nx.average_shortest_path_length(graph)
        return aspl

    def dijkstra(graph, source, target):
        """
        Let us find the dijkstra path from source to target.
        """
        dijkstra = nx.dijkstra_path(graph, source=source, target=target)
        return dijkstra

    def dijkstra_weight(graph, source, target, weight):
        """
        Let us try to find the dijkstra path weighted by variable(approximate case)
        """
        dijkstra_weight = nx.dijkstra_path(graph, source=source, target=target, weight=weight)
        return dijkstra_weight

    def clustering(graph):
        """
        create clustering for each graph
        """
        clustering = nx.clustering(graph)
        return clustering

    def chains():
        """
        """
        chains = nx.algorithms.chain_decomposition(graph)
        return chains


#grafo = Calculus()
#print(grafo.node())