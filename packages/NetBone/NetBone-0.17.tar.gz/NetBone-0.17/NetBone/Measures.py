import igraph as ig
import networkx as nx
import numpy as np
from NetBone.Utils.utils import lcc

def node_fraction(network, b):
    return len(b)/len(network)

def edge_fraction(network, b):
    return len(b.edges())/len(network.edges())

def weight_fraction(network, b):
    return sum(weights(b))/sum(weights(network))

def reachability(G):
    r = 0
    for c in [len(component) for component in nx.connected_components(G)]:
        r += c*(c-1)
    return r/(len(G)*(len(G) - 1))

def lcc_size(G):
    return len(lcc(G))

def number_connected_components(G):
    nx.number_connected_components(G)

def diameter(G):
    return ig.Graph.from_networkx(lcc(G)).diameter(directed=False, unconn=True)

def lcc_node_fraction(G):
    return node_fraction(G, lcc(G))

def lcc_edge_fraction(G):
    return edge_fraction(G, lcc(G))

def lcc_weight_fraction(G):
    return weight_fraction(G, lcc(G))

def weights(G):
    return list(nx.get_edge_attributes(G, 'weight').values())

def degrees(G):
    return list(dict(G.degree()).values())

def average_clustering_coefficient(G):
    node_clustering = ig.Graph.from_networkx(G).transitivity_local_undirected(mode="nan")
    return np.mean([x for x in node_clustering if isinstance(x, float) and not np.isnan(x)])










