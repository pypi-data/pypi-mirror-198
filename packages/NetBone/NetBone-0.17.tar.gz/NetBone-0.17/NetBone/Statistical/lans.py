import networkx as nx
from NetBone.Backbone import Backbone

def lans(G :nx.Graph)-> nx.Graph :
    for u, v, w in G.edges(data='weight'):
        G[u][v]['p_value'] = min(compute_pvalue(G, v, w), compute_pvalue(G, u, w))
    return Backbone(G, name="Locally Adaptive Network Sparsification Filter", column="p_value", ascending=True)

def compute_pvalue(G, node, w):
    u_degree = G.degree(node, weight='weight')
    puv = w/u_degree
    u_n = G[node]
    count = len([n for n in u_n if u_n[n]['weight']/u_degree <= puv])
    return  1-count/len(u_n)