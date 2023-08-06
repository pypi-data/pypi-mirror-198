import pandas as pd
import networkx as nx
from NetBone.Utils.utils import cumulative_dist
from NetBone.Filters import threshold_filter
from pandas import DataFrame

class Compare:
    def __init__(self):
        self.network = nx.Graph()
        self.backbones = []
        self.props = dict()
        self.value_name = 'p_value'
        self.filter = threshold_filter
        self.filter_value = 0.05

    def set_network(self, network):
        if isinstance(network, DataFrame):
            columns = list(network.columns)
            columns.remove('source')
            columns.remove('target')
            network = nx.from_pandas_edgelist(network, edge_attr=columns)
        self.network = network

    def add_backbone(self, backbone):
        self.backbones.append(backbone)

    def add_property(self, name, property):
        self.props[name] = property

    def set_filter(self, filter, value):
        self.filter = filter
        self.filter_value = value
        if "fraction" in filter.__name__:
            self.value_name = 'Fraction of Edges'
        elif "threshold" in filter.__name__:
            self.value_name = 'P-value'


    def properties(self):
        results = pd.DataFrame(index=['Original'] + [backbone.name for backbone in self.backbones])
        props_arrays = dict()

        for property in self.props:
            props_arrays[property] = [self.props[property](self.network, self.network)]

        for backbone in self.backbones:
            extracted_backbone = self.filter(backbone, value=self.filter_value)

            for property in self.props:
                props_arrays[property].append(self.props[property](self.network, extracted_backbone))


        for property in self.props:
            results[property] = props_arrays[property]

        return results.T


    def properties_progression(self, values):
        props_res = dict()
        for property in self.props:
            props_res[property] = pd.DataFrame(index=[backbone.name for backbone in self.backbones])
        for value in values:
            temp_props = dict()
            for property in self.props:
                temp_props[property] = []

            for backbone in self.backbones:
                extracted_backbone = self.filter(backbone, value=value)

                for property in self.props:
                    temp_props[property].append(self.props[property](self.network, extracted_backbone))

            for property in self.props:
                props_res[property][value] = temp_props[property]

        for res in props_res:
            props_res[res] = props_res[res].T
            props_res[res].index.name = self.value_name
        return props_res


    def cumulative_distribution(self, name, method, increasing=True):
        dist_res = dict()

        values = method(self.network)
        dist_res['Original'] = cumulative_dist(name, 'Original', values, increasing)

        for backbone in self.backbones:
                extracted_backbone = self.filter(backbone, value=self.filter_value)
                values = method(extracted_backbone)
                dist_res[backbone.name] = cumulative_dist(name, extracted_backbone.name, values, increasing)

        return dist_res



