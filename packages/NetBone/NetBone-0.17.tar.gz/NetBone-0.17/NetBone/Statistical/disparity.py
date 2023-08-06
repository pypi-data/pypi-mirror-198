

import networkx as nx
import numpy as np
from scipy import integrate
from NetBone.Backbone import Backbone


# algo: disparity_filter.py
def disparity(G: nx.Graph) -> Backbone:
    weight='weight'
    B = nx.Graph()
    for u in G:
        k = len(G[u])
        if k > 1:
            sum_w = sum(np.absolute(G[u][v][weight]) for v in G[u])
            for v in G[u]:
                w = G[u][v][weight]
                p_ij = float(np.absolute(w))/sum_w
                alpha_ij = 1 - \
                           (k-1) * integrate.quad(lambda x: (1-x)
                                                            ** (k-2), 0, p_ij)[0]
                # float('%.4f' % alpha_ij)
                B.add_edge(u, v, weight=w, p_value=float(alpha_ij))
    return Backbone(B, name="Disparity Filter", column="p_value", ascending=True)