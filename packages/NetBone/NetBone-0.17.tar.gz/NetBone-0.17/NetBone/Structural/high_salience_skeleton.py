
from collections import defaultdict
import networkx as nx
import pandas as pd
import warnings
from NetBone.Backbone import Backbone


# algo: high_salience_skeleton.py
warnings.filterwarnings('ignore')

def high_salience_skeleton(data):
    # sys.stderr.write("Calculating HSS score...\n")
    undirected=True
    return_self_loops=False

    if isinstance(data, pd.DataFrame):
        table = data.copy()
    elif isinstance(data, nx.Graph):
        table = nx.to_pandas_edgelist(data)
    else:
        print("data should be a panads dataframe or nx graph")
        return
    
    table["distance"] = 1.0 / table["weight"]
    nodes = set(table["source"]) | set(table["target"])
    G = nx.from_pandas_edgelist(
        table, source="source", target="target", edge_attr="distance", create_using=nx.DiGraph())
    cs = defaultdict(float)
    for s in nodes:
        pred = defaultdict(list)
        dist = {t: float("inf") for t in nodes}
        dist[s] = 0.0
        Q = defaultdict(list)
        for w in dist:
            Q[dist[w]].append(w)
        S = []
        while len(Q) > 0:
            v = Q[min(Q.keys())].pop(0)
            S.append(v)
            for _, w, l in G.edges(nbunch=[v, ], data=True):
                new_distance = dist[v] + l["distance"]
                if dist[w] > new_distance:
                    Q[dist[w]].remove(w)
                    dist[w] = new_distance
                    Q[dist[w]].append(w)
                    pred[w] = []
                if dist[w] == new_distance:
                    pred[w].append(v)
            while len(S) > 0:
                w = S.pop()
                for v in pred[w]:
                    cs[(v, w)] += 1.0
            Q = defaultdict(list, {k: v for k, v in Q.items() if len(v) > 0})
    table["score"] = table.apply(
        lambda x: cs[(x["source"], x["target"])] / len(nodes), axis=1)
    if not return_self_loops:
        table = table[table["source"] != table["target"]]
    if undirected:
        table["edge"] = table.apply(
            lambda x: "%s-%s" % (min(x["source"], x["target"]), max(x["source"], x["target"])), axis=1)
        table_maxscore = table.groupby(by="edge")["score"].sum().reset_index()
        table = table.merge(table_maxscore, on="edge", suffixes=("_min", ""))
        table = table.drop_duplicates(subset=["edge"])
        table = table.drop("edge", 1)
        table = table.drop("score_min", 1)

    G = nx.from_pandas_edgelist(table, edge_attr=['weight', 'score'])
    for u,v in G.edges():
        if G[u][v]['score']>=0.8:
            G[u][v]['high_salience_skeleton'] = True
        else:
            G[u][v]['high_salience_skeleton'] = False

    return Backbone(G, name="High Salience Skeleton Filter", column="high_salience_skeleton", ascending=False)
    # return table[["source", "target", "weight", "score"]], "high_salience_skeleton"


