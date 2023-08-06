from pandas import DataFrame
from networkx import Graph,to_pandas_edgelist

def global_threshold(data):

    if isinstance(data, DataFrame):
        table = data.copy()
    elif isinstance(data, Graph):
        table = to_pandas_edgelist(data)
        is_graph=True
    else:
        print("data should be a panads dataframe or nx graph")
        return

    table['score'] = table['weight']
    return table, "global_threshold"